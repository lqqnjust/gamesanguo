# coding:utf-8
from sanguo.tscenes import BaseTScene
from sanguo.tscenes.choosescene import ChooseScene
import sanguo

class MenuScene(BaseTScene):
    def __init__(self):
        print("1. 开始游戏")
        print("2. 继续游戏")
        print("3. 退    出")

    def run(self):
        while True:
            try:
                mode = int(input("请选择模式: "))
                sanguo.datamanager.game.init(mode)

                sanguo.tscenes.current_scene = ChooseScene()
                break
            except:
                print("只能输入1，2，3")
             
    