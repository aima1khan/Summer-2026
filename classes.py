class Point:
    def __init__(self,name): #Constructor
        self.name=name
    def draw(self):
        print(f"Draw {self.name}")

    def hello(self):
        print(f"Hello {self.name}")

point1 = Point("Aimal")
print(point1.hello())
point1.x=10
point1.y=20
print(point1.x)
print(point1.y)
point1.hello()
point1.draw()
print(point1)