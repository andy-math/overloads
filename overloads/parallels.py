# -*- coding: utf-8 -*-
import builtins
import multiprocessing.pool
from typing import (Any, Callable, Dict, List, Optional, Sequence, Tuple, TypeVar, Union)

import psutil  # type: ignore
from mypy_extensions import NamedArg

from capture_exceptions import Captured_Exception, capture_exceptions

T = TypeVar('T')
pool: Optional[multiprocessing.pool.Pool] = None
output: List[str] = []


def launch_parpool() -> None:
    global pool
    multiprocessing.set_start_method('spawn')
    processes: int = psutil.cpu_count(logical=False)
    pool = multiprocessing.pool.Pool(processes)


def print(*args: Any, end: str = '\n') -> None:
    output.append(' '.join((str(arg) for arg in args)) + end)


def helper(
    info_tuple: Tuple[int, Callable[..., T], Tuple[Any]]
) -> Tuple[int, Union[T, Captured_Exception[T]], str]:
    idx, f, args = info_tuple
    value = capture_exceptions(f, *args)
    output_str = ''.join(output)
    output.clear()
    return idx, value, output_str


def parfor(
    f: Callable[..., T],
    args_list: Sequence[Tuple[Any]],
    *,
    print: Callable[[str, NamedArg(str, 'end')], None] = builtins.print  # noqa: F821
) -> List[Union[T, Captured_Exception[T]]]:
    if pool is None:
        launch_parpool()
        assert pool is not None
    helper_args_list = ((idx, f, args) for idx, args in enumerate(args_list))
    result_dict: Dict[int, Union[T, Captured_Exception[T]]] = {}
    for idx, result, output in pool.imap_unordered(helper, helper_args_list):
        print(output, end='')
        if isinstance(result, Captured_Exception):
            print('[{}]: {}\n'.format(idx, result), end='')
        result_dict[idx] = result
    result_list = [result_dict[idx] for idx in range(len(args_list))]
    return result_list


def show(x: float) -> float:
    import time
    time.sleep(0.1)
    print(multiprocessing.current_process(), x)
    assert x < 5, "x应当小于5"
    return x


if __name__ == '__main__':
    builtins.print(parfor(show, [(x, ) for x in range(10)]))
