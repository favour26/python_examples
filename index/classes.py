class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print("talk")


favour = Person("Favour Dada")
print(favour.name)
favour.talk( )