# Overloads
![Test](https://github.com/Andy-math/overloads/workflows/Test/badge.svg)
[![codecov](https://codecov.io/gh/Andy-math/overloads/branch/main/graph/badge.svg?token=QIY4S318S1)](https://codecov.io/gh/Andy-math/overloads)

支持mypy静态类型推断的Python实用API集合
> 使用`python -m doctest -v -o ELLIPSIS README.md`可以交互式检查此`README.md`。
## Usage

* ### bind_checker
    #### 输入输出检查器绑定
    ```python
    >>> from overloads import bind_checker as bd_chk
    >>> from overloads.shortcuts import assertNoInfNaN
    >>> import numpy as np

    # `_2`表示输入参数为两个，映射到`input[T1, T2]`
    # varadic (like C++) 受PEP484限制无法实现
    >>> checkInfNaN_2 = bd_chk.make_checker_2(assertNoInfNaN, assertNoInfNaN)

    >>> def checkNone(_: None) -> None:
    ...     pass

    >>> @bd_chk.bind_checker_2(  # `_2`, PEP484
    ...     input=checkInfNaN_2,  # `_2`, PEP484
    ...     output=checkNone
    ... )
    ... def f(a: np.ndarray, b: np.ndarray) -> None:
    ...     pass

    >>> f(np.array(1), np.array(2))  # OK
    >>> f(np.array(np.nan), np.array(2))  # AssertionError
    Traceback (most recent call last):
        ...
    AssertionError: ('出现了Inf或NaN', ...)
    >>> f(np.array(1), np.array(np.nan))  # AssertionError
    Traceback (most recent call last):
        ...
    AssertionError: ('出现了Inf或NaN', ...)
    
    ```

* ### capture_exceptions
    #### 异常捕获
    ```python
    >>> from overloads import capture_exceptions as ce

    >>> def f(a: int) -> int:
    ...     assert a != 1, "input value 1 is invalid"
    ...     return a

    >>> print(ce.capture_exceptions(f, 0))
    0

    >>> print(ce.capture_exceptions(f, 1))  # catch=default(BaseException), without=default(tuple())
    Captured_Exception(f=__main__.f, args=(1,), e=AssertionError) with the following exception:
        input value 1 is invalid
      traceback:
        ...
        
    ```
    #### `map`
    ```python
    >>> from overloads import capture_exceptions as ce
    >>> def f(a: int) -> int:
    ...     assert a != 1, "input value 1 is invalid"
    ...     return a
    ...
    >>> ce.map(f, range(10))
    [1]: Captured_Exception(f=__main__.f, args=(1,), e=AssertionError) with the following exception:
        input value 1 is invalid
      traceback:
        ...
    [0, <...Captured_Exception object at ...>, 2, 3, 4, 5, 6, 7, 8, 9]

    ```

* ### dyn_typing
    #### 动态类型检查
    ```python
    >>> from overloads import dyn_typing as dynT
    >>> import numpy as np

    >>> N = dynT.SizeVar()
    >>> TypeA = dynT.NDArray(np.float64, (N, N + 1))
    >>> assert TypeA.isinstance(np.zeros((3, 4)))  # N is 3
    >>> assert TypeA.isinstance(np.zeros((7, 8)))  # N is 7
    >>> assert not TypeA.isinstance(np.zeros((7, 7)))  # N is 7, 7+1 != 7
    >>> assert not TypeA.isinstance(np.zeros((7, 8, 9)))  # len(TypeA.shape) != len((7, 8, 9))
    >>> assert not TypeA.isinstance(np.zeros((3, 4), dtype=np.int64))  # dtype != np.float64
    >>> assert not TypeA.isinstance(1.0)  # `1.0` is not np.ndarray

    ```
    #### 函数签名（runtime）
    ```python
    >>> from overloads import dyn_typing as dynT
    >>> import numpy as np

    # 矩阵乘法([M*K] @ [K*N] -> [M*N])
    >>> M = dynT.SizeVar()
    >>> N = dynT.SizeVar()
    >>> K = dynT.SizeVar()

    >>> @dynT.dyn_check_2(  # `_2`表示输入参数为两个，映射到`input[T1, T2]`, varadic (like C++) 受PEP484限制无法实现
    ...     input=(dynT.NDArray(np.float64, (M, K)), dynT.NDArray(np.float64, (K, N))),
    ...     output=dynT.NDArray(np.float64, (M, N))
    ... )
    ... def matmul(A: ..., B: ...) -> ...:
    ...     return A @ B

    >>> matmul(np.zeros((1, 4)), np.zeros((4, 1)))  # K is 4, OK
    array([[0.]])

    >>> matmul(np.zeros((7, 5)), np.zeros((5, 3)))  # K is 5, OK
    array([[...]])

    >>> matmul(np.zeros((7, 5)), np.zeros((6, 3)))  # K不匹配, AssertionError
    Traceback (most recent call last):
        ...
    AssertionError

    >>> matmul(np.zeros((1, 4)), np.zeros((4, 1), dtype=np.int64))  # dtype != np.float64, AssertionError
    Traceback (most recent call last):
        ...
    AssertionError

    >>> matmul(np.zeros((1, 4)), 1)  # `1` is not np.ndarray, AssertionError
    Traceback (most recent call last):
        ...
    AssertionError

    ```

* ### parallels
    #### MATLAB风格多进程`parfor`(based on `multiprocessing`)
    ```python
    
    >>> from overloads.parallels import parfor
    >>> def f(a: int) -> int:
    ...     print(a)
    ...     return a * a
    >>> # callback=default(None)
    >>> parfor(f, range(5))  # doctest:+SKIP
    0
    4
    3
    1
    2
    [0, 1, 4, 9, 16]

    ```

* ### shortcuts
    #### 杂项
    + `save`/`load`
        ```python
        >>> from overloads.shortcuts import save, load
        >>> import numpy
        >>> a = numpy.zeros((1, 2, 3))
        >>> save('path/not/existing/a.pkl', a)
        >>> b = load('path/not/existing/a.pkl')
        >>> assert numpy.all(a == b)

        ```

    + `timestamp`
        ```python
        >>> from datetime import datetime
        >>> from overloads.shortcuts import timestamp
        >>> timestamp(time=datetime(2021, 1, 1))  # format=default('%Y_%m_%d %H.%M.%S')
        '2021_01_01 00.00.00'

        ```

    + `assertNoInfNaN`
        ```python
        >>> from overloads.shortcuts import assertNoInfNaN
        >>> import numpy
        >>> assertNoInfNaN(numpy.array(numpy.nan))
        Traceback (most recent call last):
            ...
        AssertionError: ('出现了Inf或NaN', ...)

        ```

    + `isunique`
        ```python
        >>> from overloads.shortcuts import isunique
        >>> import numpy
        >>> isunique([0, 1, 2])
        True
        >>> isunique([0, 1, 2, 2])
        False
        >>> isunique((0, 1, 2)) # tuple
        True
        >>> isunique(numpy.array([0, 1, 2, 2])) # numpy 1d
        False
        >>> isunique(numpy.array([[1, 2], [2, 1]])) # ndarray is invalid
        Traceback (most recent call last):
            ...
        TypeError: unhashable type: 'numpy.ndarray'

        ```

* ### tuplize
    #### 多元函数转化为一元`tuple`函数
    ```python
    # `_2`表示输入参数为两个，映射到`input[T1, T2]`
    # varadic (like C++) 受PEP484限制无法实现
    >>> from overloads import tuplize
    >>> @tuplize.tuplize_2
    ... def f(a: int, b: int) -> int:
    ...     return a+b
    >>> f((1, 2))  # call `1 + 2`
    3
    >>> f((1, 2.5))  # mypy type error
    3.5

    ```
