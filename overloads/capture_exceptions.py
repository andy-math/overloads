# -*- coding: utf-8 -*-

import copy
from typing import (Any, Callable, Dict, Generic, List, Optional, Sequence, Tuple, Type, TypeVar,
                    Union)

import pretty_errors  # type: ignore # noqa: F401

import tuplize

param_t = TypeVar('param_t')
return_t = TypeVar('return_t')

BaseException_t = Type[BaseException]
Exceptions_t = Union[BaseException_t, Tuple[BaseException_t, ...]]


class Captured_Exception(Generic[return_t]):
    f: Optional[Callable[..., return_t]]
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    exception: BaseException

    def __init__(self, f: Callable[..., return_t], args: Tuple[Any, ...], kwargs: Dict[str, Any],
                 exception: BaseException):
        self.f = copy.deepcopy(f)
        self.args = copy.deepcopy(args)
        self.kwargs = copy.deepcopy(kwargs)
        self.exception = copy.deepcopy(exception)

    def __call__(self) -> return_t:
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


def capture_exceptions(
    f: Callable[[param_t], return_t],
    arg: param_t,
    *,
    catch: Exceptions_t = BaseException,
    without: Exceptions_t = ()
) -> Union[return_t, Captured_Exception[return_t]]:
    try:
        return f(arg)
    except catch as e:
        if isinstance(e, without):
            raise e
        return Captured_Exception(f, (arg, ), {}, e)


def map(
    f: Callable[[param_t], return_t],
    args: Sequence[param_t],
    *,
    catch: Exceptions_t = BaseException,
    without: Exceptions_t = ()
) -> List[Union[return_t, Captured_Exception[return_t]]]:
    result_list: List[Union[return_t, Captured_Exception[return_t]]] = []
    for idx, arg in enumerate(args):
        result = capture_exceptions(f, arg, catch=catch, without=without)
        if isinstance(result, Captured_Exception):
            print("[{}]: {}".format(idx, result))
        result_list.append(result)
    return result_list


if __name__ == '__main__':

    Numeric = Union[int, float]

    @tuplize.tuplize_1
    def square(x: Numeric) -> Numeric:
        return x * x

    e = map(square, [(1, ), (0, ), (2, ), (1.0, ), ([], )], catch=Exception)
    print(e)
