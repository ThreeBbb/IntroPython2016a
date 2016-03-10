

#create a circle

class Circle (object):

    def __init__(self,radius,*args,**kwargs):
        self.radius = radius
        self.diameter = radius * 2
        self.area = 3.14 * (radius * radius)

     ################################ radius
    @ property
    def radius(self):
        return self._radius

    @ radius.setter
    def radius(self,value):

        print("*****im in radius setter \t", end="")

        if value < 1: print("that is a very small circle!")
        if value > 3: print("that is a good size circle!")
        self._radius = value

    ################################ diameter
    @ property
    def diameter(self):
        return self._radius * 2

    @ diameter.setter
    def diameter(self,value):
        print("*****im in diameter setter")
        self._radius = (value / 2)
        self._diameter = value

     ################################ area

    # def area(self):
    #     return self._area
    #
    #
    # def area(self,value):
    #     raise AttributeError



c1 = Circle(2)
print("c1's radius is: {} and diameter is {} ".format(c1.radius, c1.diameter))

c2 = Circle(3)
print("c2's radius is: {} and diameter is {} ".format(c2.radius, c2.diameter))
#print("c2's diameter: " , c2.diameter)
#print("c2's radius: " , c2.radius)

c2.diameter = 7
print("c2's radius is: {} and diameter is {} ".format(c2.radius, c2.diameter))
# print("now c2's diameter: " , c2.diameter)
# print("and c2's radius: " , c2.radius)

c1.radius = 5
print("c1's radius is: {} and diameter is {} ".format(c1.radius, c1.diameter))

print("c1.area is {}".format(c1.area))
c1.area = 14
print("c1.area is {}".format(c1.area))