# coding:utf-8
from typing import List
from .models import GeneralModel
"""
战场管理
"""


class Army(object):
    """
    战场双方
    """
    def __init__(self):
        # 所属势力
        self.power = None
        # 机动力
        self.mobility = 0
        # 双方部队颜色， 分红为我方， 蓝为敌方
        self.color: int = None
        # 金钱
        self.money: int = 0
        self.food: int = 0
        # 主帅
        self.leader: GeneralModel = None
        # 部队列表
        self.generals: List[GeneralModel] = None
        # 俘虏
        self.prisoners: List[GeneralModel] = []
        # 己方死亡
        self.dead: List[GeneralModel] = []

        # 杀敌
        self.killed_solders = 0
        # 损失
        self.lost_solders = 0

    def cal_mobility(self):
        """
        重新计算机动力
        :return:
        """
        return 0




