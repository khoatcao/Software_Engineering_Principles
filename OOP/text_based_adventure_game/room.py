class Room() : 
    def __init__(self) : 
        self._name = None 
        self._description = None 
        self.linked_rooms = {}

    # adding more methods in python
    # getter in python return results  
    @property 
    def description(self) : 
        if self._description is None : 
            print("You did not assign name of description")

        else : 
            return self._description 
    # setter 
    @description.setter
    def description(self,value) :
        if self._description != str : 
            print("Invalid value") 
        else : 
            self._description = value          
    @property # getter equally  
    def name(self) : 
        return self._name     
    @name.setter 
    def name(self,room_name) : 
        self._name = room_name 

    def describe(self) : 
        print(self._description)
    
    
    def link_room(self,room_to_link,direction) : 
        self.linked_rooms[direction] = room_to_link
        print(self.name + "linked rooms : " + repr(self.linked_rooms))

    def get_details(self) : 
        for direction in self.linked_rooms : 
            room = self.linked_rooms[direction]

            print("The " + room.name + " is " + direction)

    def move(self,direction) : 

        if direction in self.linked_rooms : 
            return self.linked_rooms[direction]
        
        else : 
            print("You can not go that way")
            return self 
