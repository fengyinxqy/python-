import math


class circular(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("圆的面积是:%.2f" % (math.pi*pow(self.radius, 2)))

    def circum(self):
        print("圆的周长是:%.2f" % (2*math.pi*self.radius))


radius1 = circular(5)
radius1.area()
radius1.circum()
