
# Using room.py to create a room object
from character import Enemy
from character import Character
from room import Room

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
diningHall = Room("Dining Hall")


# Setting the description of the kitchen and ballroom

kitchen.setDescription("A dank and dirty room buzzing with flies.")
ballroom.setDescription("A vast room with shiny wooden floors.")
diningHall.setDescription("A large room with ornate golden decorations on each wall.")


# The output of the code above is:

diningHall.linkRoom(ballroom, "west")
kitchen.linkRoom(diningHall, "south")
diningHall.linkRoom(kitchen, "north")
ballroom.linkRoom(diningHall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.setWeakness("cheese")
dave.set_conversation("I'm hungry, braiiiiiiins")
diningHall.set_character(dave)

catria = Character("Catria", "A friendly skeleton")
catria.set_conversation("Why hello there.")
ballroom.set_character(catria)

currentRoom = kitchen
dead = False

while dead == False:
    print("\n")
    currentRoom.getDetails()
    inhabitant = currentRoom.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        currentRoom = currentRoom.move(command)
        
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None:
            print("what will you fight with?")
            fight_with = input()
            
            if inhabitant.fight(fight_with) == True:
                print("Hooray, you won the fight!")
                currentRoom.set_character(None)
            else:
                print("Oh dear, you lost the fight.")
                print("That's the end of the game")
                dead = True
        else:
            print("I don't understand what you're trying to do.")
    
    elif command == "hug":
        if inhabitant is not None:
            if inhabitant.name == "Dave":
                print("Dave doesn't seem like the hugging type.")
            else:
                inhabitant.hug()
        else:  
            print("There's no one here to hug.")
            
    elif command == "quit":
        dead = True
        print("Quitting game")  
            
        