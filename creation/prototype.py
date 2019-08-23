import copy


class Product:
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.foo = None
        self.hello = None

    def __str__(self):
        return '{}|{}|{}'.format(self.name, self.foo, self.hello)


class Prototype:
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.prototypes = dict()

    def register(self, name, obj):
        self.prototypes[name] = obj

    def unregister(self, name):
        del self.prototypes[name]

    def make_copy(self, name, **kwargs):
        obj = copy.deepcopy(self.prototypes.get(name))
        obj.__dict__.update(kwargs)
        return obj


product_one = Product('product one')
product_two = Product('product two')
product_three = Product('product three')

p = Prototype('p1')
p.register('one', product_one)
p.register('two', product_two)
p.register('three', product_three)

protype_object = p.make_copy('one', hello='world', foo='bar')
protype_object2 = p.make_copy('two', hello='world1', foo='bar1')
print(protype_object)
print(protype_object2)
