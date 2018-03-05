# demonstrate attribute management

class Eggs:
    def __init__(self):
        self.spam = None

    def say_hi(self):
        pass

    @classmethod
    def say_hiC(cls):
        pass

    @staticmethod
    def say_hiS(self):
        pass
    
names = ("spam", "say_hi", "say_hiC", "say_hiS", "noneya")
obj = Eggs()
for name in names:
    if hasattr(obj, name):
        print("Found", name)


    
