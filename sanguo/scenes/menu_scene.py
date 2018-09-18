# coding:utf-8

import os

from sanguo.ui.label import Label
import pygame

from sanguo.core.scene import Scene

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class MenuScene(Scene):
    def __init__(self):
        super().__init__()

        # self.font = pygame.font.Font(os.path.join(BASE_DIR,'resource/fonts/SIMLI.TTF'), 60)
        # # self.font = pygame.font.SysFont('楷体', 60)
        # self.ext_surface = self.font.render(u"123中文", True, (120, 130, 220))
        # self.add(self.ext_surface)
        self.label = Label(os.path.join(BASE_DIR,'resource/fonts/SIMLI.TTF'), u"123中文",60)
        self.label.x = 100
        self.label.y = 100

        self.add(self.label)





