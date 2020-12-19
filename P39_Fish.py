import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置是：", self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self) # 重写继承方法1
        super().__init__() #重写继承方法2
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有的吃")
            self.hungry = False
        else:
            print("太撑了，吃不下了！")

fish = Fish()
fish.move()

goldfish = Goldfish()
goldfish.move()

shark = Shark()
shark.eat()
shark.move()

# 方法1 相当于 Fish.__init__(shark) -> shark.move()

# shark.move() 会报错，因为Shak定义时覆盖了父类的__init_(self)，导致没有x,y 属性
# 重写方法1 ->调用未绑定的父类方法

# 使用super函数
