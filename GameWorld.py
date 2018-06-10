import pygame
import random
import sys
import os
from Player import Player
from Menus import Menus
from Level import Level
from Obstacles import Obstacle
from Text import Text
from FSM import FiniteStateMachine
from CollisionChecker import CollisionChecker
from GameLogic import GameLogic


# Set a specific location for the window to open
windowX = 20
windowY = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (windowX, windowY)



#pygame.init()

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
		self.collision = CollisionChecker()

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
		elif self.state == 'SelectAI':
			self.menu.SelectAI(self.screen)
		elif self.state == 'FSM':
			self.player = Player('AI')
			self.fsm = FiniteStateMachine(self)
			self.fsm.RunGameFSM()
			self.menu.SetState('MainMenu')
		elif self.state == 'PlayGameHuman':
			self.player = Player('HUMAN')
			self.level = Level(self.screen, self.player)
			self.RunGameHuman()

	def DetermineGameState(self):
		self.state = self.menu.GetState()

	def LoadObstacles(self):
		self.obList = [Obstacle(130,-100, 1), Obstacle(350, -100, 2), Obstacle(645, -100, 3), Obstacle(800, -100, 4)]

	# Handles the left and right movement of the player
	def HandlePlayerMovement(self):
		if self.player.type == 'HUMAN':
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

	def AddObstacle(self):
		if self.level.level == 2 and len(self.obList) == 4:
			self.obList.append(Obstacle(random.randint(130, 850), (random.randint(50, 300)), 5))
		elif self.level.level == 3 and len(self.obList) == 5:
			self.obList.append(Obstacle(random.randint(130, 850), (random.randint(50, 300)), 6))
		elif self.level.level == 4 and len(self.obList) == 6:
			self.obList.append(Obstacle(random.randint(130, 850), (random.randint(50, 300)), 7))

	def RunGameHuman(self):
		self.LoadObstacles()
		self.game = GameLogic(self, self.screen, self.level, self.text)
		self.GetSprites()
		self.player.DrawPlayer(self.screen)
		for o in self.obList:
			o.DrawObstacle(self.screen)
		self.menu.StartGame(self.screen)
		while self.playing and not self.collision.CheckCollision(self.obList, self.player):
			# Get the player movement
			self.HandlePlayerMovement()
			# Add other Obstacles
			self.AddObstacle()
			# Run the game logic
			self.game.TheGame(self.obList)		
			# Refresh Rate
			self.clock.tick(120)

		pygame.time.delay(1000)
		self.menu.EndGameScreen(self.screen, self.player)
		pygame.time.delay(5000)
		self.menu.SetState('MainMenu')