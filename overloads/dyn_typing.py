# -*- coding: utf-8 -*-
from __future__ import annotations

import abc as _abc
from typing import Callable as _Callable
from typing import Dict as _Dict
from typing import Optional as _Optional
from typing import Union
from typing import Union as _Union


def _get_value(value: _Union[int, float, DepSize]) -> Union[int, float]:
    if isinstance(value, (int, float)):
        return value
    else:
        return value.get_value()


def _make_using(
        self: DepSize,  # force line wrap
        value: _Optional[_Union[int, float, DepSize]]) -> _Dict[int, SizeVar]:
    using: _Dict[int, SizeVar] = {}
    if isinstance(self, SizeExpr):
        using.update(self.using)
    elif isinstance(self, SizeVar):
        using[id(self)] = self
    if isinstance(value, SizeExpr):
        using.update(value.using)
    elif isinstance(value, SizeVar):
        using[id(self)] = value
    return using


class _DepSize(metaclass=_abc.ABCMeta):
    def __eq__(self, value: object) -> bool:
        assert isinstance(value, int)
        return self._eq_(value)

    @_abc.abstractmethod
    def _eq_(self, value: int) -> bool:
        pass

    @_abc.abstractmethod
    def check_using(self) -> None:
        pass

    @_abc.abstractmethod
    def get_value(self) -> Union[int, float]:
        pass


class DepSize(_DepSize, metaclass=_abc.ABCMeta):  # 算术运算支持
    def __neg__(self) -> SizeExpr:
        def neg() -> Union[int, float]:
            return -self.get_value()

        return SizeExpr(_make_using(self, None), neg)

    def __add__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def add() -> Union[int, float]:
            return self.get_value() + _get_value(value)

        return SizeExpr(_make_using(self, value), add)

    def __sub__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def sub() -> Union[int, float]:
            return self.get_value() - _get_value(value)

        return SizeExpr(_make_using(self, value), sub)

    def __mul__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def mul() -> Union[int, float]:
            return self.get_value() * _get_value(value)

        return SizeExpr(_make_using(self, value), mul)

    def __floordiv__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def floordiv() -> Union[int, float]:
            return self.get_value() // _get_value(value)

        return SizeExpr(_make_using(self, value), floordiv)

    def __truediv__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def truediv() -> Union[int, float]:
            return self.get_value() / _get_value(value)

        return SizeExpr(_make_using(self, value), truediv)

    def __mod__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def mod() -> Union[int, float]:
            return self.get_value() % _get_value(value)

        return SizeExpr(_make_using(self, value), mod)

    def __pow__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def pow() -> Union[int, float]:
            return self.get_value()**_get_value(value)

        return SizeExpr(_make_using(self, value), pow)

    def __radd__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def radd() -> Union[int, float]:
            return _get_value(value) + self.get_value()

        return SizeExpr(_make_using(self, value), radd)

    def __rsub__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rsub() -> Union[int, float]:
            return _get_value(value) - self.get_value()

        return SizeExpr(_make_using(self, value), rsub)

    def __rmul__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rmul() -> Union[int, float]:
            return _get_value(value) * self.get_value()

        return SizeExpr(_make_using(self, value), rmul)

    def __rfloordiv__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rfloordiv() -> Union[int, float]:
            return _get_value(value) // self.get_value()

        return SizeExpr(_make_using(self, value), rfloordiv)

    def __rtruediv__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rtruediv() -> Union[int, float]:
            return _get_value(value) / self.get_value()

        return SizeExpr(_make_using(self, value), rtruediv)

    def __rmod__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rmod() -> Union[int, float]:
            return _get_value(value) % self.get_value()

        return SizeExpr(_make_using(self, value), rmod)

    def __rpow__(self, value: _Union[int, float, DepSize]) -> SizeExpr:
        def rpow() -> Union[int, float]:
            return _get_value(value)**self.get_value()

        return SizeExpr(_make_using(self, value), rpow)


class SizeExpr(DepSize):
    using: _Dict[int, SizeVar]
    expr: _Optional[_Callable[[], Union[int, float]]]

    def __init__(self, using: _Dict[int, SizeVar], expr: _Callable[[], Union[int, float]]) -> None:
        self.using = using
        self.expr = expr

    def _eq_(self, value: int) -> bool:
        assert self.expr is not None
        return self.expr() == value

    def check_using(self) -> None:
        for s in self.using.values():
            s.check_using()

    def get_value(self) -> Union[int, float]:
        assert self.expr is not None
        return self.expr()


class SizeVar(DepSize):
    value: _Optional[int] = None

    def _eq_(self, value: int) -> bool:
        if self.value is None:
            self.value = value
        return self.value == value

    def check_using(self) -> None:
        assert self.value is None

    def get_value(self) -> int:
        assert self.value is not None
        return self.value


class SizeConst(DepSize):
    value: int

    def __init__(self, value: int) -> None:
        self.value = value

    def _eq_(self, value: int) -> bool:
        return self.value == value

    def check_using(self) -> None:
        pass  # using nothing

    def get_value(self) -> int:
        return self.value


if __name__ == '__main__':
    A = SizeVar()
    assert 5 == A
    assert A == 5
    ee = None
    try:
        assert 2 == A
    except BaseException as e:
        ee = e
    print((2**A).get_value())
    assert ee is not None
    assert 1 == 1.0
