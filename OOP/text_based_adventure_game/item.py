class Item() : 
     
    def __init__(self) :
        # item_name is attribute for the name  
        self._name = None  
        self._description = None 
        self._level = None  
        self._type = None

    @property     
    def description(self) : 
        return self._description  
      
    @description.setter 
    def description(self,string) : 
        self._description = string  
    @property 
    def level(self) : 
        return self._level  
    @level.setter  
    def level(self,value) : 
        if value < 0 : 
            print("Invalid value. Type again")
        else : 
            self._level = value   
    def type(self) : 
        return self._type 
    # add additional attributes and methods 
    
    def get_item_details(self) : 
        print(" You have a ", self._name + "\n\n" + " Description " + self._description)
        print("Type of item",self._type + "\n\n"  +  " Level is " +  self._level)  
         
  
     

