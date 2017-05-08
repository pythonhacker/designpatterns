"""

The Singleton Pattern - In different implementation avatars.

"""

from singletons import singleton_simple
from singletons import singleton_new
from singletons import singleton_call
from singletons import singleton_deco
from singletons import singleton_mp

from multiprocessing import Process

def test_singularity(cls):
    """ Test if the given class is a Singleton """

    instance1 = cls()
    instance2 = cls()

    return instance1 == instance2

def f1(x, instance):
    instance.x = x
    print('instance.x==',instance, instance.x)

def f2(instance):
    # Will print modified value in f1
    print('instance.x==',instance, instance.x)

def f3(y, instance):
    # Add a dynamic attribute y
    instance.y = y
    
def test_multiprocess_singleton(cls):
    """ Test multiprocess shared singleton """
    
    s = cls(x=100)
    p1 = Process(target=f1, args=(200, s))
    p2 = Process(target=f2, args=(s,))
    p3 = Process(target=f3, args=('shared memory', s)) 

    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()

    # Print final values
    print('instance.x=',s.x)
    print('instance.y=',s.y) 

    # Assertions
    assert(s.x == 200)
    assert(s.y == 'shared memory')
    
if __name__ == "__main__":
    assert(test_singularity(singleton_simple.Singleton.getInstance))
    assert(test_singularity(singleton_new.Singleton))
    assert(test_singularity(singleton_new.SingletonN))
    assert(test_singularity(singleton_call.SingletonC))
    assert(test_singularity(singleton_deco.SingletonD))
    test_multiprocess_singleton(singleton_mp.SingletonS)

    
