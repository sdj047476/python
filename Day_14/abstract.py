# abstract - 2
# 추상 클래스
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_round(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        return 3.14 * self.radius ** 2

    def get_round(self):
        return 3.14 * self.radius * 2

class Square(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def get_area(self):
        return self.length * self.width

    def get_round(self):
        return (self.length + self.width) * 2
class Triangle(Shape):
    def __init__(self, l, l_1, l_2, h):
        self.length = l
        self.length_1 = l_1
        self.length_2 = l_2
        self.height = h

    def get_area(self):
        return self.length * self.height * 0.5

    def get_round(self):
        return self.length + self.length_1 + self.length_2

A = Triangle(8,5,4,3)
B = Square(6,8)
print(f"Triangle A.round : {A.get_round()}\nTriangle A.area : {A.get_area()}")
print(f"Square B.round : {B.get_round()}\nSquare A.area : {B.get_area()}")
