class compute(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Add(self):
        print("a+b=%d" % (self.num1+self.num2))

    def Sub(self):
        print("a-b=%d" % (self.num1-self.num2))

    def Mult(self):
        print("a*b=%d" % (self.num1*self.num2))

    def Div(self):
        print("a/b=%.2f" % (self.num1/self.num2))


compute1 = compute(8, 4)
compute1.Add()
compute1.Sub()
compute1.Mult()
compute1.Div()
