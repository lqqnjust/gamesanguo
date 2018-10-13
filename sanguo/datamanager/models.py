# coding:utf-8
from typing import List
from enum import Enum
import random



class WeaponType(Enum):
    """
    武器类型
    """
    # 剑
    SWORD = 0
    # 刀
    KNIFE = 1
    # 矛
    SPEAR = 2
    # 防
    ARMOR = 3


class WeaponModel(object):
    """
    武器防具数据信息
    """
    def __init__(self):
        self.id: str = None
        # 名称
        self.name: str = None
        # 类型剑刀矛防
        self.type: int = None
        # 攻击值或者防御值
        self.value: int = None
        # 商店价格
        self.price: int = None
        # 重量
        self.weight: int = None

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class GeneralStatus(Enum):
    # 仕官
    OFFICE = 0
    # 在野
    UNOFFICE = 1
    DIE = 2


State_Dict = {
    "仕官": GeneralStatus.OFFICE,
    "在野": GeneralStatus.UNOFFICE
}


class GeneralModel(object):
    """
    武将数据信息
    """
    def __init__(self):
        self.id: str = None
        self.name: str = None

        self.max_hp: int = 100
        self.cur_hp: int = 100
        # 武力
        self.atk: int = 100
        # 智力
        self.intelligence: int = 100
        # 品德
        self.morality: int = 100
        # 忠诚
        self.loyal: int = 100
        # 经验
        self.exp: int = 0
        # 等级
        self.level: int = 1
        # 士兵数
        self.solders: int = 1000
        # 状态 (在野，出仕，死亡，等待）
        self.state = GeneralStatus.UNOFFICE
        # 武器
        self.weapon: WeaponModel = None
        # 防具
        self.armor: WeaponModel = None

    def __str__(self):
        return '{}<{}>'.format(self.name, self.id)

    def die(self):
        """
        死亡
        :return:
        """
        self.state = GeneralStatus.DIE

    def add_exp(self, exp):
        """
        经验增加
        :param exp:
        :return:
        """
        self.exp += exp

    def level_up(self, level):
        """
        升级
        :param level:
        :return:
        """
        self.level = level


class PowerModel(object):
    """
    势力
    """

    def __init__(self, general: GeneralModel):
        self.starter: GeneralModel = general
        self.inheritor: GeneralModel = general

        self.inheritor_list: List[GeneralModel] = []

    def set_inheritor(self, general: GeneralModel):
        """
        设置继承人
        :param general:
        :return:
        """
        self.inheritor = general


class CityModel(object):
    """
    城市信息
    """
    def __init__(self):
        self.id: str = None
        self.name: str = None

        # 金钱
        self.money: int = 0
        # 粮食
        self.food: int = 0

        # 农业 0-999
        self.farming: int = 0
        # 经济贸易 0-999
        self.business: int = 0
        # 人口 0-99900, 只存储去除00的部分。
        self.population: int = 0
        # 城防 0-100
        self.defence: int = 0
        # 治安统治度 0-100
        self.security: int = 0
        # 预备兵
        self.redif: int = 100
        # 所属势力
        self.power: PowerModel = None

        # 宝
        self.treasure = 0

        # 买米价格
        self.buy_price = 0
        # 卖米价格
        self.sold_price = 0

        # 当前
        self.generals :List[GeneralModel] = []
        # 在野
        self.out_generals = []

    def __unicode__(self):
        return '<{}>{}'.format(self.id, self.name)

    def leader(self):
        """
        获取太守
        :return:
        """
        if len(self.generals) == 0:
            return None
        else:
            return self.generals[0]

    def get_power(self) -> PowerModel:
        """
        获取势力
        :return:
        """
        if self.power is None:
            return None
        else:
            return self.power.inheritor

    def change_leader(self, idx: int):
        """
        交换太守
        :param idx: 新的将领的城市内索引
        :return:
        """
        tmp = self.generals[idx]
        self.generals[idx] = self.generals[0]
        self.generals[0] = tmp

    @property
    def total_solders(self) -> int:
        total = 0
        for general in self.generals:
            total += general.solders
        return total

    def add_business(self, general: GeneralModel, money: int):
        """
        提升商业
        :param general: 执行武将
        :param money: 投入的资金
        :return:
        """
        result = money * general.intelligence / 100 * random.randint(10, 17) /10
        self.security += 1
        if result >= 32:
            self.security += 1
        self.business += result
        if self.business >= 999:
            self.business = 999
        return result

    def add_farming(self, general: GeneralModel, money: int):
        """
        提升农业
        :param general: 执行武将
        :param money: 投入的资金
        :return:
        """
        result = money * general.intelligence / 100 * random.randint(10, 17) /10
        self.security += 1
        if result >= 32:
            self.security += 1
        self.farming += result
        if self.farming >= 999:
            self.farming = 999
        return result

    @staticmethod
    def money_need_for_develop(general: GeneralModel):
        """
        开发土地或产业需要的金钱
        :param general:
        :return:
        """
        if general.intelligence >= 81:
            return random.choice([18, 20, 22, 24, 26])
        elif general.intelligence >= 51:
            return random.choice([14, 16, 18, 20, 22])
        else:
            return random.choice([10, 12, 14, 16, 18])

    def gain_money(self):
        """
        4月收获金钱
        """
        B, C, D = self.get_level_coef()
        A = self.get_coef_security()
        money =  A * B * self.population * (1+self.business/D)
        self.money += round(money)
        if self.money > 9999:
            self.money = 9999

    def gain_food(self):
        """
        10月收获粮食
        """
        B, C, D = self.get_level_coef()
        A = self.get_coef_security()
        food =  A * C * self.population * (1+self.farming/D)
        self.food += round(food)
        if self.food > 9999:
            self.food = 9999

    def get_coef_security(self):
        """
        根据统治度计算系数
        """
        if self.security <= 50:
            return 1.0
        elif self.security <= 70:
            return 1.2
        elif self.security <= 80:
            return 1.4
        elif self.security <= 90:
            return 1.8
        elif self.security <= 99:
            return 1.8
        else:
            return 2.0

    def get_level_coef(self):
        # level 1
        #return 5/8, 5/6, 300
        # level 2
        # return 3/8 , 1/2 , 180
        # level 3
        return 3/8, 1/2, 240


