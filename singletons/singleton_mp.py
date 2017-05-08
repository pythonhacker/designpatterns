"""
Singleton on shared memory using multiprocessing module.
Using this singleton, two processes can share the same object
at the same memory location.

This is done by using the Manager object and its shared dictionary type.

"""

from multiprocessing import Manager

class SingletonS(object):
    """ A shared memory singleton class """
    
    def __init__(self, x=100):
        mgr = Manager()
        self._shared = mgr.dict()
        self.x = x

    def __setattr__(self, key, value):
        # For all lookups other than '_shared'
        # set value in the shared dictionary
        if key == '_shared':
            self.__dict__[key] = value
        else:
            self._shared[key] = value

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]


        # Lookups via shared memory
        return self._shared[key]
        
