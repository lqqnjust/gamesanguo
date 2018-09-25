# coding:utf-8

from sanguo.datamanager.datamanager import DataManager

if __name__ == '__main__':
    dm = DataManager()
    dm.load_common()
    print(len(dm.generals))
    for g in dm.generals:
        print(g.__dict__)

    for city in dm.cities:
        print(city.__dict__)