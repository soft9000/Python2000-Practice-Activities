# "Abstract Class" / Python Framework Testing ...
from AbsAble import absAble

class Baker(absAble):

    @classmethod
    def Create(cls, order):
        print("Baker: Creating", order)
        return cls()

    def say_hello(self):
        print("Greetings from Baker!")
        return True

