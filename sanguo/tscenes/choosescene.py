# coding:utf-8
from sanguo.tscenes import BaseTScene
from sanguo.datamanager import datamanager


class ChooseScene(BaseTScene):
    def __init__(self):
        pass

    def run(self):
        for idx, power in enumerate(datamanager.powers):
            print("{}. {}".format(idx, power.starter.name))
        idx = int(input("选择势力:"))