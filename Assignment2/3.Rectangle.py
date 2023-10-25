class Rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def area(self):
        return self.lenght*self.width
    def perimeter(self):
        return 2*(self.lenght+self.width)
    def compare(self,other_rectangle):
        area1=self.area()
        area2=other_rectangle.area()
        if area1>area2:
            return "The first rectangle has a larger area."
        elif area1<area2:
            return "The second rectangle has a larger area."
        else:
            return "Both rectangles have the same area."
r1=Rectangle(2,4)
r2=Rectangle(3,5)
print("Area of 1st Rectangle:",r1.area())
print("Perimeter of 1st Rectangle:",r1.perimeter())
print("Area of 2nd Rectangle:",r2.area())
print("Perimeter of 2nd Rectangle:",r2.perimeter())
print(r1.compare(r2))
