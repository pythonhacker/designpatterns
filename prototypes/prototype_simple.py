"""

Simple prototype pattern by using the copy module

"""

import copy

class Prototype(object):
    """ Base class for Prototype pattern """

    def clone(self):
        """ Return a clone of self """
        
        return copy.deepcopy(self)

class SPrototype(object):
    """ Base class for Prototype pattern using shallow copy """

    def clone(self):
        """ Return a shallow clone of self """

        return copy.copy(self)

class MyClass(Prototype):

    def __init__(self, x=100, y=200):
        self.x = x
        self.y = y
        self.items = [self.x, self.y]
        

class MySClass(SPrototype):

    def __init__(self, x=100, y=200):
        self.x = x
        self.y = y
        self.items = [self.x, self.y]



        
        
