# coding:utf-8
import csv
import os
import codecs
from typing import List

from .models import CityModel
from .models import GeneralModel
from .models import State_Dict
from .models import GeneralModel
from .models import PowerModel
from .models import WeaponModel


BASEDIR = os.path.dirname(os.path.dirname(__file__))


class DataManager(object):
    def __init__(self):
        self.generals = []
        self.cities = []
        self.weapons = []
        self.powers: List[PowerModel] = []

    def load(self, record=None):
        """
        记载记录，如果为空，则读取初始化数据
        :param record:
        :return:
        """
        if record is None:
            self.load_common()
        else:
            self.load_record(record)

    def load_common(self):
        weapon_dict = {}

        # 加载武器数据
        filepath = os.path.join(BASEDIR, "resource/data/weapon.csv")
        with codecs.open(filepath, 'rb', 'gbk') as csvfile:
            reader = csv.reader(csvfile, dialect="excel-tab")
            for i, rows in enumerate(reader):
                if i != 0:

                    weapon = WeaponModel()
                    weapon.id = rows[0]
                    weapon.name = rows[1]
                    weapon.price = int(rows[2])
                    weapon.value = int(rows[3])
                    weapon.weight = int(rows[4])

                    weapon_dict[weapon.name] = weapon
                    self.weapons.append(weapon)

        # 加载将领数据
        general_dict = {}
        filepath = os.path.join(BASEDIR,"resource/data/general.csv")
        with codecs.open(filepath, 'rb', 'gbk') as csvfile:
            reader = csv.reader(csvfile)
            for i, rows in enumerate(reader):
                if i != 0:
                    general = GeneralModel()
                    general.id = rows[0]
                    general.name = rows[1]
                    general.max_hp = int(rows[2])
                    general.cur_hp = general.max_hp
                    general.atk = int(rows[3])
                    general.intelligence = int(rows[4])
                    general.loyal = int(rows[5])
                    general.morality = int(rows[6])
                    general.exp = int(rows[7])
                    general.solders = int(rows[8])
                    general.level = int(rows[12])

                    weapon_name = rows[9]
                    general.weapon = weapon_dict[weapon_name]
                    armor_name = rows[10]
                    general.armor = weapon_dict[armor_name]
                    general_dict[general.name] = general
                    self.generals.append(general)

        # 加载势力数据
        power_dict = {}
        filepath = os.path.join(BASEDIR, "resource/data/power.csv")
        with codecs.open(filepath, 'rb', 'gbk') as csvfile:
            reader = csv.reader(csvfile)
            for i, rows in enumerate(reader):
                if i != 0:
                    general = general_dict[rows[1]]
                    power = PowerModel(general)
                    power.id = rows[0]

                    power_dict[general.name] = power
                    self.powers.append(power)

        # 加载城市数据
        filepath = os.path.join(BASEDIR, "resource/data/city.csv")
        with codecs.open(filepath, 'rb', 'gbk') as csvfile:
            reader = csv.reader(csvfile)
            for i, rows in enumerate(reader):
                if i != 0:
                    city = CityModel()
                    city.id = rows[0]
                    city.name = rows[1]
                    power_name = rows[2]
                    if power_name != "空城":
                        city.power = power_dict[power_name]
                    city.money = int(rows[3])
                    city.food = int(rows[4])
                    city.population = int(rows[5])
                    city.farming = int(rows[6])
                    city.defence = int(rows[7])
                    city.security = int(rows[8])
                    city.redif = int(rows[9])
                    city.business = int(rows[10])
                    city.treasure = int(rows[11])

                    city.sold_price = int(rows[13])
                    city.buy_price = int(rows[14])

                    self.cities.append(city)



    def load_record(self, record):
        pass

    def save_record(self, record):
        pass


datamanager = DataManager()