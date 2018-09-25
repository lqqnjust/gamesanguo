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

        image_mov = pyglet.resource.image('solders/mov_{}_{}_{}.png'.format(self.unit_type,self.unit_color, unit_level))
        image_atk = pyglet.resource.image('solders/atk_{}_{}_{}.png'.format(self.unit_type,self.unit_color, unit_level))

        tileset = pyglet.image.ImageGrid(image_mov, 11, 1, 48, 48)
        tileset_atk = pyglet.image.ImageGrid(image_atk, 12, 1, 64, 64)

        # move animation
        self.ani_down = pyglet.image.Animation.from_image_sequence([tileset[9], tileset[4], tileset[10], tileset[4]],
                                                                   0.2)
        self.ani_left = pyglet.image.Animation.from_image_sequence(
            [tileset[5], tileset[2],
             tileset[6], tileset[2]], 0.2)

        self.ani_right = self.ani_left.get_transform(flip_x=True)

        self.ani_up = pyglet.image.Animation.from_image_sequence(
            [tileset[7], tileset[3],
             tileset[8], tileset[3]], 0.2)

        # atk animation
        self.ani_atk_down= pyglet.image.Animation.from_image_sequence(
            [tileset_atk[11], tileset_atk[10],
             tileset_atk[9], tileset_atk[8]], 0.2,loop=False)

        self.ani_atk_up= pyglet.image.Animation.from_image_sequence(
            [tileset_atk[7], tileset_atk[6],
             tileset_atk[5],tileset_atk[4]], 0.2,loop=False)

        self.ani_atk_left= pyglet.image.Animation.from_image_sequence(
            [tileset_atk[3], tileset_atk[2],
             tileset_atk[1],tileset_atk[0]], 0.2,loop=False)

        self.ani_atk_right = self.ani_atk_left.get_transform(flip_x=True)

        super().__init__(self.ani_up, position=position)
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
            self.image = self.ani_down
        elif self.direction == DIRECTION_UP:
            self.image = self.ani_up
        elif self.direction == DIRECTION_RIGHT:
            self.image = self.ani_right
        elif self.direction == DIRECTION_LEFT:
            self.image = self.ani_left

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
            self.image_anchor = 24, 24
            self.set_direction(self.direction)
            self.attack_flag = False



