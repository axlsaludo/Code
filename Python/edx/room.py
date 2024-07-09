
# Room Class

class Room:
        def __init__(self, roomname):
            self.name = roomname
        
        def getDescription(self):
            return self.description
                
        def setDescription(self,roomDescription):
            self.description = roomDescription
            
        def linkRoom(self,roomToLink,direction):
            self.linkedRooms[direction] = roomToLink
            