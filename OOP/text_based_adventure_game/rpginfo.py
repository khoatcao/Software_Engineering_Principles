class RPGInfo() : 
    # define class variable 
    author = "Khoa" # name of the author who made the game 
    def __init__(self,title_game) : 
        self.title = title_game 

    def welcome(self) : 
        print("Welcome to " + str(self.title))

    @staticmethod 
    def info() : 

        print("Made using the OOP game creator (c) me ")
    # using classmethod allow you to interact with class variables like overriding in other programming languages 
    @classmethod 
    def credits(cls) :
        print("Thank you for playing")
        print("Created by " + cls.author) 

    
    


