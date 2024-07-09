
# Using room.py to create a room object

from room import Room

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")


# Setting the description of the kitchen and ballroom

kitchen.setDescription("A dank and dirty room buzzing with flies \n")
ballroom.setDescription("A vast room with shiny wooden floors.")


# The output of the code above is:

print(kitchen.getDescription(), ballroom.getDescription())