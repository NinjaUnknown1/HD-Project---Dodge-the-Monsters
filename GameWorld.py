import pygame
import random
import sys
import os
from Player import Player
from Menus import Menus
from Level import Level
from Obstacles import Obstacle
from Text import Text

# Set a specific location for the window to open
windowX = 20
windowY = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (windowX, windowY)

pygame.init()

class World():
	# Initialisation
	def __init__(self):
		#self.player = Player()
		self.ScreenSetup()
		self.menu = Menus(self.screen)
		self.text = Text(self.screen)
		self.state = ''
		self.playing = True
		self.clock = pygame.time.Clock()
		self.fps = 120
		self.obstacleSprites = []
		self.obList = []

	def RunningStatus(self):
		if self.state == 'Quit':
			return False
		else:
			return True

	# Sets up the screen
	def ScreenSetup(self):
		width = 1000
		height = 800

		self.screen = pygame.display.set_mode((width, height), pygame.HWSURFACE|pygame.DOUBLEBUF)
		pygame.display.set_caption('Dodge The Monsters 3')	

	# Draws all the game objects
	def GameStatus(self):
		self.DetermineGameState()
		if self.state == 'MainMenu':
			self.menu.MainMenu(self.screen)
		elif self.state == 'TuteMenu':
			self.menu.TutorialMenu(self.screen)
		elif self.state == 'PlayGameAI':
			self.menu.HighScoresMenu(self.screen)
		elif self.state == 'PlayGameHuman':
			self.player = Player('HUMAN')
			self.level = Level(self.screen, self.player)
			self.RunGame()

	def DetermineGameState(self):
		self.state = self.menu.GetState()

	def LoadObstacles(self):
		self.obList = [Obstacle(130,-100), Obstacle(350, -100), Obstacle(645, -100), Obstacle(800, -100)]

	# Handles the left and right movement of the player
	def HandlePlayerMovement(self):
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			self.player.MoveLeft()
		if pygame.key.get_pressed()[pygame.K_RIGHT]:
			self.player.MoveRight()
		if not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_RIGHT]:
			self.player.ReturnStraight()

	def GetSprites(self):
		self.allObstacles = pygame.sprite.Group()
		for o in self.obList:
			self.allObstacles.add(o.oSprite)


	def CheckCollision(self):
		# for o in self.obList:
		# 	collision = o.MyImage().colliderect(self.player.MyImage())
		# 	if collision == True:
		# 		return True
		# return False

		# Set Masks for collision
		self.player.playerSprite.mask = pygame.mask.from_surface(self.player.playerSprite.image)
		obstacleMask = []
		for o in self.obList:
			o.oSprite.mask = pygame.mask.from_surface(o.oSprite.image)
		
		for o in self.obList:
			if pygame.sprite.collide_mask(self.player.playerSprite, o.oSprite) != None:
				#print('Collision')
				return True


	def RunGame(self):
		self.LoadObstacles()
		self.GetSprites()
		self.player.DrawPlayer(self.screen)
		for o in self.obList:
			o.DrawObstacle(self.screen)
		while self.playing and not self.CheckCollision():
			self.screen.fill((255,255,255))
			# Get the current Level
			self.level.GetLevel()

			# Checks to see if the user quit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()	

			# Player Movement and Drawing
			self.HandlePlayerMovement()
			self.player.DrawPlayer(self.screen)

			
			# Handles Movement and Drawing of Obstalces	
			for o in self.obList:
				o.Move(self.player)
				o.DrawObstacle(self.screen)	

			self.text.InGameScore(self.player)
			# Refresh Rate
			self.clock.tick(120)
			print(self.clock.get_fps())
			
			# Update the Screen
			pygame.display.update()

		pygame.time.delay(1000)
		self.menu.EndGameScreen(self.screen, self.player)
		pygame.time.delay(5000)
		self.menu.SetState('MainMenu')