# coding:utf-8

import pyglet
from cocos.sprite import Sprite

DIRECTION_UP = 0
DIRECTION_RIGHT = 1
DIRECTION_DOWN = 2
DIRECTION_LEFT =3



class Solder(object):
    def __init__(self, direction, unit_type, color, position):
        self.direction = direction
        self.unit_type = unit_type
        self.color = color

        image = pyglet.resource.image('Unit_mov_1-1.png')

        tileset = pyglet.image.ImageGrid(image, 11, 1, 48, 48)

        self.ani_down = pyglet.image.Animation.from_image_sequence([tileset[9], tileset[4], tileset[10], tileset[4]],
                                                                   0.2)
        self.ani_left = pyglet.image.Animation.from_image_sequence(
            [tileset[5], tileset[2],
             tileset[6], tileset[2]], 0.2)

        self.ani_right = pyglet.image.Animation.from_image_sequence(
            [tileset[5].get_transform(flip_x=True), tileset[2].get_transform(flip_x=True),
             tileset[6].get_transform(flip_x=True), tileset[2].get_transform(flip_x=True)], 0.2)

        self.ani_up = pyglet.image.Animation.from_image_sequence(
            [tileset[7], tileset[3],
             tileset[8], tileset[3]], 0.2)

        self.position = position
        self.sprite = Sprite(self.ani_up, position)
        self.set_direction(direction)

    def set_direction(self, direction):
        self.direction = direction
        if self.direction == DIRECTION_DOWN:
            self.sprite.image = self.ani_down
        elif self.direction == DIRECTION_UP:
            self.sprite.image = self.ani_up
        elif self.direction == DIRECTION_RIGHT:
            self.sprite.image = self.ani_right
        elif self.direction == DIRECTION_LEFT:
            self.sprite.image = self.ani_left



