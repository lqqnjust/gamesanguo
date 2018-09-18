# coding:utf-8

import pygame


class View(object):
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.size = (self.width, self.height)

        self.surface = self.surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)

        self.children = []
        self.x = 0
        self.y = 0
        self.background_color = None

    def update(self, dt):
        for child in self.children:
            child.update(dt)

    def draw(self):
        if self.background_color is not None:
            self.surface.fill(self.background_color, rect=pygame.Rect((self.x, self.y), self.size))

        for child in self.children:
            child.draw()

    def add(self, node):
        self.children.append(node)