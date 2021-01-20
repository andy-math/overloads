# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
import pickle
from typing import Any, Optional

import numpy


def save(filename: str, object: Any) -> None:
    with open(filename, 'wb') as f:
        pickle.dump(object, f)


def load(filename: str) -> Any:
    with open(filename, 'rb') as f:
        pickle.load(f)


def timestamp(*,
              time: Optional[datetime.datetime] = None,
              format: str = '%Y_%m_%d %H.%M.%S') -> str:
    if time is None:
        time = datetime.datetime.now()
    fmt_cvrt = format.encode('unicode_escape').decode('ascii')
    timestr = time.strftime(fmt_cvrt)
    timestr = timestr.encode('ascii').decode('unicode_escape')
    return timestr


def assertNoInfNaN(x: numpy.ndarray[numpy.float64]) -> None:
    idx: numpy.ndarray[numpy.int64] = numpy.argwhere(numpy.isfinite(x))  # type: ignore
    count = idx.shape[0]
    assert count == 0, ('出现了Inf或NaN', idx)


if __name__ == '__main__':
    isfinite = numpy.isfinite  # type: ignore
    assert not bool(isfinite(numpy.array([numpy.inf])))
    assert not bool(isfinite(numpy.array([numpy.nan])))
    assert numpy.isnan(numpy.sqrt(numpy.array([-1])))
