import numpy

from overloads import difference


class Test_difference:
    def test(self) -> None:
        assert difference.absolute(numpy.array([1.0]), numpy.array([2.0])) == 1.0
        assert difference.relative(numpy.array([1.0]), numpy.array([2.0])) == 0.5
