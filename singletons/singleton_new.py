""" Singleton by overriding the __new__ method on Python classes
on class as well as meta-class """


# At meta-class level
class MetaSingletonN(type):
    """ A type for Singleton classes by overriding __new__ """

    def my_new(cls,name,bases=(),dct={}):
        if not cls.instance:
            cls.instance = object.__new__(cls)
                
        return cls.instance
    
    def __init__(cls, name, bases, dct):
        super(MetaSingletonN, cls).__init__(name, bases, dct)
        cls.instance = None
        cls.__new__ = cls.my_new
        
class Singleton(object):
    """ By overriding the __new__ method of the class and
    using dictionaries """

    def __new__(cls):
        if '_instance' not in cls.__dict__:
            cls._instance = object.__new__(cls)
        return cls.__dict__['_instance']

class SingletonN(metaclass=MetaSingletonN):
    """ A singleton class using the MetaSingletonN class as metaclass """
    pass
