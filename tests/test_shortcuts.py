from overloads import shortcuts


# save_load 支持树状路径
class save_load_check():
    def 普通SL(self) -> None:
        a = [{()}]
        filename = 'a.pkl'
        shortcuts.save(filename, a)
        assert shortcuts.load(filename) == a

    def 新建不存在的路径(self) -> None:
        a = [{()}]
        filename = 'a/a/a/a/a.pkl'
        shortcuts.save(filename, a)
        assert shortcuts.load(filename) == a

    def 覆盖重复的路径(self) -> None:
        a = [{()}]
        filename = 'a/a/a/a/a.pkl'
        shortcuts.save(filename, a)
        assert shortcuts.load(filename) == a


# 时间戳
class 时间戳检查():
    def 时间戳行为预期(self) -> None:
        import datetime
        ss = shortcuts.timestamp()
        assert isinstance(datetime.datetime.strptime(ss, '%Y_%m_%d %H.%M.%S'), datetime.datetime)

    def 时间戳时间准确性(self) -> None:
        import datetime
        now = datetime.datetime.now()
        ss = shortcuts.timestamp(time=now)
        assert datetime.datetime.strptime(ss, '%Y_%m_%d %H.%M.%S') == now

    def 时间戳自定义格式(self) -> None:
        import datetime
        fmt = '%Y.%m.%d %H_%M_%S'
        now = datetime.datetime.now()
        ss = shortcuts.timestamp(time=now, format=fmt)
        assert datetime.datetime.strptime(ss, fmt) == now


# assertInfNaN
