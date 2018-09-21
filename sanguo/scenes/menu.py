# coding:utf-8


from cocos.menu import BaseMenuItem
from cocos.sprite import Sprite

import pyglet
from pyglet import gl
import pyglet.graphics


class IconMenuItem (BaseMenuItem):
    """A menu item that shows a label. """
    def __init__(self, label, callback_func, *args, **kwargs):
        """Creates a new menu item

        :Parameters:
            `label` : string
                The label the of the menu item
            `callback_func` : function
                The callback function
        """
        self.label = label

        super(IconMenuItem, self).__init__(callback_func, *args, **kwargs)

    def get_item_width(self):
        return self.item.content_width

    def get_item_height(self):
        return self.item.content_height

    def generateWidgets(self, pos_x, pos_y, font_item, font_item_selected):
        font_item['x'] = int(pos_x)
        font_item['y'] = int(pos_y)
        font_item['text'] = self.label
        self.item = pyglet.text.Label(**font_item)

        position = int(pos_x) - self.get_item_width() /2 - 24, int(pos_y) - self.get_item_height() /2 + 10
        self.item_icon = Sprite("arrow_right.png", anchor=(0,0), position=position)

    def draw(self):
        gl.glPushMatrix()
        self.transform()
        self.item.draw()
        if self.is_selected:
            self.item_icon.draw()

        gl.glPopMatrix()