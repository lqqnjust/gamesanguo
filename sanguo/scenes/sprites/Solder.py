# coding:utf-8

import pyglet
from cocos.sprite import Sprite

DIRECTION_UP = 0
DIRECTION_RIGHT = 1
DIRECTION_DOWN = 2
DIRECTION_LEFT =3


UNIT_TYPE_BU = 1
UNIT_TYPE_GONG = 2
UNIT_TYPE_QI = 3
UNIT_TYPE_JIANG = 4

UNIT_COLOR_RED = 1
UNIT_COLOR_BLUE = 2


class Solder(Sprite):
    def __init__(self, direction, unit_type,unit_color, unit_level, position, value):
        """

        :param direction:  方向DIRECTION
        :param unit_type:  类型UNIT_TYPE
        :param unit_color:  颜色UNIT_COLOR
        :param position:   位置
        :param soldermodel: 将领数据
        """
        self.direction = direction
        self.unit_type = unit_type
        self.unit_color = unit_color
        self.unit_level = unit_level

        # image_mov = pyglet.resource.image('solders/mov_{}_{}_{}.png'.format(self.unit_type,self.unit_color, unit_level))
        # image_atk = pyglet.resource.image('solders/atk_{}_{}_{}.png'.format(self.unit_type,self.unit_color, unit_level))

        image = pyglet.resource.image('solders/{}_{}_{}.png'.format(self.unit_type, self.unit_color,self.unit_level))

        tileset = pyglet.image.ImageGrid(image, 7, 4, 64, 64)
        # tileset_atk = pyglet.image.ImageGrid(image_atk, 12, 1, 64, 64)

        # move animation
        self.ani_atk_down = pyglet.image.Animation.from_image_sequence(tileset[24:28],0.2,False)
        self.ani_atk_up = pyglet.image.Animation.from_image_sequence(tileset[20:24], 0.2,loop=False)
        self.ani_atk_left = pyglet.image.Animation.from_image_sequence(tileset[16:20], 0.2,loop=False)
        self.ani_atk_right = pyglet.image.Animation.from_image_sequence(tileset[12:16], 0.2,loop=False)

        
        # atk animation
        self.ani_mov_down= pyglet.image.Animation.from_image_sequence(tileset[8:10], 0.2)

        self.ani_mov_up= pyglet.image.Animation.from_image_sequence(tileset[10:12], 0.2)

        self.ani_mov_left= pyglet.image.Animation.from_image_sequence(tileset[4:6], 0.2)

        self.ani_mov_right = pyglet.image.Animation.from_image_sequence(tileset[6:8], 0.2)

        super().__init__(self.ani_atk_down, position=position)
        self.attack_flag = False
        self.set_direction(self.direction)

    def set_direction(self, direction):
        '''
        设置方向
        :param direction:
        :return:
        '''
        self.direction = direction
        if self.direction == DIRECTION_DOWN:
            self.image = self.ani_mov_down
        elif self.direction == DIRECTION_UP:
            self.image = self.ani_mov_up
        elif self.direction == DIRECTION_RIGHT:
            self.image = self.ani_mov_right
        elif self.direction == DIRECTION_LEFT:
            self.image = self.ani_mov_left

    def atk_ani(self, direction):
        '''
        攻击动画
        :param direction:
        :return:
        '''
        self.image_anchor = 32, 32
        if self.direction == DIRECTION_DOWN:
            self.image = self.ani_atk_down
        elif self.direction == DIRECTION_UP:
            self.image = self.ani_atk_up
        elif self.direction == DIRECTION_RIGHT:
            self.image = self.ani_atk_right
        elif self.direction == DIRECTION_LEFT:
            self.image = self.ani_atk_left
        self.attack_flag = True

    def on_animation_end(self):
        '''
        动画播放结束时触发
        :return:
        '''
        if self.attack_flag is True:
            self.image_anchor = 32, 32
            self.set_direction(self.direction)
            self.attack_flag = False



