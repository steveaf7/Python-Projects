

# ABC gives the class the ability to have an abstract method,
# and abstractmethod is how we identify the abstract mehtod to the computer
from abc import ABC, abstractmethod
class meat(ABC):

    def howToStore(self):
        print("Make sure to store all raw and cooked meat in the fridge or freezer.")
        
    @abstractmethod #defines the below method as an abstract method
    def howToCook(self): 
        pass

class beefSteak(meat):
    def howToCook(self): #define the abstractmethod in the child class
        print("I look to cook my steaks on a grill to medium rare")


obj = beefSteak()
obj.howToStore()
obj.howToCook()
