# coding:utf-8

import pyglet

from cocos.layer import Layer
from cocos.actions import MoveBy
from cocos.text import Label

from .sprites.Solder import *


class BattleLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()

        self.solder = Solder(DIRECTION_RIGHT, SOLDER_UNIT_TYPE_BUBING_RED, (24,24), None)

        self.add(self.solder)

    def on_key_press(self, key, modifiers):
        keystr = pyglet.window.key.symbol_string(key)
        print(keystr)
        if keystr == "RIGHT":
            self.solder.set_direction(DIRECTION_RIGHT)
            self.solder.do(MoveBy((48,0),0.5))
        elif keystr == "UP":
            self.solder.set_direction(DIRECTION_UP)
            self.solder.do(MoveBy((0, 48), 0.5))
        elif keystr == "DOWN":
            self.solder.set_direction(DIRECTION_DOWN)
            self.solder.do(MoveBy((0, -48), 0.5))
        elif keystr == "LEFT":
            self.solder.set_direction(DIRECTION_LEFT)
            self.solder.do(MoveBy((-48, 0), 0.5))
        elif keystr == "K":
            self.solder.atk_ani(self.solder.direction)
            #self.solder.set_direction(0)


class GeneralInfoLayer(Layer):
    def __init__(self, generalmodel):
        super().__init__()
        self.generalmodel = generalmodel

        name = Label(self.generalmodel.name, (30, 60))

        self.add(name)