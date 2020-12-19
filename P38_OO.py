class Ball:
    def __init__(self, name = '未定义球'):
            self.name = name
    def kick(self):
            print("我叫%s,该死的，谁踢我！！！" % self.name)

b = Ball('土豆')
b.kick()
c = Ball()
c.kick()


# 私有变量，在变量名前加__即可

class Person:
    __name = "大虾"
    def getName(self):
            return self.__name

p = Person()
# 此方法不行
# name = p.__name()

name = p.getName()
print(name)

# 或者
name2 = p._Person__name
print(name2)
