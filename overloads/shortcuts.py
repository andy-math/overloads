# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
import pickle
from typing import Any, Optional, Union

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
    assert numpy.isfinite(x.flatten()).all()  # type: ignore
