# "Abstract Class" / Python Framework Testing ...
from AbsAble import absAble

class Charley(absAble):

    @classmethod
    def Create(cls, order):
        print("Charley: Creating", order)
        return cls()

    def say_hello(self):
        print("Greetings from Charley!")
        return True

