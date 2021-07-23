# -*- coding: utf-8 -*-
import pickle

from overloads import capture_exceptions


class E(Exception):
    def __init__(self, *args: str):
        self.args = args


def f(a: int) -> int:
    if a == 1:
        raise E("将返回自身")
    return a * a


class Test:
    def test_异常情形(self) -> None:
        ce = capture_exceptions.capture_exceptions(f, 1)
        assert isinstance(ce, capture_exceptions.Captured_Exception)
        assert isinstance(ce.exception, E)
        assert ce.exception.args[0] == "将返回自身"

    def test_正常情形(self) -> None:
        ce = capture_exceptions.capture_exceptions(f, 2)
        assert ce == 4

    def test_过滤Without(self) -> None:
        ce = None
        try:
            capture_exceptions.capture_exceptions(f, 1, without=E)
        except E as e:
            ce = e
        assert isinstance(ce, E)
        assert ce.args[0] == "将返回自身"

    def test_str函数暂时能用就行(self) -> None:
        ce = capture_exceptions.capture_exceptions(f, 1)
        assert isinstance(ce, capture_exceptions.Captured_Exception)
        assert isinstance(ce.exception, E)
        assert str(ce) == "{}".format(ce)
        print(ce)

    def test_重放(self) -> None:
        ce = capture_exceptions.capture_exceptions(f, 1)
        assert isinstance(ce, capture_exceptions.Captured_Exception)
        assert isinstance(ce.exception, E)
        ee = None
        try:
            ce()
        except BaseException as eee:
            ee = eee
        assert isinstance(ee, E)
        assert ee.args == ce.exception.args

    def test_map(self) -> None:
        ce_list = capture_exceptions.map(f, [1, 2])
        assert isinstance(ce_list[0], capture_exceptions.Captured_Exception)
        assert isinstance(ce_list[0].exception, E)
        assert ce_list[0].exception.args[0] == "将返回自身"
        assert ce_list[1] == 4

    def test_picklable(self) -> None:
        """
        包装器伪装为原f，pickle后从真正的原函数进行load，
        而原函数没有包装，因此发生了unwrap，调用f(1)触发异常
        """
        assert isinstance(
            capture_exceptions.capture_exceptions(
                lambda _: pickle.loads(
                    pickle.dumps(capture_exceptions.capture_exceptions()(f))
                )(1),
                (),
            ),
            capture_exceptions.Captured_Exception,
        )
        """
        没有包装伪装，则可以捕获save/load后的异常
        """
        ff = pickle.loads(pickle.dumps(capture_exceptions.capture_exceptions(f)))
        assert isinstance(ff(1), capture_exceptions.Captured_Exception)


if __name__ == "__main__":
    t = Test()
    t.test_异常情形()
    t.test_map()
    t.test_str函数暂时能用就行()
    t.test_正常情形()
    t.test_过滤Without()
    t.test_重放()
    t.test_picklable()
