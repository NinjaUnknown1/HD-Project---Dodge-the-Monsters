import pygame
from Obstacles import Obstacle

class Level():
	def __init__(self, screen, player):
		self.screen = screen
		self.player = player
		self.LoadImages()

	def LoadImages(self):
		self.level1 = pygame.image.load("images/Background_Suburb_Road.png").convert()
		self.level2 = pygame.image.load("images/Background_City_Road.png")
		self.level3 = pygame.image.load("images/Background_Country_Road.png").convert()
		self.level4 = pygame.image.load("images/Background_Beach_Road.png").convert()

	def GetLevel(self):
		# The First Level
		if self.player.score <= 10:
			background = self.level1
		elif self.player.score > 10 and self.player.score <= 20:
			background = self.level2
		elif self.player.score > 20 and self.player.score <= 30:
			background = self.level3
		elif self.player.score > 30:
			background = self.level4
		else:
			background = self.level1
			print('Error in determining level. Loading Level 1')
		self.screen.blit(background, (0,0))	