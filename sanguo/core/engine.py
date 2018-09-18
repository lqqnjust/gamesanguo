# coding:utf-8

import sys
import pygame
from pygame.locals import *


class Game(object):
    def __init__(self, width=800, height=600, fps=60, title=""):
        pygame.init()

        self.width = width
        self.height = height

        self.fps = fps
        self.title = title
        self.window_size = (self.width, self.height)

        self.scene = None
        self.scenes = []
        self.window_surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(title)

    def run(self, scene):
        self.scene = scene
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)


            self.scene.update(clock.get_time())
            self.scene.draw()
            self.window_surface.blit(self.scene.surface, (0, 0))

            pygame.display.flip()

    def place(self, scene):
        self.scene = scene

    def push(self, scene):
        self.scenes.append(self.scene)
        self.scene = scene

    def pop(self):
        self.scene = self.scenes.pop()


