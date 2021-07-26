# -*- coding: utf-8 -*-
from functools import wraps as _wraps
from typing import Any as _Any
from typing import Callable as _Callable
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
    *, input: _Callable[[_Tuple[()]], None], output: _Callable[[_return_t], None]
) -> _Callable[[_Callable[[], _return_t]], _Callable[[], _return_t]]:
    return _bind_checker_unsafe(input=input, output=output)


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


_checker_input_t = _TypeVar("_checker_input_t")


def _make_checker_unsafe(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[[_Tuple[_checker_input_t, ...]], None]:
    def checker(args: _Tuple[_checker_input_t, ...]) -> None:
        for arg in args:
            f(arg)

    return checker


def make_checker_0(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[[_Tuple[()]], None]:
    return _make_checker_unsafe(f)


def make_checker_1(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[[_Tuple[_checker_input_t]], None]:
    return _make_checker_unsafe(f)


def make_checker_2(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[[_Tuple[_checker_input_t, _checker_input_t]], None]:
    return _make_checker_unsafe(f)


def make_checker_3(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[[_Tuple[_checker_input_t, _checker_input_t, _checker_input_t]], None]:
    return _make_checker_unsafe(f)


def make_checker_4(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[
    [_Tuple[_checker_input_t, _checker_input_t, _checker_input_t, _checker_input_t]],
    None,
]:
    return _make_checker_unsafe(f)


def make_checker_5(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[
    [
        _Tuple[
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
        ]
    ],
    None,
]:
    return _make_checker_unsafe(f)


def make_checker_6(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[
    [
        _Tuple[
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
        ]
    ],
    None,
]:
    return _make_checker_unsafe(f)


def make_checker_7(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[
    [
        _Tuple[
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
        ]
    ],
    None,
]:
    return _make_checker_unsafe(f)


def make_checker_8(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[
    [
        _Tuple[
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
        ]
    ],
    None,
]:
    return _make_checker_unsafe(f)


def make_checker_9(
    f: _Callable[[_checker_input_t], None]
) -> _Callable[
    [
        _Tuple[
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
            _checker_input_t,
        ]
    ],
    None,
]:
    return _make_checker_unsafe(f)
