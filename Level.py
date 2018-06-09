import pygame
from Obstacles import Obstacle

class Level():
	def __init__(self, screen, player):
		self.screen = screen
		self.player = player
		self.level = None
		self.LoadImages()

	def LoadImages(self):
		self.level1 = pygame.image.load("images/Background_Suburb_Road_NN.png").convert()
		# self.level2 = pygame.image.load("images/Background_City_Road.png")
		# self.level3 = pygame.image.load("images/Background_Country_Road.png").convert()
		# self.level4 = pygame.image.load("images/Background_Beach_Road.png").convert()

	def GetLevel(self):
		# The First Level
		# if self.player.score <= 50:
		# 	background = self.level1
		# 	self.level = 1
		# elif self.player.score > 50 and self.player.score <= 100:
		# 	background = self.level2
		# 	self.level = 2
		# elif self.player.score > 100 and self.player.score <= 150:
		# 	background = self.level3
		# 	self.level = 3
		# elif self.player.score > 150:
		# 	background = self.level4
		# 	self.level = 4
		# else:
		# 	background = self.level1
		# 	print('Error in determining level. Loading Level 1')
		background = self.level1
		self.screen.blit(background, (0,0))	
