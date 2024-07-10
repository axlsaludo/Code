
class Item():
    def __init__(self):
        self.name = None
        self.description = None

    def getName(self):
        return self.name
    
    def setName(self, itemName):
        self.name = itemName
    
    def getDescription(self):
        return self.description
    
    def setDescription(self, itemDescription):
        self.description = itemDescription     