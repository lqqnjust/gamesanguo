# coding:utf-8
import csv
import os

from sanguo.datamanager.models import GeneralModel

BASEDIR = os.path.dirname(os.path.dirname(__file__))


class DataManager(object):
    def __init__(self):
        self.generals = []
        self.cities = []


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
        filepath = os.path.join(BASEDIR,"resource/data/general.csv")
        with open(filepath, encoding='utf-8') as csvfile:
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

                    self.generals.append(general)



    def load_record(self, record):
        pass

    def save_record(self, record):
        pass


datamanager = DataManager()