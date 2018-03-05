# Basic inheritance concepts ...

class Able:

    def say_hello(self):
        print("Hello - from Able")

class Baker(Able):

    def say_hello(self):
        print("Greetings from Baker!")

var = Able()

if isinstance(var, Baker):
    print("Is Baker")
else:
    print("Is NOT")
