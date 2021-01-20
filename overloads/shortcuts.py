# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
import math
import pickle
from typing import Any, Optional, Tuple, Union

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


def assertNoInfNaN(x: Union[int, float, numpy.ndarray[numpy.float64]]) -> None:
    idx: Tuple[numpy.ndarray[numpy.int64], ...]
    if isinstance(x, float):
        assert math.isfinite(x), ('出现了Inf或NaN', x)
    elif isinstance(x, numpy.ndarray):
        xx = x.reshape((1, ) if x.shape == () else x.shape)
        idx = numpy.where(numpy.isfinite(xx))  # type: ignore
        count = idx[0].shape[0]
        assert count == 0, ('出现了Inf或NaN', xx[idx], idx)


if __name__ == '__main__':
    isfinite = numpy.isfinite  # type: ignore
    assert not bool(isfinite(numpy.array([numpy.inf])))
    assert not bool(isfinite(numpy.array([numpy.nan])))
    assert not bool(isfinite(numpy.array([-numpy.inf])))
    assert numpy.isnan(numpy.sqrt(numpy.array([-1])))
    ee = None
    try:
        int(math.nan)
    except BaseException as e:
        ee = e
    assert ee is not None
    ee = None
    try:
        int(math.inf)
    except BaseException as e:
        ee = e
    assert ee is not None
    ee = None
    try:
        int(-math.inf)
    except BaseException as e:
        ee = e
    assert ee is not None
