class Vector3(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def Add(self, v):
        v1 = Vector3()
        v1.x = self.x+v.x
        v1.y = self.y+v.y
        v1.z = self.z+v.z
        return v1

    def Sub(self, v):
        v1 = Vector3()
        v1.x = self.x-v.x
        v1.y = self.y-v.y
        v1.z = self.z-v.z
        return v1

    def Mul(self, n):
        v1 = Vector3()
        v1.x = self.x*n
        v1.y = self.y*n
        v1.z = self.z*n
        return v1

    def Div(self, n):
        v1 = Vector3()
        v1.x = self.x/n
        v1.y = self.y/n
        v1.z = self.z/n
        return v1

    def show(self):
        print((self.x, self.y, self.z))


v1 = Vector3(1, 2, 3)
v2 = Vector3(4, 5, 6)
v3 = v2.Add(v1)
v3.show()
v4 = v2.Sub(v1)
v4.show()
v5 = v2.Mul(2)
v5.show()
v6 = v2.Div(2)
v6.show()
