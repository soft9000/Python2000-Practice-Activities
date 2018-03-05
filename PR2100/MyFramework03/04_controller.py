# Basic controller class
from MyFramework.Person import Person as zThing

class ThingCtrlr01:
    @staticmethod
    def Create():
        return zThing()
    
    @classmethod
    def Create(cls, myOrder):
        print(str(cls))
        return zThing()

var = ThingCtrlr01.Create("Fries & Soda")

if var.create() is True:
    print("Testing Success")




    








    


