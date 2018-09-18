# coding:utf-8

import pygame

from sanguo.core.view import View


class Label(View):
    def __init__(self, fontname, text, size):
        View.__init__(self, 300, 200)
        # 'resource/fonts/SIMLI.TTF')
        self.font = pygame.font.Font(fontname, size)
        self.text = text
        self.text_surface = self.font.render(text, True, (120, 130, 220))

    def draw(self):
        self.surface.blit(self.text_surface, (self.x, self.y))

