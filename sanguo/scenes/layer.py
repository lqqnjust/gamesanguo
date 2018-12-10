# coding:utf-8

import pyglet

from cocos.layer import Layer
from cocos.actions import MoveBy
from cocos.text import Label
from cocos.tiles import load

from .sprites.Solder import *


class BattleLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()

        self.solder1 = Solder(1,1, 1,1, (99,99), 100)
        self.solder2 = Solder(DIRECTION_LEFT,1, 2,1, (170,99), 100)

        # tmxmap = load('water.tmx')
        # layer = tmxmap['layer1']
        # layer.set_view(0, 0, 800, 600)
        # self.add(layer)
        self.add(self.solder1)
        self.add(self.solder2)

    def on_key_press(self, key, modifiers):
        keystr = pyglet.window.key.symbol_string(key)
        print(keystr)
        if keystr == "RIGHT":
            self.solder1.set_direction(DIRECTION_RIGHT)
            self.solder1.do(MoveBy((48,0),0.5))
        elif keystr == "UP":
            self.solder1.set_direction(DIRECTION_UP)
            self.solder1.do(MoveBy((0, 48), 0.5))
        elif keystr == "DOWN":
            self.solder1.set_direction(DIRECTION_DOWN)
            self.solder1.do(MoveBy((0, -48), 0.5))
        elif keystr == "LEFT":
            self.solder1.set_direction(DIRECTION_LEFT)
            self.solder1.do(MoveBy((-48, 0), 0.5))
        elif keystr == "K":
            self.solder1.atk_ani(self.solder.direction)
            #self.solder.set_direction(0)


class GeneralInfoLayer(Layer):
    def __init__(self, generalmodel):
        super().__init__()
        self.generalmodel = generalmodel

        name = Label(self.generalmodel.name, (30, 60))

        self.add(name)
