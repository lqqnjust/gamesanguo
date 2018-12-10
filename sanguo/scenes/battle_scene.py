# coding:utf-8
from cocos.scene import Scene
from pytmx.util_pyglet import pyglet_image_loader,load_pyglet

from .layer import BattleLayer
from .layer import GeneralInfoLayer
from sanguo.scenes.sprites.ArmySprite import ArmySprite

class BattleScene(Scene):
    """
    大战场
    """
    def __init__(self, *children):
        super().__init__(*children)



        layer = BattleLayer()
        self.add(layer)
        #
        # from sanguo.datamanager.datamanager import DataManager
        #
        # dm = DataManager()
        # dm.load_common()
        #
        # generalmodel = dm.generals[0]
        #
        # infolayer = GeneralInfoLayer(generalmodel)
        # self.add(infolayer)
        # army_unit = ArmySprite(None,32,32,(255,255,255,255))
        # army_unit.position = 128,128
        # self.add(army_unit)


