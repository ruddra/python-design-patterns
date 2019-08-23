class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


class PetShop:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def get_pet(self):
        return self._pet_factory.get_pet()

    def get_pet_food(self):
        return self._pet_factory.get_food()


if __name__ == '__main__':
    factory = DogFactory()
    petshop = PetShop(factory)
    pet = petshop.get_pet()
    food = petshop.get_food()
    print(pet, food)
