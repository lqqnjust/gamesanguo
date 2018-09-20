# coding:utf-8

import pyglet

from cocos.layer import Layer

from sanguo.battle.Solder import Solder,DIRECTION_LEFT,DIRECTION_RIGHT,DIRECTION_UP,DIRECTION_DOWN


class BattleLayer(Layer):
    is_event_handler = True
    def __init__(self):
        super().__init__()

        self.solder = Solder(0, 0, 0,(24,24))

        self.add(self.solder.sprite)

    def on_key_press(self, key, modifiers):
        keystr = pyglet.window.key.symbol_string(key)
        if keystr == "RIGHT":
            self.solder.set_direction(DIRECTION_RIGHT)
        elif keystr == "UP":
            self.solder.set_direction(DIRECTION_UP)
        elif keystr == "DOWN":
            self.solder.set_direction(DIRECTION_DOWN)
        elif keystr == "LEFT":
            self.solder.set_direction(DIRECTION_LEFT)










