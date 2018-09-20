# coding:utf-8

import pyglet

from cocos.layer import Layer
from cocos.actions import MoveBy

from sanguo.battle.Solder import Solder,DIRECTION_LEFT,DIRECTION_RIGHT,DIRECTION_UP,DIRECTION_DOWN


class BattleLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()

        self.solder = Solder(0, 0, 0,(24,24))

        self.add(self.solder.sprite)

    def on_key_press(self, key, modifiers):
        keystr = pyglet.window.key.symbol_string(key)
        print(keystr)
        if keystr == "RIGHT":
            self.solder.set_direction(DIRECTION_RIGHT)
            self.solder.sprite.do(MoveBy((48,0),0.5))
        elif keystr == "UP":
            self.solder.set_direction(DIRECTION_UP)
            self.solder.sprite.do(MoveBy((0, 48), 0.5))
        elif keystr == "DOWN":
            self.solder.set_direction(DIRECTION_DOWN)
            self.solder.sprite.do(MoveBy((0, -48), 0.5))
        elif keystr == "LEFT":
            self.solder.set_direction(DIRECTION_LEFT)
            self.solder.sprite.do(MoveBy((-48, 0), 0.5))
        elif keystr == "K":
            self.solder.set_atk(0)
            self.solder.set_direction(0)










