from room import Room # import data from room file
from item import Item # get from item file 
# create an object 
kitchen = Room("kitchen")
kitchen.set_description(" A dark and dirty room")
# create a new object 

# create a dining_hall 

dining_hall = Room("dining_hall")
dining_hall.set_description(" A large room with something")

# 
ballroom = Room("Ballroom")
ballroom.set_description(" A vast room with a shiny something")

kitchen.link_room(dining_hall,"south")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

kitchen.get_details() 
dining_hall.get_details() 
ballroom.get_details()

current_room = kitchen

while True : 
    print("\n")
    current_room.get_details()

    command = input(">")

    current_room = current_room.move(command) 


