# This is a simple timer to record the time interval from you strat to end

import datetime
    

class MyTimer():
    def __init__(self):
        self.prompt = '未开始计时！'
        self.unit = '秒'
        self.last = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = "总共运行了"
        result = 0
        result = round((self.last[0] + other.last[0]),2)
        prompt = prompt + str(result) + self.unit
        return prompt

    # Start function
    def start(self):
        self.begin = datetime.datetime.now()
        print("开始计时...")
     
    # Stop function
    def stop(self):
        if not self.begin:
            print("请先调用start()进行计时！")
        else:
            self.end = datetime.datetime.now()
            self._calc()
            print("计时结束...")
            #print("计时结束，总共计时： %.2f 秒" % self.prompt)
        
    # 计算时间间隔
    def _calc(self):
        self.last.append(round((self.end - self.begin).total_seconds(),2))
        self.prompt = str(self.last[0]) + self.unit
        
        self.begin = 0
        self.end = 0

if __name__ == '__main__':
    print('程序开始')


