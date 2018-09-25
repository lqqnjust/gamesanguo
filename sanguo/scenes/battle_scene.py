# coding:utf-8
from cocos.scene import Scene
from pytmx.util_pyglet import pyglet_image_loader,load_pyglet

from .layer import BattleLayer
from .layer import GeneralInfoLayer


class BattleScene(Scene):
    def __init__(self, *children):
        super().__init__(*children)

        tmx_data = load_pyglet("sanguo/resource/smallbattle/water.tmx")
        layer = tmx_data['layer1']
        self.add(layer)

        layer = BattleLayer()
        self.add(layer)

        from sanguo.datamanager.datamanager import DataManager

        dm = DataManager()
        dm.load_common()

        generalmodel = dm.generals[0]

        infolayer = GeneralInfoLayer(generalmodel)
        self.add(infolayer)


