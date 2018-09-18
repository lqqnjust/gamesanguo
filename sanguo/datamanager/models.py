# coding:utf-8

'''
数据模型
'''


class GeneralModel(object):
    """
    武将数据信息
    """
    def __init__(self):
        self.id = 0
        self.name = None

        self.max_hp = 100
        self.cur_hp = 100
        # 武力
        self.atk = 100
        # 智力
        self.intelligence = 100
        # 品德
        self.morality =  100
        # 忠诚
        self.loyal = 100
        # 经验
        self.exp = 0
        # 等级
        self.level = 1
        # 士兵数
        self.solders = 1000
        # 状态 (在野，出仕，死亡，等待）
        self.state = 0
        # 跟随某个武将出仕
        self.follow = None
        # 所在城市
        self.city = None
        # 所属势力
        self.power = None

    def __str__(self):
        return '{}<{}>'.format(self.name, self.id)




class WeaponModel(object):
    """
    武器防具数据信息
    """
    def __init__(self, id, name, type, value, price):
        self.id = id
        self.name = name
        self.type = type
        self.value = value
        self.price = price


class CityModel(object):
    """
    城市信息
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
        # 当前
        self.generals = []
        # 在野
        self.out_generals = []

    def __unicode__(self):
        return '<{}>{}'.format(self.id, self.name)


class PowerModel(object):
    """
    势力
    """
    def __init__(self, general, color):
        pass
