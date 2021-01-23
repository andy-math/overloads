from overloads import capture_exceptions


def f(a: int) -> int:
    assert a != 1, '将返回自身'
    return a * a


class Test():
    def test_异常情形(self) -> None:
        ce = capture_exceptions.capture_exceptions(f, 1)
        assert isinstance(ce, capture_exceptions.Captured_Exception)
        assert ce.exception.args[0] == '将返回自身 '

    def test_正常情形(self) -> None:
        ce = capture_exceptions.capture_exceptions(f, 2)
        assert ce == 4
