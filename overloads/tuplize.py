from functools import wraps
from typing import Any, Callable, Tuple, TypeVar

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_T6 = TypeVar('_T6')
_T7 = TypeVar('_T7')
_T8 = TypeVar('_T8')
_T9 = TypeVar('_T9')
_return_t = TypeVar('_return_t')


def _tuplize_unsafe(f: Callable[..., _return_t]) -> Callable[[Tuple[Any, ...]], _return_t]:
    @wraps(f)
    def wrapper(args: Tuple[Any, ...]) -> _return_t:
        return f(*args)

    return wrapper


def tuplize_0(f: Callable[[], _return_t]) -> Callable[[Tuple[()]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_1(f: Callable[[_T1], _return_t]) -> Callable[[Tuple[_T1]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_2(f: Callable[[_T1, _T2], _return_t]) -> Callable[[Tuple[_T1, _T2]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_3(
        f: Callable[[_T1, _T2, _T3], _return_t]) -> Callable[[Tuple[_T1, _T2, _T3]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_4(
    f: Callable[[_T1, _T2, _T3, _T4],
                _return_t]) -> Callable[[Tuple[_T1, _T2, _T3, _T4]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_5(
    f: Callable[[_T1, _T2, _T3, _T4, _T5], _return_t]
) -> Callable[[Tuple[_T1, _T2, _T3, _T4, _T5]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_6(
    f: Callable[[_T1, _T2, _T3, _T4, _T5, _T6], _return_t]
) -> Callable[[Tuple[_T1, _T2, _T3, _T4, _T5, _T6]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_7(
    f: Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7], _return_t]
) -> Callable[[Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_8(
    f: Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8], _return_t]
) -> Callable[[Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8]], _return_t]:
    return _tuplize_unsafe(f)


def tuplize_9(
    f: Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9], _return_t]
) -> Callable[[Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9]], _return_t]:
    return _tuplize_unsafe(f)


if __name__ == '__main__':

    @tuplize_0
    def coeff0() -> int:
        return 1

    @tuplize_3
    def coeff3(a: int, b: float, c: Tuple[()]) -> Tuple[int, float, Tuple[()]]:
        return a, b, c

    coeff0(())
    coeff3((1, 1, ()))
