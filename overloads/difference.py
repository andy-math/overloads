# -*- coding: utf-8 -*-
import numpy
from numpy import ndarray

from overloads import bind_checker
from overloads.shortcuts import assertNoInfNaN, assertNoInfNaN_float


@bind_checker.bind_checker_2(
    input=bind_checker.make_checker_2(assertNoInfNaN), output=assertNoInfNaN_float
)
def relative(A: ndarray, B: ndarray) -> float:
    assert A.shape == B.shape
    max = numpy.maximum(numpy.abs(A), numpy.abs(B))
    relerr = numpy.abs(A - B) / max
    relerr[max == 0] = 0
    return float(numpy.max(relerr))


@bind_checker.bind_checker_2(
    input=bind_checker.make_checker_2(assertNoInfNaN), output=assertNoInfNaN_float
)
def absolute(A: ndarray, B: ndarray) -> float:
    assert A.shape == B.shape
    return float(numpy.max(numpy.abs(A - B)))
