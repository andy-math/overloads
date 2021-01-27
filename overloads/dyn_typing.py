# -*- coding: utf-8 -*-
from __future__ import annotations

import abc as _abc
from functools import wraps as _wraps
from typing import Any as _Any
from typing import Callable as _Callable
from typing import Dict as _Dict
from typing import Optional as _Optional
from typing import Set as _Set
from typing import Tuple as _Tuple
from typing import Type as _Type
from typing import TypeVar as _TypeVar
from typing import Union as _Union

import numpy as _numpy


def _get_value(value: _Union[int, float, DepSize]) -> _Union[int, float]:
    if isinstance(value, (int, float)):
        return value
    elif isinstance(value, SizeConst):
        return value.value
    elif isinstance(value, SizeVar):
        assert value.value is not None
        return value.value
    else:
        assert isinstance(value, SizeExpr)
        assert value.expr is not None
        return value.expr()


def _make_using(*values: _Union[int, float, DepSize, DepType]) -> _Set[SizeVar]:
    using: _Set[SizeVar] = set()
    for value in values:
        if isinstance(value, SizeVar):
            using.add(value)
        elif isinstance(value, (SizeExpr, DepType)):
            using.update(value.using)
    return using


class _DepSize(metaclass=_abc.ABCMeta):
    @_abc.abstractmethod
    def eqn(self, value: int) -> bool:
        pass  # pragma: no cover


class DepSize(_DepSize, metaclass=_abc.ABCMeta):  # 算术运算支持
    def __neg__(self) -> SizeExpr:
        def neg() -> _Union[int, float]:
            return -_get_value(self)

        return SizeExpr(_make_using(self), neg)

    def __add__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def add() -> _Union[int, float]:
            return _get_value(self) + _get_value(value)

        return SizeExpr(_make_using(self, value), add)

    def __sub__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def sub() -> _Union[int, float]:
            return _get_value(self) - _get_value(value)

        return SizeExpr(_make_using(self, value), sub)

    def __mul__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def mul() -> _Union[int, float]:
            return _get_value(self) * _get_value(value)

        return SizeExpr(_make_using(self, value), mul)

    def __floordiv__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def floordiv() -> _Union[int, float]:
            return _get_value(self) // _get_value(value)

        return SizeExpr(_make_using(self, value), floordiv)

    def __truediv__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def truediv() -> _Union[int, float]:
            return _get_value(self) / _get_value(value)

        return SizeExpr(_make_using(self, value), truediv)

    def __mod__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def mod() -> _Union[int, float]:
            return _get_value(self) % _get_value(value)

        return SizeExpr(_make_using(self, value), mod)

    def __pow__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def pow() -> _Union[int, float]:
            return _get_value(self)**_get_value(value)

        return SizeExpr(_make_using(self, value), pow)

    def __radd__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def radd() -> _Union[int, float]:
            return _get_value(value) + _get_value(self)

        return SizeExpr(_make_using(self, value), radd)

    def __rsub__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rsub() -> _Union[int, float]:
            return _get_value(value) - _get_value(self)

        return SizeExpr(_make_using(self, value), rsub)

    def __rmul__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rmul() -> _Union[int, float]:
            return _get_value(value) * _get_value(self)

        return SizeExpr(_make_using(self, value), rmul)

    def __rfloordiv__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rfloordiv() -> _Union[int, float]:
            return _get_value(value) // _get_value(self)

        return SizeExpr(_make_using(self, value), rfloordiv)

    def __rtruediv__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rtruediv() -> _Union[int, float]:
            return _get_value(value) / _get_value(self)

        return SizeExpr(_make_using(self, value), rtruediv)

    def __rmod__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rmod() -> _Union[int, float]:
            return _get_value(value) % _get_value(self)

        return SizeExpr(_make_using(self, value), rmod)

    def __rpow__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rpow() -> _Union[int, float]:
            return _get_value(value)**_get_value(self)

        return SizeExpr(_make_using(self, value), rpow)


class SizeExpr(DepSize):
    using: _Set[SizeVar]
    expr: _Optional[_Callable[[], _Union[int, float]]]

    def __init__(
            self,
            using: _Set[SizeVar],  # force line wrap
            expr: _Callable[[], _Union[int, float]]) -> None:
        self.using = using
        self.expr = expr

    def eqn(self, value: int) -> bool:
        assert self.expr is not None
        return self.expr() == value

    def check_using(self) -> None:
        for s in self.using:
            assert s.value is not None


