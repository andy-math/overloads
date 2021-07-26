# -*- coding: utf-8 -*-

import numpy

from overloads import bind_checker
from overloads.shortcuts import assertNoInfNaN, assertNoInfNaN_float
from overloads.typedefs import ndarray


@bind_checker.bind_checker_2(
    input=bind_checker.make_checker_2(assertNoInfNaN, assertNoInfNaN),
    output=assertNoInfNaN_float,
)
def relative(A: ndarray, B: ndarray) -> float:
    assert A.shape == B.shape
    max = numpy.maximum(numpy.abs(A), numpy.abs(B))
    relerr = numpy.abs(A - B) / max
    relerr[max == 0] = 0
    return float(relerr.max())


@bind_checker.bind_checker_2(
    input=bind_checker.make_checker_2(assertNoInfNaN, assertNoInfNaN),
    output=assertNoInfNaN_float,
)
def absolute(A: ndarray, B: ndarray) -> float:
    assert A.shape == B.shape
    return float(numpy.abs(A - B).max())
