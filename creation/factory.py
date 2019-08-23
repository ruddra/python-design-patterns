class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


class PetShop:

    def __init__(self):
        self._pets = dict(dog=Dog(), cat=Cat())

    def get_pet(self, name):
        return self._pets.get(name)


if __name__ == '__main__':
    petshop = PetShop()
    dog = petshop.get_pet('dog')
    print(dog.speak())
