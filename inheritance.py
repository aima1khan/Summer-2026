class Mammal:
    def sound(self):
        print("hello")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def walk(self):
        print("Walk")

d1=Dog()
d1.sound()
d1.bark()
c1=Cat()
c1.sound()