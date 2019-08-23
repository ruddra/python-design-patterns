class DrawAPIOne:
    def draw(self, x, y, radius):
        print("Drawing using API One with {}, {}, {}".format(x, y, radius))


class DrawAPITwo:
    def draw(self, x, y, radius):
        print("Drawing using API Two with {}, {}, {}".format(x, y, radius))


class Circle:
    def __init__(self):
        self._x = None
        self._y = None
        self._r = None

    def draw(self, x, y, radius, drawapi):
        self._x = x
        self._y = y
        self._r = radius
        drawapi.draw(x, y, radius)

    def scale(self, percent):
        self._r *= percent


circle = Circle()
circle.draw(1, 2, 3, DrawAPIOne())
circle.draw(1, 2, 3, DrawAPITwo())
