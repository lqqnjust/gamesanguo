# coding:utf-8

import os
import logging

from cocos.scene import Scene
from cocos.menu import Menu

from .menu import IconMenuItem


logger = logging.getLogger(__name__)


class MenuScene(Scene):
    def __init__(self, *children):
        super().__init__(*children)


        l = []
        # l.append(MenuItem(u"开始", self.on_new_game))
        # l.append(MenuItem(u"继续", self.on_continue))
        l.append(IconMenuItem(u'开始',self.on_new_game))
        l.append(IconMenuItem(u'继续', self.on_continue))

        self.menu = Menu()
        # self.menu.font_item['font_name'] = 'LiSu'
        # self.menu.font_item_selected['font_name']= 'LiSu'
        self.menu.font_item['font_size'] = 24
        self.menu.create_menu(l)
        self.add(self.menu)

    def on_new_game(self):
        logger.info("new game")

    def on_continue(self):
        logger.info("continue game")


