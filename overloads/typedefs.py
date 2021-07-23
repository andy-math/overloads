from typing import TYPE_CHECKING, Tuple

import numpy

if TYPE_CHECKING:
    ndarray = numpy.ndarray[
        Tuple[int, ...], numpy.dtype[numpy.float64]
    ]  # pragma: no cover
else:
    ndarray = numpy.ndarray
