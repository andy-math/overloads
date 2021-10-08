from typing import TYPE_CHECKING

import numpy

if TYPE_CHECKING:
    ndarray = numpy.ndarray  # pragma: no cover
else:
    ndarray = numpy.ndarray
