# -*- coding: utf-8 -*-
from typing import Any

import numpy
from overloads import dyn_typing, tuplize
from overloads.capture_exceptions import Captured_Exception, capture_exceptions
from overloads.dyn_typing import SizeConst, SizeVar


class Test():
    def test_NDArray(self) -> None:
        T = dyn_typing.NDArray(numpy.float64, (SizeConst(2), SizeConst(4)))
        assert T.isinstance(numpy.zeros((2, 4)))
        assert not T.isinstance(numpy.zeros((2, 5)))
        assert not T.isinstance(numpy.zeros((2, 4), dtype=numpy.int64))
        assert not T.isinstance(numpy.zeros((2, 4, 5)))
        assert not T.isinstance(1)
        assert T.isinstance(numpy.zeros((2, 4), order='F'))
        a = SizeVar()
        T = dyn_typing.NDArray(numpy.float64, (a, a + 1))
        assert T.isinstance(numpy.zeros((2, 3)))
        assert T.isinstance(numpy.zeros((3, 4)))
        assert not T.isinstance(numpy.zeros((3, 3)))

    def test_Bool(self) -> None:
        assert dyn_typing.Bool().isinstance(True)
        assert dyn_typing.Bool().isinstance(False)
        assert not dyn_typing.Bool().isinstance(1)

    def test_Int(self) -> None:
        assert dyn_typing.Int().isinstance(1)
        assert not dyn_typing.Int().isinstance(1.0)

    def test_Float(self) -> None:
        assert dyn_typing.Float().isinstance(1.0)
        assert not dyn_typing.Float().isinstance(1)

    def test_Callable(self) -> None:
        def f() -> None:
            pass

        assert dyn_typing.Callable().isinstance(f)
        assert not dyn_typing.Callable().isinstance(1)

    def test_Class(self) -> None:
        assert dyn_typing.Class(int).isinstance(1)
        assert not dyn_typing.Class(int).isinstance(1.0)

    def test_Optional(self) -> None:
        Int = dyn_typing.Int()
        assert dyn_typing.Optional(Int).isinstance(1)
        assert not dyn_typing.Optional(Int).isinstance(1.0)
        assert dyn_typing.Optional(Int).isinstance(None)

    def test_Union(self) -> None:
        Int = dyn_typing.Int()
        Float = dyn_typing.Float()
        T = dyn_typing.Union(Int, Float)
        assert T.isinstance(1)
        assert T.isinstance(1.0)
        assert not T.isinstance(None)

    def test_List(self) -> None:
        Int = dyn_typing.Int()
        T = dyn_typing.List(Int, SizeConst(2))
        assert not T.isinstance([1, 1, 1])
        assert not T.isinstance([1, 1.0])
        assert T.isinstance([1, 1])
        assert not T.isinstance(None)
        a = SizeVar()
        aExpr = a * 2
        T = dyn_typing.List(Int, aExpr)
        assert a.eqn(1)
        assert T.isinstance([1, 1])
        assert a.eqn(1)
        assert not T.isinstance([1, 1, 1])

    def test_Tuple(self) -> None:
        Int = dyn_typing.Int()
        Float = dyn_typing.Float()
        T = dyn_typing.Tuple((Int, Float))
        assert not T.isinstance((1, 1, 1))
        assert T.isinstance((1, 1.0))
        assert not T.isinstance((1, 1))
        assert not T.isinstance([1, 1.0])

    def test_Dict(self) -> None:
        T = dyn_typing.Dict({'a': dyn_typing.Int(), 'b': dyn_typing.Float()})
        assert T.isinstance({'b': 1.0, 'a': 1})
        assert not T.isinstance({'a': 1, 'b': 1})
        assert not T.isinstance({'a': 1, 'c': 1.0})
        assert not T.isinstance([])

    def test_Expr(self) -> None:
        a = SizeConst(4)
        assert (-a).eqn(-4)
        assert (a + 3).eqn(4 + 3)
        assert (a - 3).eqn(4 - 3)
        assert (a * 3).eqn(4 * 3)
        assert (a / 2).eqn(int(4 / 2))
        assert (a // 3).eqn(4 // 3)
        assert (a % 3).eqn(4 % 3)
        assert (a**3).eqn(int(4**3))
        assert (3 + a).eqn(3 + 4)
        assert (3 - a).eqn(3 - 4)
        assert (3 * a).eqn(3 * 4)
        assert (8 / a).eqn(int(8 / 4))
        assert (3 // a).eqn(3 // 4)
        assert (3 % a).eqn(3 % 4)
        assert (3**a).eqn(int(3**4))
        assert (a + a + a).eqn(4 + 4 + 4)


dynInt = dyn_typing.Int()


@tuplize.tuplize_0
@dyn_typing.dyn_check_0(input=(), output=dyn_typing.Class(type(None)))
def f0() -> None:
    return None


@tuplize.tuplize_1
@dyn_typing.dyn_check_1(input=(dynInt, ), output=dyn_typing.Class(type(None)))
def f1(a: Any) -> None:
    return None


@tuplize.tuplize_2
@dyn_typing.dyn_check_2(input=(dynInt, dynInt), output=dyn_typing.Class(type(None)))
def f2(a: Any, b: Any) -> None:
    return None


@tuplize.tuplize_3
@dyn_typing.dyn_check_3(input=(dynInt, dynInt, dynInt), output=dyn_typing.Class(type(None)))
def f3(a: Any, b: Any, c: Any) -> None:
    return None


@tuplize.tuplize_4
@dyn_typing.dyn_check_4(input=(dynInt, dynInt, dynInt, dynInt),
                        output=dyn_typing.Class(type(None)))
def f4(a: Any, b: Any, c: Any, d: Any) -> None:
    return None


@tuplize.tuplize_5
@dyn_typing.dyn_check_5(input=(dynInt, dynInt, dynInt, dynInt, dynInt),
                        output=dyn_typing.Class(type(None)))
def f5(a: Any, b: Any, c: Any, d: Any, e: Any) -> None:
    return None


@tuplize.tuplize_6
@dyn_typing.dyn_check_6(input=(dynInt, dynInt, dynInt, dynInt, dynInt, dynInt),
                        output=dyn_typing.Class(type(None)))
def f6(a: Any, b: Any, c: Any, d: Any, e: Any, f: Any) -> None:
    return None


@tuplize.tuplize_7
@dyn_typing.dyn_check_7(input=(dynInt, dynInt, dynInt, dynInt, dynInt, dynInt, dynInt),
                        output=dyn_typing.Class(type(None)))
def f7(a: Any, b: Any, c: Any, d: Any, e: Any, f: Any, g: Any) -> None:
    return None


@tuplize.tuplize_8
@dyn_typing.dyn_check_8(input=(dynInt, dynInt, dynInt, dynInt, dynInt, dynInt, dynInt, dynInt),
                        output=dyn_typing.Class(type(None)))
def f8(a: Any, b: Any, c: Any, d: Any, e: Any, f: Any, g: Any, h: Any) -> None:
    return None


@tuplize.tuplize_9
@dyn_typing.dyn_check_9(input=(dynInt, dynInt, dynInt, dynInt, dynInt, dynInt, dynInt, dynInt,
                               dynInt),
                        output=dyn_typing.Class(type(None)))
def f9(a: Any, b: Any, c: Any, d: Any, e: Any, f: Any, g: Any, h: Any, ii: Any) -> None:
    return None


fff = (f0, f1, f2, f3, f4, f5, f6, f7, f8, f9)

MM = SizeVar()
NN = SizeVar()
KK = SizeVar()


@tuplize.tuplize_2
@dyn_typing.dyn_check_2(input=(dyn_typing.NDArray(numpy.float64, (MM, KK)),
                               dyn_typing.NDArray(numpy.float64, (KK, NN))),
                        output=dyn_typing.NDArray(numpy.float64, (MM, NN)))
def matmul(a: Any, b: Any) -> Any:
    return a @ b


@tuplize.tuplize_2
@dyn_typing.dyn_check_2(input=(dyn_typing.NDArray(numpy.float64, (MM, KK)),
                               dyn_typing.NDArray(numpy.float64, (KK, NN))),
                        output=dyn_typing.NDArray(numpy.float64, (MM, NN)))
def matmulERR(a: Any, b: Any) -> Any:
    return numpy.zeros((1, 1))


class TestDynChk():
    def test_matmul(self) -> None:
        assert matmul((numpy.zeros((2, 3)), numpy.zeros((3, 4)))).shape == (2, 4)
        assert matmul((numpy.zeros((7, 6)), numpy.zeros((6, 5)))).shape == (7, 5)
        ce = capture_exceptions(matmul, (numpy.zeros((7, 6)), numpy.zeros((3, 4))))
        assert isinstance(ce, Captured_Exception)
        assert isinstance(ce.exception, AssertionError)

    def test_matmul_ERRimpl(self) -> None:
        assert matmulERR((numpy.zeros((1, 6)), numpy.zeros((6, 1)))).shape == (1, 1)
        ce = capture_exceptions(matmulERR, (numpy.zeros((7, 6)), numpy.zeros((6, 4))))
        assert isinstance(ce, Captured_Exception)
        assert isinstance(ce.exception, AssertionError)

    def test_1(self) -> None:
        dataOK = 1
        dataERR = None
        fff[0](())
        fff[1]((dataOK, ))
        fff[2]((dataOK, dataOK))
        fff[3]((dataOK, dataOK, dataOK))
        fff[4]((dataOK, dataOK, dataOK, dataOK))
        fff[5]((dataOK, dataOK, dataOK, dataOK, dataOK))
        fff[6]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        fff[7]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        fff[8]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        fff[9]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        ce_1 = capture_exceptions(fff[1], (dataERR, ))
        ce_2 = capture_exceptions(fff[2], (dataOK, dataERR))
        ce_3 = capture_exceptions(fff[3], (dataOK, dataOK, dataERR))
        ce_4 = capture_exceptions(fff[4], (dataOK, dataOK, dataOK, dataERR))
        ce_5 = capture_exceptions(fff[5], (dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_6 = capture_exceptions(fff[6], (dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_7 = capture_exceptions(fff[7],
                                  (dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_8 = capture_exceptions(
            fff[8], (dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_9 = capture_exceptions(
            fff[9], (dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
        assert isinstance(ce_1, Captured_Exception)
        assert isinstance(ce_2, Captured_Exception)
        assert isinstance(ce_3, Captured_Exception)
        assert isinstance(ce_4, Captured_Exception)
        assert isinstance(ce_5, Captured_Exception)
        assert isinstance(ce_6, Captured_Exception)
        assert isinstance(ce_7, Captured_Exception)
        assert isinstance(ce_8, Captured_Exception)
        assert isinstance(ce_9, Captured_Exception)
        assert isinstance(ce_1.exception, AssertionError)
        assert isinstance(ce_2.exception, AssertionError)
        assert isinstance(ce_3.exception, AssertionError)
        assert isinstance(ce_4.exception, AssertionError)
        assert isinstance(ce_5.exception, AssertionError)
        assert isinstance(ce_6.exception, AssertionError)
        assert isinstance(ce_7.exception, AssertionError)
        assert isinstance(ce_8.exception, AssertionError)
        assert isinstance(ce_9.exception, AssertionError)
        cce_2 = capture_exceptions(fff[2], (dataERR, dataOK))
        cce_3 = capture_exceptions(fff[3], (dataERR, dataOK, dataOK))
        cce_4 = capture_exceptions(fff[4], (dataERR, dataOK, dataOK, dataOK))
        cce_5 = capture_exceptions(fff[5], (dataERR, dataOK, dataOK, dataOK, dataOK))
        cce_6 = capture_exceptions(fff[6], (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK))
        cce_7 = capture_exceptions(fff[7],
                                   (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        cce_8 = capture_exceptions(
            fff[8], (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        cce_9 = capture_exceptions(
            fff[9], (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        assert isinstance(cce_2, Captured_Exception)
        assert isinstance(cce_3, Captured_Exception)
        assert isinstance(cce_4, Captured_Exception)
        assert isinstance(cce_5, Captured_Exception)
        assert isinstance(cce_6, Captured_Exception)
        assert isinstance(cce_7, Captured_Exception)
        assert isinstance(cce_8, Captured_Exception)
        assert isinstance(cce_9, Captured_Exception)
        assert isinstance(cce_2.exception, AssertionError)
        assert isinstance(cce_3.exception, AssertionError)
        assert isinstance(cce_4.exception, AssertionError)
        assert isinstance(cce_5.exception, AssertionError)
        assert isinstance(cce_6.exception, AssertionError)
        assert isinstance(cce_7.exception, AssertionError)
        assert isinstance(cce_8.exception, AssertionError)
        assert isinstance(cce_9.exception, AssertionError)
