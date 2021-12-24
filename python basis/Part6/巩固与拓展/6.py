class Person(object):
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def compute(self):
        Standard_weight = self.height-105
        return Standard_weight

    def Overweight(self):
        if self.weight > (self.compute()*1.1):
            print("{},您超重了!".format(self.name))
        else:
            print("{},您没有超重!".format(self.name))


class Women(Person):
    def __init__(self, name, height, weight):
        Person.__init__(self, name, height, weight)

    def compute(self):
        Standard_weight = (self.height-70)*0.6
        return Standard_weight


class Men(Person):
    def __init__(self, name, height, weight):
        Person.__init__(self, name, height, weight)

    def compute(self):
        Standard_weight = (self.height-80)*0.7
        return Standard_weight


def test(obj):
    obj.Overweight()


p1 = Person("zhangsan", 175, 60)
p2 = Men("lisi", 175, 58)
p3 = Women("feng", 152, 40)
test(p1)
test(p2)
test(p3)
