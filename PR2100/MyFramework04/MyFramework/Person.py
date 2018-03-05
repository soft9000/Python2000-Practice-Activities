from MyFramework.AbsThing import Thing

class Person(Thing):

    @classmethod
    def Create(recipe, order=None):
        return recipe()
    
    def create(self):
        return True

    def read(self):
        return True

    def update(self):
        return True

    def delete(self):
        return True


