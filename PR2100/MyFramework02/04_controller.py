# Basic controller class
from MyFramework.Person import Person as zThing

class ThingCtrlr01:
    @staticmethod
    def Create(recipe):
        return zThing()

var = ThingCtrlr01.Create("Fries & Soda")

if var.create() is True:
    print("Testing Success")




    








    


