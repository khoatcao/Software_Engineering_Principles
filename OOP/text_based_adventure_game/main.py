from room import Room # import data from room file
from item import Item # get from item file 
from rpginfo import RPGInfo
# create an object 
kitchen = Room()
kitchen.name = "kitchen"
#kitchen.description(" A dark room")
# create a new object 

# create a dining_hall 

dining_hall = Room()
dining_hall.name = "dining_hall"
#dining_hall.description(" A large room with something")

# 
ballroom = Room()
ballroom.name = "Ballroom"
#ballroom.description(" A vast room with a shiny something")

kitchen.link_room(dining_hall,"south")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

kitchen.get_details() 
dining_hall.get_details() 
ballroom.get_details()

spooky_castle = RPGInfo("The Spooky Castle")
RPGInfo.welcome("Move game") 

spooky_castle.info() 
current_room = kitchen

RPGInfo.author = "Cao Toan Khoa" 
RPGInfo.credits() 


while True : 
    print("\n")
    current_room.get_details()

    command = input(">")

    current_room = current_room.move(command) 



