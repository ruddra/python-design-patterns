class Subject:
    def __init__(self):
        self._observers = list()

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, notified=None):
        for ob in self._observers:
            if ob != notified:
                ob.update(self)


class Core(Subject):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, tmp):
        self._temp = tmp
        self.notify()


class TempViewer():
    def update(self, sub):
        print(sub.name, sub.temp)


sub1 = Core('core one')
sub2 = Core('core two')

ob1 = TempViewer()
ob2 = TempViewer()

sub1.attach(ob1)
sub2.attach(ob1)
sub2.attach(ob2)
sub1.attach(ob2)

sub1.temp = 100
sub2.temp = 100
