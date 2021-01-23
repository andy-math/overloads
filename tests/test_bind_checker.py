# -*- coding: utf-8 -*-
import math

import numpy
from overloads import bind_checker
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
