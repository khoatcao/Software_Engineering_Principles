class Room() : 
    def __init__(self) : 
        self._name = None 
        self._description = None 
        self.linked_rooms = {}

    # adding more methods in python
    # getter in python return results  
    @property 
    def description(self) : 
        string_attribute = str(self._description)

        return string_attribute   
    # setter 
    @description.setter
    def description(self, string) : 
         if len(string) > 10 :
             print("type again? Must least than 10 characaters")

         else : 
             self._description = string  
               
            
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

            print("The " + room.get_name() + " is " + direction)

    def move(self,direction) : 

        if direction in self.linked_rooms : 
            return self.linked_rooms[direction]
        
        else : 
            print("You can not go that way")
            return self 
