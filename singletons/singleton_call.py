""" Singleton by overriding the __call__ method on metaclass """

class MetaSingletonC(type):
    """ A type for Singleton classes (overrides __call__) """    

    def __init__(cls, *args):
        print(cls,"__init__ method called with args", args)
        type.__init__(cls, *args)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls,"creating instance", args, kwargs)
            cls.instance = type.__call__(cls, *args, **kwargs)
        return cls.instance

class SingletonC(metaclass=MetaSingletonC):
    """ A singleton class using the MetaSingletonN class as metaclass """
    pass
