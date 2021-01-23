# -*- coding: utf-8 -*-
import math
from typing import TYPE_CHECKING

import numpy
from overloads import bind_checker, tuplize
from overloads.capture_exceptions import Captured_Exception, capture_exceptions
from overloads.shortcuts import assertNoInfNaN

checker = (
    bind_checker.make_checker_0(assertNoInfNaN), bind_checker.make_checker_1(assertNoInfNaN),
    bind_checker.make_checker_2(assertNoInfNaN), bind_checker.make_checker_3(assertNoInfNaN),
    bind_checker.make_checker_4(assertNoInfNaN), bind_checker.make_checker_5(assertNoInfNaN),
    bind_checker.make_checker_6(assertNoInfNaN), bind_checker.make_checker_7(assertNoInfNaN),
    bind_checker.make_checker_8(assertNoInfNaN), bind_checker.make_checker_9(assertNoInfNaN))

dataOK = numpy.array([1.0])
dataERR = numpy.array([math.nan])


class TestMaker():
    def test_maker(self) -> None:
        checker[0](())
        checker[1]((dataOK, ))
        checker[2]((dataOK, dataOK))
        checker[3]((dataOK, dataOK, dataOK))
        checker[4]((dataOK, dataOK, dataOK, dataOK))
        checker[5]((dataOK, dataOK, dataOK, dataOK, dataOK))
        checker[6]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        checker[7]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        checker[8]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        checker[9]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        ce_1 = capture_exceptions(checker[1], (dataERR, ))
        ce_2 = capture_exceptions(checker[2], (dataOK, dataERR))
        ce_3 = capture_exceptions(checker[3], (dataOK, dataOK, dataERR))
        ce_4 = capture_exceptions(checker[4], (dataOK, dataOK, dataOK, dataERR))
        ce_5 = capture_exceptions(checker[5], (dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_6 = capture_exceptions(checker[6], (dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_7 = capture_exceptions(checker[7],
                                  (dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_8 = capture_exceptions(
            checker[8], (dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_9 = capture_exceptions(
            checker[9], (dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
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
        cce_2 = capture_exceptions(checker[2], (dataERR, dataOK))
        cce_3 = capture_exceptions(checker[3], (dataERR, dataOK, dataOK))
        cce_4 = capture_exceptions(checker[4], (dataERR, dataOK, dataOK, dataOK))
        cce_5 = capture_exceptions(checker[5], (dataERR, dataOK, dataOK, dataOK, dataOK))
        cce_6 = capture_exceptions(checker[6], (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK))
        cce_7 = capture_exceptions(checker[7],
                                   (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        cce_8 = capture_exceptions(
            checker[8], (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        cce_9 = capture_exceptions(
            checker[9], (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
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


if TYPE_CHECKING:
    NDArray = numpy.ndarray[numpy.float64]
else:
    NDArray = numpy.ndarray


def outcheck(_: None) -> None:
    return


@tuplize.tuplize_0
@bind_checker.bind_checker_0(input=checker[0], output=outcheck)
def f_0() -> None:
    return


@tuplize.tuplize_1
@bind_checker.bind_checker_1(input=checker[1], output=outcheck)
def f_1(a: NDArray) -> None:
    return


@tuplize.tuplize_2
@bind_checker.bind_checker_2(input=checker[2], output=outcheck)
def f_2(a: NDArray, b: NDArray) -> None:
    return


@tuplize.tuplize_3
@bind_checker.bind_checker_3(input=checker[3], output=outcheck)
def f_3(a: NDArray, b: NDArray, c: NDArray) -> None:
    return


@tuplize.tuplize_4
@bind_checker.bind_checker_4(input=checker[4], output=outcheck)
def f_4(a: NDArray, b: NDArray, c: NDArray, d: NDArray) -> None:
    return


@tuplize.tuplize_5
@bind_checker.bind_checker_5(input=checker[5], output=outcheck)
def f_5(a: NDArray, b: NDArray, c: NDArray, d: NDArray, e: NDArray) -> None:
    return


@tuplize.tuplize_6
@bind_checker.bind_checker_6(input=checker[6], output=outcheck)
def f_6(a: NDArray, b: NDArray, c: NDArray, d: NDArray, e: NDArray, f: NDArray) -> None:
    return


@tuplize.tuplize_7
@bind_checker.bind_checker_7(input=checker[7], output=outcheck)
def f_7(a: NDArray, b: NDArray, c: NDArray, d: NDArray, e: NDArray, f: NDArray,
        g: NDArray) -> None:
    return


@tuplize.tuplize_8
@bind_checker.bind_checker_8(input=checker[8], output=outcheck)
def f_8(a: NDArray, b: NDArray, c: NDArray, d: NDArray, e: NDArray, f: NDArray, g: NDArray,
        h: NDArray) -> None:
    return


@tuplize.tuplize_9
@bind_checker.bind_checker_9(input=checker[9], output=outcheck)
def f_9(a: NDArray, b: NDArray, c: NDArray, d: NDArray, e: NDArray, f: NDArray, g: NDArray,
        h: NDArray, i: NDArray) -> None:
    return


checker2 = (f_0, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9)


class TestBinding():
    def test_1(self) -> None:
        checker2[0](())
        checker2[1]((dataOK, ))
        checker2[2]((dataOK, dataOK))
        checker2[3]((dataOK, dataOK, dataOK))
        checker2[4]((dataOK, dataOK, dataOK, dataOK))
        checker2[5]((dataOK, dataOK, dataOK, dataOK, dataOK))
        checker2[6]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        checker2[7]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        checker2[8]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        checker2[9]((dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        ce_1 = capture_exceptions(checker2[1], (dataERR, ))
        ce_2 = capture_exceptions(checker2[2], (dataOK, dataERR))
        ce_3 = capture_exceptions(checker2[3], (dataOK, dataOK, dataERR))
        ce_4 = capture_exceptions(checker2[4], (dataOK, dataOK, dataOK, dataERR))
        ce_5 = capture_exceptions(checker2[5], (dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_6 = capture_exceptions(checker2[6], (dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_7 = capture_exceptions(checker2[7],
                                  (dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_8 = capture_exceptions(
            checker2[8], (dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
        ce_9 = capture_exceptions(
            checker2[9], (dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataERR))
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
        cce_2 = capture_exceptions(checker2[2], (dataERR, dataOK))
        cce_3 = capture_exceptions(checker2[3], (dataERR, dataOK, dataOK))
        cce_4 = capture_exceptions(checker2[4], (dataERR, dataOK, dataOK, dataOK))
        cce_5 = capture_exceptions(checker2[5], (dataERR, dataOK, dataOK, dataOK, dataOK))
        cce_6 = capture_exceptions(checker2[6], (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK))
        cce_7 = capture_exceptions(checker2[7],
                                   (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        cce_8 = capture_exceptions(
            checker2[8], (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
        cce_9 = capture_exceptions(
            checker2[9], (dataERR, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK, dataOK))
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
