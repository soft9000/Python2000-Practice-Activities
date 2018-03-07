class Skitz:

    def __init__(self, zName=None, zAge=None, zPhone=None):
        self.name=zName;self._age=zAge;self.phone=zPhone

    def set_age(self, age):
        if age < 0:
            raise ValueError("Error: Age is negative")
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, zAge):
        self.set_age(zAge)
    
var = Skitz()

