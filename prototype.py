"""

The Prototype Pattern - In its different implentation avatars.

"""

from prototypes import prototype_simple
from prototypes import prototype_meta
from prototypes import prototype_factory
from prototypes import prototype_singleton


class Name(prototype_simple.SPrototype):
    """ A class representing a person's name """
    
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return ' '.join((self.first, self.second))

class Address(prototype_simple.SPrototype):
    """ An address class """

    def __init__(self, building, street, city, zip, country):
        self.building = building
        self.street = street
        self. city = city
        self.zip = zip
        self.country = country

    def __str__(self):
        return ', '.join((map(str, (self.building, self.street, self.city, self.zip, self.country))))


def test_singularity(cls):
    """ Test if the given class is a Singleton """

    instance1 = cls()
    instance2 = cls()

    return instance1 == instance2

def test_deep_prototype(klass, attr, val):
    """ Test deep prototypes using an attribute (which is
    assumed to be a list) """

    # Make an instance
    instance = klass()
    attr_val = getattr(instance, attr)
    # make a clone
    klone = instance.clone()
    # Assert this is a different instance
    assert(klone != instance)
    print('Verified',klone,'is different from original instance',instance)
    
    # Modify value
    attr_val[0] = val
    # Check that value is *not* modified in clone
    cattr_val = getattr(klone, attr)
    assert(cattr_val[0] != val)
    print('Verified instance value',val,'not modified in clone for attribute',attr) 

def test_shallow_prototype(klass, attr, val):
    """ Test shallow prototypes using an attribute (which is
    assumed to be a list) """

    # Make an instance
    instance = klass()
    attr_val = getattr(instance, attr)
    # make a clone
    klone = instance.clone()
    assert(klone != instance)
    print('Verified',klone,'is different from original instance',instance)
    
    # Modify value
    attr_val[0] = val
    # Check that value is modified in clone
    cattr_val = getattr(klone, attr)
    assert(cattr_val[0] == val)
    print('Verified instance value',val,'is modified in clone for attribute',attr)      

def test_prototype_factory(instance, attr):
    """ Test prototype factory """

    factory = prototype_factory.PrototypeFactory()
    factory.register(instance)

    print('Making a clone of',instance)
    klone = factory.clone(instance.__class__)
    assert(klone != instance)
    print('Verified',klone,'is different from original instance',instance)
    
    # Access an attribute
    attr_val1 = getattr(instance, attr)
    attr_val2 = getattr(klone, attr)    

    # Ensure its same
    assert(attr_val1 == attr_val2)
    print('Verified clone attribute value same as instance for attribute',attr)

def test_singleton_prototype(klass, attr, val):
    """ Test singleton+prototype metaclass """

    test_singularity(klass)
    test_deep_prototype(klass, attr, val)


if __name__ == "__main__":
    test_deep_prototype(prototype_simple.MyClass, 'items', 400)
    test_shallow_prototype(prototype_simple.MySClass, 'items', 400)

    test_deep_prototype(prototype_meta.MyClass, 'items', 400)
    
    name = Name('Anand','Pillai')
    test_prototype_factory(name, 'first')

    address = Address('221B','Baker Street','London','6XE','UK')
    test_prototype_factory(address, 'street')

    test_singleton_prototype(prototype_singleton.MyClass, 'items', 500)
    print('All tests passed.')
