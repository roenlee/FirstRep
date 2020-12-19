import easygui as g
import sys

while 1:
    g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")

    msg = "请问你希望学习到什么知识呢？"

    title = "互动小游戏"

    choices = ["谈恋爱", "编程", "XXOO", "琴棋书画"]

    choice = g.choicebox(msg, title, choices)

    g.msgbox("你选择的是："+str(choice), "结果")

    msg = "你希望重新开始小游戏吗？"

    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
