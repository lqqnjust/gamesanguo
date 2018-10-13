# coding:utf-8

import unittest
import sys
import os

from sanguo.datamanager.datamanager import DataManager
from sanguo.datamanager.models import CityModel
from sanguo.datamanager.models import GeneralModel


class TestCity(unittest.TestCase): 

    def setUp(self):
        self.dm: DataManager = DataManager()
        self.dm.load_common()
        
    def test_develop_cost(self):
        city: CityModel = self.dm.cities[0]
        general = GeneralModel()
        general.intelligence = 99
        value = city.money_need_for_develop(general)
        self.assertIn(value,[18, 20, 22, 24, 26])

        general.intelligence = 53
        value = city.money_need_for_develop(general)
        self.assertIn(value, [14, 16, 18, 20, 22])

    
if __name__ == '__main__':
    unittest.main()