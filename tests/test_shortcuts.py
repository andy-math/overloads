from overloads import shortcuts


# save_load 支持树状路径
class Test_save_load_check():
    def test_普通SL(self) -> None:
        a = [{()}]
        filename = 'a.pkl'
        shortcuts.save(filename, a)
        assert shortcuts.load(filename) == a

    def test_新建不存在的路径(self) -> None:
        a = [{()}]
        filename = 'a/a/a/a/a.pkl'
        shortcuts.save(filename, a)
        assert shortcuts.load(filename) == a

    def test_覆盖重复的路径(self) -> None:
        a = [{()}]
        filename = 'a/a/a/a/a.pkl'
        shortcuts.save(filename, a)
        assert shortcuts.load(filename) == a


# 时间戳
class Test_时间戳检查():
    def test_时间戳行为预期(self) -> None:
        import datetime
        ss = shortcuts.timestamp()
        assert isinstance(datetime.datetime.strptime(ss, '%Y_%m_%d %H.%M.%S'), datetime.datetime)

    def test_时间戳时间准确性(self) -> None:
        import datetime
        now = datetime.datetime.now()
        ss = shortcuts.timestamp(time=now)
        assert shortcuts.timestamp(time=datetime.datetime.strptime(ss, '%Y_%m_%d %H.%M.%S')) == ss

    def test_时间戳自定义格式(self) -> None:
        import datetime
        fmt = '%Y.%m.%d %H_%M_%S'
        now = datetime.datetime.now()
        ss = shortcuts.timestamp(time=now, format=fmt)
        assert shortcuts.timestamp(time=datetime.datetime.strptime(ss, fmt), format=fmt) == ss


# assertInfNaN
