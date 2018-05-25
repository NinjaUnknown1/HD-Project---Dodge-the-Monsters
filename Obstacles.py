import pygame
import random

class Obstacle():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = 2

		# Loads the images
		imageSlime = pygame.image.load("images/Slime.png")
		imageTroll = pygame.image.load("images/Troll.png")
		imageCar = pygame.image.load("images/Car.png")
		imageTree = pygame.image.load("images/Tree.png")

		# Create a list for the object an image to choose from
		imageList = [imageSlime, imageTroll, imageCar, imageTree]

		# Randomly pick an image
		self.image = imageList[random.randint(0,3)]

		# Sets width and height depending on image selected
		if self.image == imageSlime:
			self.width = 62
			self.height = 83
		elif self.image == imageTroll:
			self.width = 62
			self.height = 84
		elif self.image == imageCar:
			self.width = 104
			self.height = 83
		elif self.image == imageTree:
			self.width = 104
			self.height = 84

		self.oSprite = pygame.sprite.Sprite()

	def Move(self, player):
		if self.y > 801:
			self.x = random.randint(130, 850)
			self.y = (random.randint(50, 300)) * -1
			player.score += 1
		else:
			self.y += self.speed


	def DrawObstacle(self, screen):
		self.oSprite.image = self.image
		screen.blit(self.oSprite.image, self.MyImage())

	def MyImage(self):
		self.oSprite.rect = self.image.get_rect(x=self.x, y=self.y, w=self.width, h=self.height)
		return self.oSprite.rect