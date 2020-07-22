class Rectangle:
    def __init__(self, width, height ):
        self.width = width
        self.height = height
        print("When the object is created automatically get assigned:",self.width)
        print("When the object is created automatically get assigned:",self.height)

    # def compare(self):
    #     if self.width == self.height:
    #         return True
    #     else:
    #         return False

    def __eq__(self, other):
        if self.width == other.width:
            print("Equal")
            return True
        else:
            print("Unequal")
            return False




r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
a = r1.__eq__(r2)
# a = r1.compare()
print(a)
