class Director:
    def __init__(self, builder):
        self._builder = builder

    def build_car(self):
        self.car = self._builder.create_new_car()

    def get_car(self):
        return self.car


class Builder:
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class Ford(Builder):
    def __init__(self):
        super().__init__()

    def create_new_car(self):
        super().create_new_car()
        self.car.name = "Ford"
        self.car.tyre = "Normal"
        self.car.engine = "OK"
        return self.car


class Car:
    def __init__(self):
        self.name = None
        self.tyre = None
        self.engine = None

    def __str__(self):
        return "{}|{}|{}".format(self.name, self.tyre, self.engine)


builder = Ford()

director = Director(builder)

director.build_car()

print(director.get_car())
