number = 0


def add(num1, num2):
    global number
    number = num1+num2
    print("函数内变量number: ", number)
    return number


add(1, 2)
print("函数外变量number: ", number)
