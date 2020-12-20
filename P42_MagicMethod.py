# 构造和解析

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getPeri(self):
        return (self.x + self.y) * 2
    def getArea(self):
        return self.x * self.y

rect = Rectangle(3, 4)
rect.getPeri()
rect.getArea()

# 重写str，__new__
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)

a = CapStr("I lvoe You")
print(a)


class C:
    def __init__(self):
        print("我是__init__方法，我被调用了...")

    def __del__(self):
        print("我是__del__方法，我被调用了!!!")

c1 = C()

del c1
