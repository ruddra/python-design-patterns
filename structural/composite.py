class Component:
    """Abstract Class"""

    def run_function(self):
        pass


class Child(Component):
    def __init__(self, *args, **kwargs):
        self.name = args[0]

    def run_function(self):
        print("Child {}".format(self.name))


class Composite(Component):
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.children = []

    def add_children(self, child):
        self.children.append(child)

    def remove_children(self, child):
        self.children.remove(child)

    def run_function(self):
        print("Component {}".format(self.name))
        for i in self.children:
            i.run_function()


menu = Composite('menu')
sub1 = Composite('sub1')
sub2 = Composite('sub2')
child1 = Child('c1')
child2 = Child('c2')
child3 = Child('c3')
child4 = Child('c4')
sub1.add_children(child1)
sub1.add_children(child2)
sub2.add_children(child3)
sub2.add_children(child4)

menu.add_children(sub1)
menu.add_children(sub2)

menu.run_function()
