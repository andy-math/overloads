# -*- coding: utf-8 -*-
from __future__ import annotations

import copy
import functools
import traceback
from types import TracebackType
from typing import (
    Callable,
    Generic,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

param_t = TypeVar("param_t")
return_t = TypeVar("return_t")

BaseException_t = Type[BaseException]
Exceptions_t = Union[BaseException_t, Tuple[BaseException_t, ...]]


class Captured_Exception(Generic[param_t, return_t]):
    f: Optional[Callable[[param_t], return_t]]
    args: Tuple[param_t]
    exception: BaseException
    traceback: str

    def __init__(
        self,
        f: Callable[[param_t], return_t],
        args: param_t,
        exception: BaseException,
        trace: str,
    ):
        self.f = copy.deepcopy(f)
        self.args = (copy.deepcopy(args),)
        self.exception = copy.deepcopy(exception)
        self.traceback = trace

    def __call__(self) -> return_t:
        assert self.f is not None
        return self.f(*self.args)

    def __str__(self) -> str:
        assert self.f is not None
        fmtstr = "".join(
            [
                "{T}(f={f}, args={args}, e={e})".format(
                    T=Captured_Exception.__name__,
                    f="{}.{}".format(self.f.__module__, self.f.__name__),
                    args=self.args,
                    e=type(self.exception).__name__,
                ),
                " with the following exception:\n    {}\n".format(self.exception),
                "  traceback:\n{}".format(
                    "\n".join("    " + x for x in self.traceback.split("\n"))
                ),
            ]
        )
        return fmtstr


class _exception_capturer(Generic[param_t, return_t]):
    entered = False
    f: Optional[Callable[[param_t], return_t]]
    catch: Exceptions_t
    without: Exceptions_t
    e: BaseException
    trace: str

    def __init__(
        self,
        f: Callable[[param_t], return_t],
        *,
        catch: Exceptions_t = BaseException,
        without: Exceptions_t = ()
    ) -> None:
        self.f = f
        self.catch = catch
        self.without = without

    def __call__(
        self, arg: param_t
    ) -> Union[return_t, Captured_Exception[param_t, return_t]]:
        assert self.f is not None
        _arg = copy.deepcopy(arg)
        with self:
            return self.f(arg)
        return Captured_Exception(self.f, _arg, self.e, self.trace)

    def __enter__(self) -> _exception_capturer[param_t, return_t]:
        assert not self.entered
        self.entered = True
        return self

    def __exit__(
        self,
        _: Optional[Type[BaseException]],
        __exc_value: Optional[BaseException],
        __traceback: Optional[TracebackType],
    ) -> bool:
        if not isinstance(__exc_value, self.catch):
            return False
        if isinstance(__exc_value, self.without):
            return False
        if __exc_value is None or __traceback is None:
            return False  # pragma: no cover
        self.e = __exc_value
        self.trace = "\n".join(traceback.format_tb(__traceback))
        return True


@overload
def capture_exceptions(
    *, catch: Exceptions_t = BaseException, without: Exceptions_t = ()
) -> Callable[
    [Callable[[param_t], return_t]],
    Callable[[param_t], Union[return_t, Captured_Exception[param_t, return_t]]],
]:
    pass  # pragma: no cover


@overload
def capture_exceptions(
    f: Callable[[param_t], return_t],
    *,
    catch: Exceptions_t = BaseException,
    without: Exceptions_t = ()
) -> Callable[[param_t], Union[return_t, Captured_Exception[param_t, return_t]]]:
    pass  # pragma: no cover


@overload
def capture_exceptions(
    f: Callable[[param_t], return_t],
    arg: param_t,
    *,
    catch: Exceptions_t = BaseException,
    without: Exceptions_t = ()
) -> Union[return_t, Captured_Exception[param_t, return_t]]:
    pass  # pragma: no cover


def capture_exceptions(  # type: ignore
    f: Optional[Callable[[param_t], return_t]] = None,
    *args: param_t,
    catch: Exceptions_t = BaseException,
    without: Exceptions_t = ()
) -> Union[
    Callable[
        [Callable[[param_t], return_t]],
        Callable[[param_t], Union[return_t, Captured_Exception[param_t, return_t]]],
    ],
    Callable[[param_t], Union[return_t, Captured_Exception[param_t, return_t]]],
    return_t,
    Captured_Exception[param_t, return_t],
]:

    assert len(args) <= 1

    def wraps(
        f: Callable[[param_t], return_t], *, wraps: bool
    ) -> Callable[[param_t], Union[return_t, Captured_Exception[param_t, return_t]]]:
        ecap: Callable[
            [param_t],
            Union[
                return_t,
                Captured_Exception[param_t, return_t],
            ],
        ]
        ecap = _exception_capturer(f, catch=catch, without=without)
        if wraps:
            ecap = functools.wraps(f)(ecap)
        return ecap

    if f is None:
        assert args is None
        return lambda f: wraps(f, wraps=True)
    elif not len(args):
        return wraps(f, wraps=False)
    else:
        return wraps(f, wraps=False)(*args)


def map(
    f: Callable[[param_t], return_t],
    args: Sequence[param_t],
    *,
    catch: Exceptions_t = BaseException,
    without: Exceptions_t = ()
) -> List[Union[return_t, Captured_Exception[param_t, return_t]]]:
    result_list: List[Union[return_t, Captured_Exception[param_t, return_t]]] = []
    for idx, arg in enumerate(args):
        result = capture_exceptions(f, arg, catch=catch, without=without)
        if isinstance(result, Captured_Exception):
            print("[{}]: {}".format(idx, result))
        result_list.append(result)
    return result_list
