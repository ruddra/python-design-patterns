class Berg:
    _inner_object = dict()

    def __init__(self):
        self.__dict__ = self._inner_object


class Singleton(Berg):
    def __init__(self, **kwarg):
        super().__init__()
        self._inner_object.update(kwarg)

    def __str__(self):
        return str(self._inner_object)


singleton1 = Singleton(hello='world')
print(singleton1)
singleton2 = Singleton(foo='bar')
print(singleton2)
