# coding:utf-8
import pickle

from sanguo.datamanager import datamanager


class Game(object):
    def __init__(self):
        # 玩家势力
        self.player_power = None
        # 数据
        self.datamgr = datamanager
        # 年份
        self.year = 189
        # 月份
        self.month = 1
        # 顺序
        self.turns = []
        # 当前编号
        self.turn_now = 0

    def init(self, mode):
        if mode == 1:
            self.datamgr.load_common()
        else:
            print("继续游戏")

    def set_player_power(self, index):
        self.player_power = index

    def next_month(self):
        """
        下一个月
        """
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

    def next_turn(self):
        self.turn_now += 1
        if self.turn_now >= len(self.turns):
            self.turn_now = 0
        return self.turns[self.turn_now]

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.player_power, self.datamgr, self.year, self.month, self.turns, self.turn_now), f)

    def load(self, filename):
        with open(filename, 'rb') as f:
            self.player_power, self.datamgr, self.year, self.month, self.turns, self.turn_now = pickle.load(f)


game = Game()