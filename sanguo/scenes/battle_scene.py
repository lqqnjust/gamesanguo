# coding:utf-8
from cocos.scene import Scene

from .layers.battle_layer import BattleLayer

class BattleScene(Scene):
    def __init__(self, *children):
        super().__init__(*children)

        layer = BattleLayer()
        self.add(layer)