class SizeVar(DepSize):
    value: _Optional[int] = None

    def eqn(self, value: int) -> bool:
        if self.value is None:
            self.value = value
        return self.value == value


class SizeConst(DepSize):
    value: int

    def __init__(self, value: int) -> None:
        self.value = value

    def eqn(self, value: int) -> bool:
        return self.value == value


class DepType(metaclass=_abc.ABCMeta):
    using: _Set[SizeVar]

    @_abc.abstractmethod
    def _isinstance(self, value: _Any) -> bool:
        pass  # pragma: no cover

    def isinstance(self, value: _Any) -> bool:
        result = self._isinstance(value)
        for s in self.using:
            s.value = None
        return result


class NDArray(DepType):
    dtype: _Type[_Any]
    shape: _Tuple[DepSize, ...]
    isfortran: bool

    def __init__(self,
                 dtype: _Type[_Any],
                 shape: _Tuple[DepSize, ...],
                 isfortran: bool = False) -> None:
        self.using = _make_using(*shape)
        self.dtype = dtype
        self.shape = shape
        self.isfortran = isfortran

    def _isinstance(self, value: _Any) -> bool:
        if not isinstance(value, _numpy.ndarray):
            return False
        if _numpy.isfortran(value) != self.isfortran:
            return False
        if value.dtype.type != self.dtype:
            return False
        if len(value.shape) != len(self.shape):
            return False
        for a, b in zip(value.shape, self.shape):
            if isinstance(b, SizeExpr):
                b.check_using()
            if not b.eqn(a):
                return False
        return True


class Optional(DepType):
    dtype: DepType

    def __init__(self, dtype: DepType) -> None:
        self.using = _make_using(dtype)
        self.dtype = dtype

    def _isinstance(self, value: _Any) -> bool:
        if value is None:
            return True
        return self.dtype._isinstance(value)


class Union(DepType):
    dtype: _Tuple[DepType, ...]

    def __init__(self, *dtype: DepType) -> None:
        self.using = _make_using(*dtype)
        self.dtype = dtype

    def _isinstance(self, value: _Any) -> bool:
        for t in self.dtype:
            if t._isinstance(value):
                return True
        return False


class List(DepType):
    dtype: DepType
    len: DepSize

    def __init__(self, dtype: DepType, len: DepSize) -> None:
        self.using = _make_using(dtype, len)
        self.dtype = dtype
        self.len = len

    def _isinstance(self, value: _Any) -> bool:
        if not isinstance(value, list):
            return False
        if isinstance(self.len, SizeExpr):
            self.len.check_using()
        if not self.len.eqn(len(value)):
            return False
        for v in value:
            if not self.dtype._isinstance(v):
                return False
        return True


class Tuple(DepType):
    dtype: _Tuple[DepType, ...]

    def __init__(self, dtype: _Tuple[DepType, ...]) -> None:
        self.using = _make_using(*dtype)
        self.dtype = dtype

    def _isinstance(self, value: _Any) -> bool:
        if not isinstance(value, tuple):
            return False
        if len(value) != len(self.dtype):
            return False
        for v, t in zip(value, self.dtype):
            if not t._isinstance(v):
                return False
        return True


class Dict(DepType):
    dtype: _Dict[_Any, DepType]

    def __init__(self, dtype: _Dict[_Any, DepType]) -> None:
        self.using = _make_using(*dtype.values())
        self.dtype = dtype

    def _isinstance(self, value: _Any) -> bool:
        if not isinstance(value, dict):
            return False
        if value.keys() != self.dtype.keys():
            return False
        for k in self.dtype.keys():
            if not self.dtype[k]._isinstance(value[k]):
                return False
        return True


class Class(DepType):
    dtype: _Type[_Any]

    def __init__(self, dtype: _Type[_Any]) -> None:
        self.using = set()
        self.dtype = dtype

    def _isinstance(self, value: _Any) -> bool:
        return isinstance(value, self.dtype)


class Bool(DepType):
    def __init__(self) -> None:
        self.using = set()

    def _isinstance(self, value: _Any) -> bool:
        return isinstance(value, bool)


class Int(DepType):
    def __init__(self) -> None:
        self.using = set()

    def _isinstance(self, value: _Any) -> bool:
        return isinstance(value, int)


class Float(DepType):
    def __init__(self) -> None:
        self.using = set()

    def _isinstance(self, value: _Any) -> bool:
        return isinstance(value, float)


