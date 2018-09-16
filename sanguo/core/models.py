# coding:utf-8

'''
数据模型
'''


class GeneralModel(object):
    """
    武将数据信息
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __unicode__(self):
        return '{}'.format(self.name)


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
    def __init__(self, id, name):
        self.id = id
        self.name = name
