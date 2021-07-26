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
    f: Optional[Callable[[param_t], return_t]]
    arg: param_t
    catch: Exceptions_t
    without: Exceptions_t
    ce: Optional[Captured_Exception[param_t, return_t]]

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
        self.ce = None

    def __call__(self, arg: param_t) -> return_t:
        self.arg = copy.deepcopy(arg)
        assert self.f is not None
        return self.f(arg)

    def __enter__(self) -> _exception_capturer[param_t, return_t]:
        return self

    def __exit__(
        self,
        _: Type[BaseException],
        __exc_value: BaseException,
        __traceback: TracebackType,
    ) -> bool:
        if not isinstance(__exc_value, self.catch):
            return False
        if isinstance(__exc_value, self.without):
            return False
        e = __exc_value
        trace = "\n".join(traceback.format_tb(__traceback))
        assert self.f is not None
        self.ce = Captured_Exception(self.f, self.arg, e, trace)
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
        def capturer(
            param: param_t,
        ) -> Union[return_t, Captured_Exception[param_t, return_t]]:
            cap = _exception_capturer(f, catch=catch, without=without)
            with cap:
                return cap(param)
            assert cap.ce is not None
            return cap.ce

        return functools.wraps(f)(capturer) if wraps else capturer

    if f is None:
        assert not len(args)
        return lambda f: wraps(f, wraps=True)
    elif not len(args):
        return wraps(f, wraps=False)
    else:
        return wraps(f, wraps=False)(*args)


def map(
    f: Callable[[param_t], return_t],
    args: Tuple[param_t, ...],
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
