'''
Distinction Project

This AI runs of a Finite State Machine

It also has to check the position of other obstacles to ensure that while moving it won't crash
and look 'dumb'

By Caitlyn Sims (100593940)
'''
import random
import pygame
import sys
from math import sqrt
from Player import Player
from Menus import Menus
from Level import Level
from Obstacles import Obstacle
from Text import Text
from CollisionChecker import CollisionChecker

class FiniteStateMachine():
	def __init__(self, world):
		self.world = world
		self.screen = world.screen
		self.obList = [Obstacle(130,-100)] #, Obstacle(350, -100), Obstacle(645, -100), Obstacle(800, -100)]
		self.player = world.player
		self.clock = pygame.time.Clock()
		self.menu = Menus(self.screen)
		self.text = Text(self.screen)
		self.collision = CollisionChecker()
		self.level = Level(self.screen, self.player)

	def Distance(self, v1x, v1y, v2x, v2y):
		''' the distance between self and v2 vector '''
		dx = v2x - v1x
		dy = v2y - v1y
		return sqrt(dx*dx + dy*dy)

	def GetSprites(self):
		self.allObstacles = pygame.sprite.Group()
		for o in self.obList:
			self.allObstacles.add(o.oSprite)

	def RunGameFSM(self):
		self.GetSprites()
		self.player.DrawPlayer(self.screen)
		for o in self.obList:
			o.DrawObstacle(self.screen)
		self.menu.StartGame(self.screen)
		while not self.collision.CheckCollision(self.obList, self.player):
			distances = []
			for o in self.obList:
				# Get the distance
				distances.append(self.Distance(self.player.x, self.player.y, o.x, o.y))
			print(distances)
			print('break')
			
			self.level.GetLevel(self.obList)

			# Checks to see if the user quit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()	

			# FSM HERE
			if distances[0] < 150:
				self.player.MoveLeft()
			else:
				self.player.ReturnStraight()

			# Draw the player
			self.player.DrawPlayer(self.screen)
			
			# Handles Movement and Drawing of Obstalces	
			for o in self.obList:
				o.Move(self.player)
				o.DrawObstacle(self.screen)	

			self.text.InGameScore(self.player)
			# Refresh Rate
			self.clock.tick(120)

			# Update the Screen
			pygame.display.update()