#!/usr/bin/env python3

class Circle:
    def __init__(self, radius):
        self.radius=1

    def area(self):
        return self.radius**2 * 3.14159



if __name__ == '__main__':
    my_circle=Circle(5)
    print(my_circle.radius)
    print(my_circle.area())
    my_circle.radius=10
    print(2*3.14159*my_circle.radius)
