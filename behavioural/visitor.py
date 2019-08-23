class House:
    def accept(self, visitor):
        visitor.visited(self)

    def has_hvac_visited(self, hvac_specialist):
        print(self, hvac_specialist, "visited")

    def has_electrician_visited(self, electrician):
        print(self, electrician, "visited")

    def __str__(self):
        return self.__class__.__name__


class HVAC:
    def visited(self, house):
        return house.has_hvac_visited(self)

    def __str__(self):
        return self.__class__.__name__


class Electrician:
    def visited(self, house):
        return house.has_electrician_visited(self)

    def __str__(self):
        return self.__class__.__name__


hvac = HVAC()
electrician = Electrician()

house = House()
house.accept(hvac)
house.accept(electrician)
