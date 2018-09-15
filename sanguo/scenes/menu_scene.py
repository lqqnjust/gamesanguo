# coding:utf-8

import os

import pygame

from sanguo.core import Scene

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class MenuScene(Scene):
	def __init__(self):
		super().__init__()

		self.font = pygame.font.Font(os.path.join(BASE_DIR,'resource/fonts/SIMLI.TTF'), 60)
		# self.font = pygame.font.SysFont('楷体', 60)

	def event(self, event):
		super().event(event)

	def update(self, surface, dt):
		#super().update(surface, dt)
		ext_surface = self.font.render(u"123中文", True, (120, 130, 220))
		surface.blit(ext_surface,(30,30))
