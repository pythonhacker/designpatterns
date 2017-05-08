""" Singleton by using decorators """

def singleton(func):
    """ Singleton as a method decorator """

    def wrapper(klass, *args):

        if not hasattr(klass, 'instance') or klass.instance is None:
            klass.instance =  object.__new__(klass)

        return klass.instance
    
    return wrapper

class SingletonD(object):

    @singleton
    def __new__(cls):
        pass
