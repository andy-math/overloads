# -*- coding: utf-8 -*-
import numpy
from overloads import dyn_typing
from overloads.dyn_typing import SizeConst, SizeVar


class Test():
    def test_NDArray(self) -> None:
        T = dyn_typing.NDArray(numpy.float64, (SizeConst(2), SizeConst(4)))
        assert T.isinstance(numpy.zeros((2, 4)))
        assert not T.isinstance(numpy.zeros((2, 5)))
        assert not T.isinstance(numpy.zeros((2, 4), dtype=numpy.int64))
        assert not T.isinstance(numpy.zeros((2, 4, 5)))
        assert not T.isinstance(1)
        assert not T.isinstance(numpy.zeros((2, 4), order='F'))
        a = SizeVar()
        T = dyn_typing.NDArray(numpy.float64, (a, a + 1))
        assert T.isinstance(numpy.zeros((2, 3)))
        assert T.isinstance(numpy.zeros((3, 4)))
        assert not T.isinstance(numpy.zeros((3, 3)))

    def test_Int(self) -> None:
        assert dyn_typing.Int().isinstance(1)
        assert not dyn_typing.Int().isinstance(1.0)

    def test_Float(self) -> None:
        assert dyn_typing.Float().isinstance(1.0)
        assert not dyn_typing.Float().isinstance(1)

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

    def test_Tuple(self) -> None:
        Int = dyn_typing.Int()
        Float = dyn_typing.Float()
        T = dyn_typing.Tuple((Int, Float))
        assert not T.isinstance([1, 1, 1])
        assert not T.isinstance([1, 1.0])
        assert T.isinstance([1, 1])
