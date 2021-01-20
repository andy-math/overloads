from functools import wraps as _wraps
from typing import Any as _Any
from typing import Callable as _Callable
from typing import Tuple as _Tuple
from typing import TypeVar as _TypeVar

_T1 = _TypeVar('_T1')
_T2 = _TypeVar('_T2')
_T3 = _TypeVar('_T3')
_T4 = _TypeVar('_T4')
_T5 = _TypeVar('_T5')
_T6 = _TypeVar('_T6')
_T7 = _TypeVar('_T7')
_T8 = _TypeVar('_T8')
_T9 = _TypeVar('_T9')
_return_t = _TypeVar('_return_t')


def _tuplize_unsafe(f: _Callable[..., _return_t]) -> _Callable[[_Tuple[_Any, ...]], _return_t]:
    @_wraps(f)
    def wrapper(args: _Tuple[_Any, ...]) -> _return_t:
        return f(*args)

    return wrapper


def tuplize_0(f: _Callable[[], _return_t]) -> _Callable[[_Tuple[()]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_1(f: _Callable[[_T1], _return_t]) -> _Callable[[_Tuple[_T1]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_2(f: _Callable[[_T1, _T2], _return_t]) -> _Callable[[_Tuple[_T1, _T2]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_3(
        f: _Callable[[_T1, _T2, _T3], _return_t]) -> _Callable[[_Tuple[_T1, _T2, _T3]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_4(
    f: _Callable[[_T1, _T2, _T3, _T4], _return_t]
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_5(
    f: _Callable[[_T1, _T2, _T3, _T4, _T5], _return_t]
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_6(
    f: _Callable[[_T1, _T2, _T3, _T4, _T5, _T6], _return_t]
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_7(
    f: _Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7], _return_t]
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_8(
    f: _Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8], _return_t]
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_9(
    f: _Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9], _return_t]
) -> _Callable[[_Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9]], _return_t]:
    return _tuplize_unsafe(f)


if __name__ == '__main__':

    @tuplize_0
    def coeff0() -> int:
        return 1

    @tuplize_3
    def coeff3(a: int, b: float, c: _Tuple[()]) -> _Tuple[int, float, _Tuple[()]]:
        return a, b, c

    coeff0(())
    coeff3((1, 1, ()))
