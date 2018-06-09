'''

The game loop for the neural network

'''
import pygame
from GameLogic import GameLogic
from Obstacles import Obstacle
from Level import Level
from Text import Text
from CollisionChecker import CollisionChecker
import NeuralNetwork_A1

class NNRunGame():
	def __init__(self, world, screen):
		self.world = world
		self.player = world.player
		self.screen = screen
		self.level = Level(screen, world.player)
		self.text = Text(screen)
		self.collision = CollisionChecker()
		self.obList = [] #[Obstacle(130,-100, 1), Obstacle(350, -100, 2), Obstacle(645, -100, 3), Obstacle(800, -100, 4)]

	def GetSprites(self):
		self.allObstacles = pygame.sprite.Group()
		for o in self.obList:
			self.allObstacles.add(o.oSprite)

	def HandlePlayerMovement(self):
		if self.player.type == 'AI':
			if pygame.key.get_pressed()[pygame.K_LEFT]:
				self.player.MoveLeft()
			if pygame.key.get_pressed()[pygame.K_RIGHT]:
				self.player.MoveRight()
			if not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_RIGHT]:
				self.player.ReturnStraight()

	def NNGame(self):
		thisAttempt = 1
		attemptLimit = 3
		file = open('ScoresNN.txt', 'w')
		game = GameLogic(self.world, self.screen, self.level, self.text)
		network = NeuralNetwork_A1

		self.player.speed = 20
		self.GetSprites()
		self.player.DrawPlayer(self.screen)
		for o in self.obList:
			o.DrawObstacle(self.screen)		
		
		# While the AI still has attempts left
		while thisAttempt <= attemptLimit:
			network.RunNN(self.player)
			if self.collision.CheckCollision(self.obList, self.player):
				finalScore = 'Attempt %s had a score of %s\n' % (thisAttempt, self.player.score)
				file.write(finalScore)
				thisAttempt += 1
				self.obList = [Obstacle(130,-100, 1), Obstacle(350, -100, 2), Obstacle(645, -100, 3), Obstacle(800, -100, 4)]
				self.player.ResetPlayer()
				self.player.DrawPlayer(self.screen)
				for o in self.obList:
					o.DrawObstacle(self.screen)
			self.HandlePlayerMovement()
			game.TheGame(self.obList)

		file.close()
