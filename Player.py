import pygame

class Player():
	# PLayer initialisation
	def __init__(self, myType, x=450, y=700):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.score = 0
		self.speed = 2
		self.name = ''
		self.type = myType
		self.direction = 'Straight'
		self.width = 97
		self.height = 97
		self.playerSprite = pygame.sprite.Sprite()

	def MoveLeft(self):
		if self.x > 135:
			self.x -= self.speed
			self.direction = 'Left'
		else:
			self.direction = 'Straight'

	def MoveRight(self):
		if (45 + self.x) < 900:
			self.x += self.speed
			self.direction = 'Right'
		else:
			self.direction = 'Straight'
	
	def ReturnStraight(self):
		self.direction = 'Straight'

	def PlayerSprites(self):
		left_sprite = pygame.sprite.Sprite()
		left_sprite.image = pygame.image.load("images/HUMAN_" + self.direction + ".png")
		left_sprite.rect = True

	def DrawPlayer(self, screen):
		if self.type == 'AI':
			self.image = pygame.image.load("images/AI_" + self.direction + ".png")
		elif self.type == 'HUMAN':
			self.image = pygame.image.load("images/HUMAN_" + self.direction + ".png")
		else:
			self.image = pygame.image.load("images/HUMAN_" + self.direction + ".png")
			print('Error in player type...')
		self.playerSprite.image = self.image
		screen.blit(self.playerSprite.image, self.MyImage())

	def MyImage(self):
		self.playerSprite.rect = self.image.get_rect(x=self.x, y=self.y, w=self.width, h=self.height)
		return self.playerSprite.rect

	def ResetPlayer(self):
		self.x = 450
		self.y = 700
		self.score = 0
