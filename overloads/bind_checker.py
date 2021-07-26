# -*- coding: utf-8 -*-
from functools import wraps as _wraps
from typing import Any as _Any
from typing import Callable
from typing import Callable as _Callable
from typing import Tuple
from typing import Tuple as _Tuple
from typing import TypeVar as _TypeVar

_return_t = _TypeVar("_return_t")
_T1 = _TypeVar("_T1")
_T2 = _TypeVar("_T2")
_T3 = _TypeVar("_T3")
_T4 = _TypeVar("_T4")
_T5 = _TypeVar("_T5")
_T6 = _TypeVar("_T6")
_T7 = _TypeVar("_T7")
_T8 = _TypeVar("_T8")
_T9 = _TypeVar("_T9")


def _bind_checker_unsafe(
    *, input: _Callable[[_Any], None], output: _Callable[[_return_t], None]
) -> _Callable[[_Callable[..., _return_t]], _Callable[..., _return_t]]:
    def decorator(f: _Callable[..., _return_t]) -> _Callable[..., _return_t]:
        @_wraps(f)
        def wrapper(*args: _Any) -> _return_t:
            input(args)
            value = f(*args)
            output(value)
            return value

        return wrapper

    return decorator


def bind_checker_0(
    *, output: _Callable[[_return_t], None]
) -> _Callable[[_Callable[[], _return_t]], _Callable[[], _return_t]]:
    return _bind_checker_unsafe(input=lambda _: None, output=output)


def bind_checker_1(
    *, input: _Callable[[_Tuple[_T1]], None], output: _Callable[[_return_t], None]
) -> _Callable[[_Callable[[_T1], _return_t]], _Callable[[_T1], _return_t]]:
    return _bind_checker_unsafe(input=input, output=output)


def bind_checker_2(
    *, input: _Callable[[_Tuple[_T1, _T2]], None], output: _Callable[[_return_t], None]
) -> _Callable[[_Callable[[_T1, _T2], _return_t]], _Callable[[_T1, _T2], _return_t]]:
    return _bind_checker_unsafe(input=input, output=output)


def bind_checker_3(
    *,
    input: _Callable[[_Tuple[_T1, _T2, _T3]], None],
    output: _Callable[[_return_t], None]
) -> _Callable[
    [_Callable[[_T1, _T2, _T3], _return_t]], _Callable[[_T1, _T2, _T3], _return_t]
]:
    return _bind_checker_unsafe(input=input, output=output)


def bind_checker_4(
    *,
    input: _Callable[[_Tuple[_T1, _T2, _T3, _T4]], None],
    output: _Callable[[_return_t], None]
) -> _Callable[
    [_Callable[[_T1, _T2, _T3, _T4], _return_t]],
    _Callable[[_T1, _T2, _T3, _T4], _return_t],
]:
    return _bind_checker_unsafe(input=input, output=output)


def bind_checker_5(
    *,
    input: _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5]], None],
    output: _Callable[[_return_t], None]
) -> _Callable[
    [_Callable[[_T1, _T2, _T3, _T4, _T5], _return_t]],
    _Callable[[_T1, _T2, _T3, _T4, _T5], _return_t],
]:
    return _bind_checker_unsafe(input=input, output=output)


def bind_checker_6(
    *,
    input: _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6]], None],
    output: _Callable[[_return_t], None]
) -> _Callable[
    [_Callable[[_T1, _T2, _T3, _T4, _T5, _T6], _return_t]],
    _Callable[[_T1, _T2, _T3, _T4, _T5, _T6], _return_t],
]:
    return _bind_checker_unsafe(input=input, output=output)


def bind_checker_7(
    *,
    input: _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7]], None],
    output: _Callable[[_return_t], None]
) -> _Callable[
    [_Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7], _return_t]],
    _Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7], _return_t],
]:
    return _bind_checker_unsafe(input=input, output=output)


def bind_checker_8(
    *,
    input: _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8]], None],
    output: _Callable[[_return_t], None]
) -> _Callable[
    [_Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8], _return_t]],
    _Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8], _return_t],
]:
    return _bind_checker_unsafe(input=input, output=output)


def bind_checker_9(
    *,
    input: _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9]], None],
    output: _Callable[[_return_t], None]
) -> _Callable[
    [_Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9], _return_t]],
    _Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9], _return_t],
]:
    return _bind_checker_unsafe(input=input, output=output)


def _make_checker_unsafe(
    checkers: Tuple[_Callable[[_Any], None], ...]
) -> _Callable[[_Tuple[_Any, ...]], None]:
    def checker(args: _Tuple[_Any, ...]) -> None:
        assert len(checkers) == len(args)
        for f, arg in zip(checkers, args):
            f(arg)

    return checker


def make_checker_1(f1: Callable[[_T1], None]) -> _Callable[[_Tuple[_T1]], None]:
    return _make_checker_unsafe((f1,))


def make_checker_2(
    f1: Callable[[_T1], None], f2: Callable[[_T2], None]
) -> _Callable[[_Tuple[_T1, _T2]], None]:
    return _make_checker_unsafe((f1, f2))


def make_checker_3(
    f1: Callable[[_T1], None], f2: Callable[[_T2], None], f3: Callable[[_T3], None]
) -> _Callable[[_Tuple[_T1, _T2, _T3]], None]:
    return _make_checker_unsafe((f1, f2, f3))


def make_checker_4(
    f1: Callable[[_T1], None],
    f2: Callable[[_T2], None],
    f3: Callable[[_T3], None],
    f4: Callable[[_T4], None],
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4]], None]:
    return _make_checker_unsafe((f1, f2, f3, f4))


def make_checker_5(
    f1: Callable[[_T1], None],
    f2: Callable[[_T2], None],
    f3: Callable[[_T3], None],
    f4: Callable[[_T4], None],
    f5: Callable[[_T5], None],
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5]], None]:
    return _make_checker_unsafe((f1, f2, f3, f4, f5))


def make_checker_6(
    f1: Callable[[_T1], None],
    f2: Callable[[_T2], None],
    f3: Callable[[_T3], None],
    f4: Callable[[_T4], None],
    f5: Callable[[_T5], None],
    f6: Callable[[_T6], None],
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6]], None]:
    return _make_checker_unsafe((f1, f2, f3, f4, f5, f6))


def make_checker_7(
    f1: Callable[[_T1], None],
    f2: Callable[[_T2], None],
    f3: Callable[[_T3], None],
    f4: Callable[[_T4], None],
    f5: Callable[[_T5], None],
    f6: Callable[[_T6], None],
    f7: Callable[[_T7], None],
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7]], None]:
    return _make_checker_unsafe((f1, f2, f3, f4, f5, f6, f7))


def make_checker_8(
    f1: Callable[[_T1], None],
    f2: Callable[[_T2], None],
    f3: Callable[[_T3], None],
    f4: Callable[[_T4], None],
    f5: Callable[[_T5], None],
    f6: Callable[[_T6], None],
    f7: Callable[[_T7], None],
    f8: Callable[[_T8], None],
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8]], None]:
    return _make_checker_unsafe((f1, f2, f3, f4, f5, f6, f7, f8))


def make_checker_9(
    f1: Callable[[_T1], None],
    f2: Callable[[_T2], None],
    f3: Callable[[_T3], None],
    f4: Callable[[_T4], None],
    f5: Callable[[_T5], None],
    f6: Callable[[_T6], None],
    f7: Callable[[_T7], None],
    f8: Callable[[_T8], None],
    f9: Callable[[_T9], None],
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9]], None]:
    return _make_checker_unsafe((f1, f2, f3, f4, f5, f6, f7, f8, f9))
