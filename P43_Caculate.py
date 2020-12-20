class New_int(int):
    def __add__(self, other):
        return int.__sub__(self, other)
    def __sub__(sel, other):
        return int.__add__(self, other)

a = New_int(3)
b = New_int(5)
c = a + b
print(c)


class Try_int(int):
    def __add__(self, other):
        return int(self) + int(other)
    def __sub__(self, other):
        return int(self) - int(other)

e = Try_int(4)
f = Try_int(10)
g = e + f
print(g)
