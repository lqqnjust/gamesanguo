# coding:utf-8

from typing import Tuple

from cocos.text import Label
from cocos.layer import ColorLayer
from sanguo.datamanager.models import GeneralModel


class ArmySprite(ColorLayer):
    """
    战场军队图标
    """
    def __init__(self, general:GeneralModel, grid_x:int, grid_y: int, color:Tuple):
        self.general = general
        self.grid_x = grid_x
        self.grid_y = grid_y

        self.width = 48
        self.height = 48
        super(ArmySprite, self).__init__(color[0], color[1], color[2], color[3], self.width, self.height)

        self.army_type = Label("山", (24, 24),color = (255, 0,0,255))
        self.add(self.army_type)

    def set_grid_position(self, gridx, gridy):
        """
        更新grid 坐标
        :param gridx:
        :param gridy:
        :return:
        """
        self.position = self.width * gridx, self.height * gridy
        self.grid_x = gridx
        self.grid_y = gridy