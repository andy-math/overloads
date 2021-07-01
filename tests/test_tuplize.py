from typing import Any, Tuple

from overloads import tuplize


@tuplize.tuplize_0
def f_0() -> Tuple[()]:
    return ()


@tuplize.tuplize_1
def f_1(a: Any) -> Tuple[Any]:
    return (a,)


@tuplize.tuplize_2
def f_2(a: Any, b: Any) -> Tuple[Any, Any]:
    return (a, b)


@tuplize.tuplize_3
def f_3(a: Any, b: Any, c: Any) -> Tuple[Any, Any, Any]:
    return (a, b, c)


@tuplize.tuplize_4
def f_4(a: Any, b: Any, c: Any, d: Any) -> Tuple[Any, Any, Any, Any]:
    return (a, b, c, d)


@tuplize.tuplize_5
def f_5(a: Any, b: Any, c: Any, d: Any, e: Any) -> Tuple[Any, Any, Any, Any, Any]:
    return (a, b, c, d, e)


@tuplize.tuplize_6
def f_6(
    a: Any, b: Any, c: Any, d: Any, e: Any, f: Any
) -> Tuple[Any, Any, Any, Any, Any, Any]:
    return (a, b, c, d, e, f)


@tuplize.tuplize_7
def f_7(
    a: Any, b: Any, c: Any, d: Any, e: Any, f: Any, g: Any
) -> Tuple[Any, Any, Any, Any, Any, Any, Any]:
    return (a, b, c, d, e, f, g)


@tuplize.tuplize_8
def f_8(
    a: Any, b: Any, c: Any, d: Any, e: Any, f: Any, g: Any, h: Any
) -> Tuple[Any, Any, Any, Any, Any, Any, Any, Any]:
    return (a, b, c, d, e, f, g, h)


@tuplize.tuplize_9
def f_9(
    a: Any, b: Any, c: Any, d: Any, e: Any, f: Any, g: Any, h: Any, i: Any
) -> Tuple[Any, Any, Any, Any, Any, Any, Any, Any, Any]:
    return (a, b, c, d, e, f, g, h, i)


f = (f_0, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9)


class Test:
    def test_tup(self) -> None:
        assert f[0](()) == ()
        assert f[1]((1,)) == (1,)
        assert f[2]((1, 2)) == (1, 2)
        assert f[3]((1, 2, 3)) == (1, 2, 3)
        assert f[4]((1, 2, 3, 4)) == (1, 2, 3, 4)
        assert f[5]((1, 2, 3, 4, 5)) == (1, 2, 3, 4, 5)
        assert f[6]((1, 2, 3, 4, 5, 6)) == (1, 2, 3, 4, 5, 6)
        assert f[7]((1, 2, 3, 4, 5, 6, 7)) == (1, 2, 3, 4, 5, 6, 7)
        assert f[8]((1, 2, 3, 4, 5, 6, 7, 8)) == (1, 2, 3, 4, 5, 6, 7, 8)
        assert f[9]((1, 2, 3, 4, 5, 6, 7, 8, 9)) == (1, 2, 3, 4, 5, 6, 7, 8, 9)
