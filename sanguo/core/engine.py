# coding:utf-8

import sys
import pygame
from pygame.locals import *


class Game(object):
	def __init__(self, width, height, fps, title):
		pygame.init()
		pygame.font.init()
		self.surface = pygame.display.set_mode((width, height))

		self.fps = fps
		self.running = True
		self.black = Color(0, 0, 0, 255)
		pygame.display.set_caption(title)

		self.load_resource()

		self.scene = None

	def run(self):
		clock = pygame.time.Clock()
		while self.running:
			clock.tick(self.fps)

			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit(0)
				else:
					self.scene.event(event)

			self.surface.fill(self.black)
			self.scene.update(self.surface, clock.get_time())

			pygame.display.flip()

	def load_resource(self):
		pass

	def set_scene(self, scene):
		self.scene = scene
