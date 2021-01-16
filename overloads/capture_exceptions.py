# -*- coding: utf-8 -*-

from typing import (Any, Callable, Dict, Generic, Optional, Tuple, Type, TypeVar, Union)

import pretty_errors  # type: ignore # noqa: F401

T = TypeVar('T')

BaseException_t = Type[BaseException]
ExceptionToBeCaptured_t = Union[BaseException_t, Tuple[BaseException_t]]


class Captured_Exception(Generic[T]):
    f: Optional[Callable[..., T]]
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    exception: BaseException

    def __init__(self, f: Callable[..., T], args: Tuple[Any, ...], kwargs: Dict[str, Any],
                 exception: BaseException):
        self.f = f
        self.args = args
        self.kwargs = kwargs
        self.exception = exception

    def __call__(self) -> T:
        assert self.f is not None
        return self.f(*self.args, **self.kwargs)

    def __str__(self) -> str:
        assert self.f is not None
        fmtstr = ''.join([
            '{T}(f={f}, len(args)={nargs}, len(kwargs)={nkwargs}, e={e})'.format(
                T=Captured_Exception.__name__,
                f='{}.{}'.format(self.f.__module__, self.f.__name__),
                nargs=len(self.args),
                nkwargs=len(self.kwargs),
                e=type(self.exception).__name__),
            ' with the following exception:\n    {}'.format(object.__str__(self.exception))
        ])
        return fmtstr


def capture_exceptions(f: Callable[..., T],
                       *args: Any,
                       _exceptions_to_be_captured: ExceptionToBeCaptured_t = BaseException,
                       **kwargs: Any) -> Union[T, Captured_Exception[T]]:
    try:
        return f(*args, **kwargs)
    except _exceptions_to_be_captured as e:
        return Captured_Exception(f, args, kwargs, e)


Numeric = TypeVar('Numeric', int, float)

if __name__ == '__main__':

    def square(x: Numeric) -> Numeric:
        return x * x

    e = capture_exceptions(square, [], _types_of_exceptions_to_capture=Exception)
    assert isinstance(e, Captured_Exception)
    print(e)
    print(capture_exceptions(square, 1))
