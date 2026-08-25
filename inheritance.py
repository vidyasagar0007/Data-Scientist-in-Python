class Animal:
    def show(self):
        print("Aminal show method")
class Cat(Animal):
    def make_sound(self):
        print("meowww...")
class Dog(Cat):
    def dog_sound(self):
        print("bhowwww")
d=Dog()
d.dog_sound()
d.make_sound()
d.show()