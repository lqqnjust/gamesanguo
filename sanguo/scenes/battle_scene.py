# coding:utf-8
from cocos.scene import Scene

from .layer import BattleLayer
from .layer import GeneralInfoLayer


class BattleScene(Scene):
    def __init__(self, *children):
        super().__init__(*children)

        layer = BattleLayer()
        self.add(layer)

        from sanguo.datamanager.datamanager import DataManager

        dm = DataManager()
        dm.load_common()

        generalmodel = dm.generals[0]

        infolayer = GeneralInfoLayer(generalmodel)
        self.add(infolayer)