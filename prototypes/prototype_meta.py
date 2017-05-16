"""

Prototype using meta-classes

"""

import copy

class MetaPrototype(type):
    """ A metaclass for Prototypes """

    def __init__(cls, *args):
        type.__init__(cls, *args)
        cls.clone = lambda self: copy.deepcopy(self)            

class Prototype(metaclass=MetaPrototype):
    """ Top-level prototype class using MetaPrototype """
    pass

class MyClass(Prototype):

    def __init__(self, x=100, y=200):
        self.x = x
        self.y = y
        self.items = [self.x, self.y]


