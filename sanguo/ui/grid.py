# coding:utf-8


# 无选择
GRID_SELECT_NO = 0
# 单选
GRID_SELECT_SINGLE = 1
# 多选
GRID_SELECT_MULTI = 2


class GridUI(object):
    """
    显示人物列表，并控制显示
    """
    def __init__(self, surface, fields):
        self.select = GRID_SELECT_NO
        self.surface = surface
        self.generals = None

    def set_generals(self, generals):
        self.generals = generals



