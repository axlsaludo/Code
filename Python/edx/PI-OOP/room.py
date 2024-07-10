
# class Room

class Room:
    
    noOfRooms = 0
    
    def __init__(self, roomName):
        self.name = roomName
        self.description = None 
        self.linkedRooms = {}
        self.character = None
        Room.noOfRooms = Room.noOfRooms + 1
       
    def setDescription(self, roomDescription):
        self.description = roomDescription
        
    def getDescription(self):
        return self.description
    
    def getName(self):
        return self.name
    
    def describe(self):
        print(self.description)
    
    def linkRoom(self, roomToLink, direction):
        self.linkedRooms[direction] = roomToLink
        # print(self.name + " linked rooms: " + repr(self.linkedRooms))
        
    def getDetails(self):
        print("The " + self.name)
        print("----------------")
        print(self.description)
        for direction in self.linkedRooms:
            room = self.linkedRooms[direction]
            print("The " + room.getName() + " is " + direction)

    def move(self,direction):
        if direction in self.linkedRooms:
            return self.linkedRooms[direction]
        else:
            print("You can't go that way")
            return self
    
    def set_character(self, new_character):
        self.character = new_character  
        
    def get_character(self):
        return self.character
    
    