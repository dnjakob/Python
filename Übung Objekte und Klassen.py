class Person:

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def vorstellen(self):
        print(self.name, self.alter)