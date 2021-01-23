# -*- coding: utf-8 -*-
import multiprocessing
import random
import time
from typing import Optional, Tuple, Union

from overloads import parallels
from overloads.capture_exceptions import Captured_Exception

random.seed(5489)


class E(Exception):
    def __init__(self, *args: str):
        self.args = args


def f(a: int) -> Tuple[int, Optional[int]]:
    time.sleep(random.random())
    return a, multiprocessing.current_process().ident


def g(a: int) -> None:
    if a == 1:
        raise E('aaa')


def h(a: int) -> int:
    time.sleep(random.random())
    return a


ident_set = set()


def callback(
    result: Union[Tuple[int, Optional[int]],  #
                  Captured_Exception[Tuple[int, Optional[int]]]]
) -> None:
    assert not isinstance(result, Captured_Exception)
    _, ident = result
    assert ident is not None
    ident_set.add(ident)
    assert ident != multiprocessing.current_process().ident


class TestCase():
    def test_顺序性(self) -> None:
        res = parallels.parfor(f, range(10), callback=callback)
        for i in range(10):
            r = res[i]
            assert not isinstance(r, Captured_Exception)
            a, _ = r
            assert a == i
        assert len(ident_set) > 1

    def test_parprint(self) -> None:
        parallels.parprint('aaabbb能用就行', sep='sep', end='end')

    def test_异常(self) -> None:
        ce = parallels.parfor(g, [1])[0]
        assert isinstance(ce, Captured_Exception)
        assert isinstance(ce.exception, E)
        assert ce.exception.args[0] == 'aaa'
