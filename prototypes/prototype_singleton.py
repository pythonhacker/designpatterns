"""
Classes which can behave as both singleton & prototype using metaclasses
"""

import copy

class MetaSingletonPrototype(type):
    """ A metaclass for Singleton & Prototype patterns """
    
    def __init__(cls, *args):
        print(cls,"__init__ method called with args", args)
        type.__init__(cls, *args)
        cls.instance = None
        cls.clone = lambda self: copy.deepcopy(cls.instance)

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls,"creating prototypical instance", args, kwargs)
            cls.instance = type.__call__(cls,*args, **kwargs)
        return cls.instance

class PrototypeS(metaclass=MetaSingletonPrototype):
    """ Top-level class using MetaSingletonPrototype """
    pass

class MyClass(PrototypeS):

    def __init__(self, x=100, y=200):
        self.x = x
        self.y = y
        self.items = [self.x, self.y]

