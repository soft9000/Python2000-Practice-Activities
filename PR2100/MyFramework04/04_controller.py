# Basic controller class
from MyFramework.Person import Person as zThing

class ThingCtrlr01:
    @staticmethod
    def Create(order=None):
        return zThing.Create(order)

var = ThingCtrlr01.Create()

if var.create() is True:
    print("Testing Success")




    








    