_T1 = _TypeVar('_T1')
_T2 = _TypeVar('_T2')
_T3 = _TypeVar('_T3')
_T4 = _TypeVar('_T4')
_T5 = _TypeVar('_T5')
_T6 = _TypeVar('_T6')
_T7 = _TypeVar('_T7')
_T8 = _TypeVar('_T8')
_T9 = _TypeVar('_T9')
return_t = _TypeVar('return_t')


def _dyn_check_unsafe(
        *, input: _Tuple[DepType, ...],
        output: DepType) -> _Callable[[_Callable[..., return_t]], _Callable[..., return_t]]:
    using = _make_using(*input, output)

    def decorator(f: _Callable[..., return_t]) -> _Callable[..., return_t]:
        @_wraps(f)
        def wrapper(*args: _Any) -> return_t:
            try:
                assert len(args) == len(input)
                for arg, t in zip(args, input):
                    assert t._isinstance(arg)
                value = f(*args)
                assert output._isinstance(value)
                return value
            finally:
                for s in using:
                    s.value = None

        return wrapper

    return decorator


def dyn_check_0(
    *,
    input: _Tuple[()],
    output: DepType  # force line wrap
) -> _Callable[[_Callable[[], return_t]], _Callable[[], return_t]]:
    return _dyn_check_unsafe(input=input, output=output)


def dyn_check_1(
    *,
    input: _Tuple[DepType],
    output: DepType  # force line wrap
) -> _Callable[[_Callable[[_T1], return_t]], _Callable[[_T1], return_t]]:
    return _dyn_check_unsafe(input=input, output=output)


def dyn_check_2(
    *,
    input: _Tuple[DepType, DepType],
    output: DepType  # force line wrap
) -> _Callable[[_Callable[[_T1, _T2], return_t]], _Callable[[_T1, _T2], return_t]]:
    return _dyn_check_unsafe(input=input, output=output)


def dyn_check_3(
    *,
    input: _Tuple[DepType, DepType, DepType],
    output: DepType  # force line wrap
) -> _Callable[[_Callable[[_T1, _T2, _T3], return_t]], _Callable[[_T1, _T2, _T3], return_t]]:
    return _dyn_check_unsafe(input=input, output=output)


def dyn_check_4(
    *,
    input: _Tuple[DepType, DepType, DepType, DepType],
    output: DepType  # force line wrap
) -> _Callable[[_Callable[[_T1, _T2, _T3, _T4], return_t]], _Callable[[_T1, _T2, _T3, _T4],
                                                                      return_t]]:
    return _dyn_check_unsafe(input=input, output=output)


def dyn_check_5(
    *,
    input: _Tuple[DepType, DepType, DepType, DepType, DepType],
    output: DepType  # force line wrap
) -> _Callable[[_Callable[[_T1, _T2, _T3, _T4, _T5], return_t]],  # force line wrap
               _Callable[[_T1, _T2, _T3, _T4, _T5], return_t]]:
    return _dyn_check_unsafe(input=input, output=output)


def dyn_check_6(
    *,
    input: _Tuple[DepType, DepType, DepType, DepType, DepType, DepType],
    output: DepType  # force line wrap
) -> _Callable[[_Callable[[_T1, _T2, _T3, _T4, _T5, _T6], return_t]],  # force line wrap
               _Callable[[_T1, _T2, _T3, _T4, _T5, _T6], return_t]]:
    return _dyn_check_unsafe(input=input, output=output)


def dyn_check_7(
    *,
    input: _Tuple[DepType, DepType, DepType, DepType, DepType, DepType, DepType],
    output: DepType  # force line wrap
) -> _Callable[[_Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7], return_t]],  # force line wrap
               _Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7], return_t]]:
    return _dyn_check_unsafe(input=input, output=output)


def dyn_check_8(
    *,
    input: _Tuple[DepType, DepType, DepType, DepType, DepType, DepType, DepType, DepType],
    output: DepType  # force line wrap
) -> _Callable[[_Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8], return_t]],  # force line wrap
               _Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8], return_t]]:
    return _dyn_check_unsafe(input=input, output=output)


def dyn_check_9(
    *,
    input: _Tuple[DepType, DepType, DepType, DepType, DepType, DepType, DepType, DepType, DepType],
    output: DepType  # force line wrap
) -> _Callable[[_Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9],
                          return_t]],  # force line wrap
               _Callable[[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9], return_t]]:
    return _dyn_check_unsafe(input=input, output=output)
