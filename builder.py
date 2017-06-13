"""
Builder design-pattern implemented as a House builder class example
( houses) with a few builder sub-classes.

NOTE: In this implementation, we have combined the director and the
builder into a single class.

The builder itself is responsible for building the house, adding rooms
and porches and returning the built house in its build() method.

"""

class Room(object):
    """ A class representing a Room in a house """
    
    def __init__(self, nwindows=2, direction='N'):
        self.nwindows = nwindows
        self.direction = direction

    def __str__(self):
        return "Room <facing:%s, windows=#%d>" % (self.direction,
                                                  self.nwindows)
class Porch(object):
    """ A class representing a Porch in a house """
    
    def __init__(self, ndoors=2, direction='W'):
        self.ndoors = ndoors
        self.direction = direction

    def __str__(self):
        return "Porch <facing:%s, doors=#%d>" % (self.direction,
                                                 self.ndoors)   
    
class House(object):
    """ A house class """

    def __init__(self, nrooms=0, nwindows=0,nporches=0):
        # windows per room
        self.nwindows = nwindows
        self.nporches = nporches
        self.nrooms = nrooms
        self.rooms = []
        self.porches = []

    def __str__(self):
        msg="House<rooms=#%d, porches=#%d>\n" % (self.nrooms,
                                                     self.nporches)

        for i in self.rooms:
            msg += str(i) + '\n'

        for i in self.porches:
            msg += str(i) + '\n'

        return msg

    def add_room(self,room):
        """ Add a room to the house """
        
        self.rooms.append(room)

    def add_porch(self,porch):
        """ Add a porch to the house """
        
        self.porches.append(porch)
    
class HouseBuilder(object):
    """ House builder class """

    def __init__(self, *args, **kwargs):
        self.house = House(*args, **kwargs)
        
    def build(self):
        """ Build a house instance and return it """
        
        self.build_rooms()
        self.build_porches()
        return self.house
    
    def build_rooms(self):
        """ Method to build rooms """
        
        for i in range(self.house.nrooms):
            room = Room(self.house.nwindows)
            self.house.add_room(room)

    def build_porches(self):
        """ Method to build porches """     

        for i in range(self.house.nporches):
            porch = Porch(1)
            self.house.add_porch(porch)


    
class BudgetHouseBuilder(HouseBuilder):
    """ Builder building budget  house with 1 room and no porch and rooms having 1 window """

    def __init__(self):
        self.house = House(nrooms=1, nporches=0, nwindows=1)

class VerySmallHouseBuilder(HouseBuilder):
    """ Builder building small  house with 2 rooms each having 1 windows and no porch """

    def __init__(self):
        self.house = House(nrooms=2, nporches=0, nwindows=1)        


class SmallHouseBuilder(HouseBuilder):
    """ Builder building small house with 2 rooms plus 1 porch each having 2 windows """

    def __init__(self):
        self.house = House(nrooms=2, nporches=1, nwindows=2)        


class EastFacingHouseBuilder(HouseBuilder):
    """ Builder building all rooms and porches facing east """

    def build_rooms(self):

        for i in range(self.house.nrooms):
            room = Room(self.house.nwindows, direction='E')
            self.house.add_room(room)

    def build_porches(self):

        for i in range(self.house.nporches):
            porch = Porch(1, direction='E')
            self.house.add_porch(porch)

class EastFacingSmallHouseBuilder(EastFacingHouseBuilder, SmallHouseBuilder):
    pass


if __name__ == "__main__":
    bbuilder = BudgetHouseBuilder()
    print(bbuilder.build())

    sbuilder = SmallHouseBuilder()
    print(sbuilder.build())

    nbuilder = EastFacingHouseBuilder(nrooms=2, nporches=1, nwindows=1)
    print(nbuilder.build())
    
    print(EastFacingSmallHouseBuilder().build())
    
