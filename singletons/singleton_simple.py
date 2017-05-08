"""
A basic implementation of Singleton -in a pattern similar to how its
implemented in more traditional languages
"""

class Singleton(object):
    """ A basic implementation of Singleton """

    instance = None

    @classmethod
    def getInstance(cls):
        
        if cls.instance == None:
            cls.instance = cls()
        return cls.instance

