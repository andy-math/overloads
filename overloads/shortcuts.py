# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
import math
import os
import pickle
from typing import Any, Optional, Tuple

import numpy


def save(filename: str, object: Any) -> None:
    path, basename = os.path.split(filename)
    if path != "":
        os.makedirs(path, exist_ok=True)
    with open(filename, "wb") as f:
        pickle.dump(object, f)


def load(filename: str) -> Any:
    with open(filename, "rb") as f:
        return pickle.load(f)


def timestamp(
    *, time: Optional[datetime.datetime] = None, format: str = "%Y_%m_%d %H.%M.%S"
) -> str:
    if time is None:
        time = datetime.datetime.now()
    fmt_cvrt = format.encode("unicode_escape").decode("ascii")
    timestr = time.strftime(fmt_cvrt)
    timestr = timestr.encode("ascii").decode("unicode_escape")
    return timestr


def assertNoNaN(x: numpy.ndarray) -> None:
    idx: Tuple[numpy.ndarray, ...]
    xx = x.reshape((1,)) if x.shape == () else x
    idx = numpy.where(numpy.isnan(xx))
    count = idx[0].shape[0]
    assert count == 0, ("出现了NaN", xx[idx], idx)


def assertNoInfNaN(x: numpy.ndarray) -> None:
    idx: Tuple[numpy.ndarray, ...]
    xx = x.reshape((1,)) if x.shape == () else x
    idx = numpy.where(numpy.logical_not(numpy.isfinite(xx)))
    count = idx[0].shape[0]
    assert count == 0, ("出现了Inf或NaN", xx[idx], idx)


def assertNoInfNaN_float(x: float) -> None:
    assert math.isfinite(x), ("出现了Inf或NaN", x)
