# Overloads
![Test](https://github.com/Andy-math/overloads/workflows/Test/badge.svg)
[![codecov](https://codecov.io/gh/Andy-math/overloads/branch/main/graph/badge.svg?token=QIY4S318S1)](https://codecov.io/gh/Andy-math/overloads)

支持mypy静态类型推断的Python实用API集合

## Usage

* ### bind_checker
    #### 输入输出检查器绑定
    ```python
    import bind_checker as bd_chk
    from shortcuts import assertNoInfNaN

    # `_2`表示输入参数为两个，映射到`input[T1, T2]`
    # varadic (like C++) 受PEP484限制无法实现
    checkInfNaN_2 = bd_chk.make_checker_2(assertNoInfNaN, assertNoInfNaN)


    def checkNone(_: None) -> None:
        pass


    @bd_chk.bind_checker_2(  # `_2`, PEP484
        input=checkInfNaN_2,  # `_2`, PEP484
        output=checkNone
    )
    def f(a: np.ndarray, b: np.ndarray) -> None:
        pass


    f(np.array(1), np.array(2))  # OK
    f(np.array(np.nan), np.array(2))  # AssertionError
    f(np.array(1), np.array(np.nan))  # AssertionError
    ```
* ### capture_exceptions
    #### 异常捕获
    ```python
    import capture_exceptions as ce


    def f(a: int) -> int:
        assert a != 1
        return a


    A = ce.capture_exceptions(f, 0)
    assert A == 0
    B = ce.capture_exceptions(f, 1)  # catch=default(BaseException), without=default(tuple())
    assert type(B) is ce.Captured_Exception
    ```
    #### `map`
    ```python
    >>> import capture_exceptions as ce
    ...
    ... def f(a: int) -> int:
    ...     assert a != 1
    ...     return a
    ...
    ... ce.map(f, range(10))
    ...
    [0, ce.Captured_Exception, 2, 3, 4, 5, 6, 7, 8, 9]
    ```
* ### dyn_typing
    #### 动态类型检查
    ```python
    import dyn_typing as dynT

    N = dynT.SizeVar()
    TypeA = dynT.NDArray(np.float64, (N, N + 1))
    assert TypeA.isinstance(np.zeros((3, 4)))  # N is 3
    assert TypeA.isinstance(np.zeros((7, 8)))  # N is 7
    assert not TypeA.isinstance(np.zeros((7, 7)))  # N is 7, 7+1 != 7
    assert not TypeA.isinstance(np.zeros((7, 8, 9)))  # len(TypeA.shape) != len((7, 8, 9))
    assert not TypeA.isinstance(np.zeros((3, 4), dtype=np.int64))  # dtype != np.float64
    assert not TypeA.isinstance(1.0)  # `1.0` is not np.ndarray
    ```
    #### 函数签名（runtime）
    ```python
    import dyn_typing as dynT

    # 矩阵乘法([M*K] @ [K*N] -> [M*N])
    M = dynT.SizeVar()
    N = dynT.SizeVar()
    K = dynT.SizeVar()


    @dynT.dyn_check_2(  # `_2`表示输入参数为两个，映射到`input[T1, T2]`, varadic (like C++) 受PEP484限制无法实现
        input=(dynT.NDArray(np.float64, (M, K)), dynT.NDArray(np.float64, (K, N))),
        output=dynT.NDArray(np.float64, (M, N))
    )
    def matmul(A: Any, B: Any) -> Any:
        return A @ B


    matmul(np.zeros((1, 4)), np.zeros((4, 1)))  # K is 4, OK
    matmul(np.zeros((7, 5)), np.zeros((5, 3)))  # K is 5, OK
    matmul(np.zeros((7, 5)), np.zeros((6, 3)))  # K不匹配, AssertionError
    matmul(np.zeros((1, 4)), np.zeros((4, 1), dtype=np.int64))  # dtype != np.float64, AssertionError
    matmul(np.zeros((1, 4)), 1)  # `1` is not np.ndarray, AssertionError
    ```
* ### parallels
    #### MATLAB风格多进程`parfor`(based on `multiprocessing`)
    ```python
    >>> from parallels import parfor, parprint
    ...
    ... def f(a: int) -> int:
    ...     parprint(a)
    ...     return a * a
    ...
    ... parfor(f, range(5))  # callback=default(None)
    ...
    1
    0
    4
    2
    3
    [0, 1, 4, 9, 16]
    ```
* ### shortcuts
    #### 杂项
    + `save`/`load`
        ```python
        a = np.zeros((1, 2, 3))
        save('path/not/existing/a.pkl', a)
        b = load('path/not/existing/a.pkl')
        assert a == b
        ```
    + `timestamp`
        ```python
        >>> timestamp()  # time=Optional[now()], format=default('%Y_%m_%d %H.%M.%S')
        '2021_01_01 00.00.00'
        ```
    + `assertNoInfNaN`
        ```python
        >>> assertNoInfNaN(np.array(np.nan))
        AssertionError
        ```

* ### tuplize
    #### 多元函数转化为一元`tuple`函数
    ```python
    # `_2`表示输入参数为两个，映射到`input[T1, T2]`
    # varadic (like C++) 受PEP484限制无法实现
    @tuplize.tuplize_2
    def f(a: int, b: int) -> int:
        return a+b


    f((1, 2))  # call `1 + 2`
    f((1, 2.5))  # mypy type error
    ```
