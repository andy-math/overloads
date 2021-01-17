# -*- coding: utf-8 -*-

import copy
from typing import (Any, Callable, Dict, Generic, List, Optional, Sequence, Tuple, Type, TypeVar,
                    Union)

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
        self.f = copy.deepcopy(f)
        self.args = copy.deepcopy(args)
        self.kwargs = copy.deepcopy(kwargs)
        self.exception = copy.deepcopy(exception)

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


def starmap(
    f: Callable[..., T],
    args: Sequence[Tuple[Any, ...]],
    _exceptions_to_be_captured: ExceptionToBeCaptured_t = BaseException
) -> List[Union[T, Captured_Exception[T]]]:
    result_list: List[Union[T, Captured_Exception[T]]] = []
    for idx, arg in enumerate(args):
        result = capture_exceptions(f, *arg, _exceptions_to_be_captured=_exceptions_to_be_captured)
        if isinstance(result, Captured_Exception):
            print("[{}]: {}".format(idx, result))
        result_list.append(result)
    return result_list


if __name__ == '__main__':

    Numeric = TypeVar('Numeric', int, float)

    def square(x: Numeric) -> Numeric:
        return x * x

    e = starmap(square, [(1, ), (0, ), (2, ), ([], ), ((), )],
                _exceptions_to_be_captured=Exception)
    print(e)
