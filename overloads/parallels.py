# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
import multiprocessing
import multiprocessing.pool
import multiprocessing.synchronize
from typing import Callable, Dict, List, Optional, Sequence, Tuple, TypeVar, Union

import psutil  # type: ignore

from overloads.capture_exceptions import Captured_Exception, capture_exceptions

param_t = TypeVar("param_t")
return_t = TypeVar("return_t")
pool: Optional[multiprocessing.pool.Pool] = None
barrier: Optional[multiprocessing.synchronize.Barrier] = None
_spawn_setted: bool = False


def _set_barrier(b: multiprocessing.synchronize.Barrier) -> None:
    global barrier  # pragma: no cover
    barrier = b  # pragma: no cover


def set_windows_compatible_start_method() -> None:
    global _spawn_setted
    if not _spawn_setted:
        multiprocessing.set_start_method("spawn")
        _spawn_setted = True


def launch_parpool() -> None:
    global pool, barrier
    set_windows_compatible_start_method()
    processes: int = psutil.cpu_count(logical=False)
    barrier = multiprocessing.Barrier(processes)
    pool = multiprocessing.pool.Pool(processes, _set_barrier, (barrier,))


def parfor_helper(
    info_tuple: Tuple[int, Callable[[param_t], return_t], param_t]
) -> Tuple[int, Union[return_t, Captured_Exception[param_t, return_t]]]:
    idx, f, arg = info_tuple
    value = capture_exceptions(f, arg)
    return idx, value


def print_without_line_feed(*values: object) -> None:
    print(*values, end="")


def parfor(
    f: Callable[[param_t], return_t],
    arg_list: Sequence[param_t],
    *,
    callback: Optional[
        Callable[[Union[return_t, Captured_Exception[param_t, return_t]]], None]
    ] = None,
    print_time: bool = False,
    task_name: Optional[str] = None,
) -> List[Union[return_t, Captured_Exception[param_t, return_t]]]:
    def timedelta2str(T: datetime.timedelta) -> str:
        s = str(T)
        return s[: s.rfind(".")]

    if pool is None:
        launch_parpool()
        assert pool is not None
    helper_arg_list = ((idx, f, arg) for idx, arg in enumerate(arg_list))
    result_dict: Dict[int, Union[return_t, Captured_Exception[param_t, return_t]]] = {}
    num_total = len(arg_list)
    num_finished = 0
    time_start = datetime.datetime.now()
    for idx, result in pool.imap_unordered(parfor_helper, helper_arg_list):
        num_finished += 1
        time_now = datetime.datetime.now()
        time_elapsed = time_now - time_start
        time_need = ((num_total - num_finished) / num_finished) * time_elapsed
        if isinstance(result, Captured_Exception):
            print_without_line_feed("[{}]: {}\n".format(idx, result))
        if print_time:
            assert task_name is not None
            print_without_line_feed(
                "{}\n\t已完成{}/{}, {:05.2f}%, 已用{}, 预计还需{}, 结束时间{:%Y-%m-%d %H:%M:%S}\n".format(  # noqa: E501
                    task_name,
                    num_finished,
                    num_total,
                    100 * num_finished / num_total,
                    timedelta2str(time_elapsed),
                    timedelta2str(time_need),
                    time_now + time_need,
                )
            )
        if callback is not None:
            callback(result)
        result_dict[idx] = result
    result_list = [result_dict[idx] for idx in range(len(arg_list))]
    return result_list


def forall_helper(info_tuple: Tuple[Callable[[param_t], None], param_t]) -> None:
    assert barrier is not None  # pragma: no cover
    f, arg = info_tuple  # pragma: no cover
    f(arg)  # pragma: no cover
    barrier.wait()  # pragma: no cover


def forall(f: Callable[[param_t], None], arg_list: param_t) -> None:
    parfor(
        forall_helper,
        [(f, arg_list) for _ in range(psutil.cpu_count(logical=False))],
    )
    assert barrier is not None
    barrier.reset()
