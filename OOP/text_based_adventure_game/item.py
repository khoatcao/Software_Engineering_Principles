class Item() : 
     
    def __init__(self,item_name) :
        # item_name is attribute for the name  
        self.name = item_name 
        self.description = None 
        self.level = 1 
        self.type = None

    
    def set_description(self,item_description) : 
        self.description = item_description 
      
    
    def get_description(self) : 
        return self.description 
    
    def set_level(self,level) : 
        self.level = level 
    
    def get_level(self) : 
        return self.level 

    def set_type(self,type) : 
        self.type = type 
    # add additional attributes and methods 
    

    def get_item_details(self) : 
        print(" You have a ", self.name + "\n\n" + " Description " + self.description)
        print("Type of item",self.type + "\n\n"  +  " Level is " +  self.level)  
         
  
     

