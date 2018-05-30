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
from Level import Level
from Obstacles import Obstacle
from CollisionChecker import CollisionChecker

class FiniteStateMachine():
	def __init__(self, world):
		self.world = world
		self.screen = world.screen
		self.obList = [Obstacle(750,-100)] #, Obstacle(350, -100), Obstacle(645, -100), Obstacle(800, -100)]
		self.player = world.player
		self.clock = world.clock
		self.text = world.text
		self.collision = CollisionChecker()
		self.level = Level(self.screen, self.player)
		self.distanceRange = 150

		self.player.x = 850

	def Distance(self, v1x, v1y, v2x, v2y):
		''' the distance between self and v2 vector '''
		dx = v2x - v1x
		dy = v2y - v1y
		return sqrt(dx*dx + dy*dy)

	def GetSprites(self):
		self.allObstacles = pygame.sprite.Group()
		for o in self.obList:
			self.allObstacles.add(o.oSprite)

	def WhichWayToMove(self):
		leftside = self.player.x
		rightside = self.player.x + self.player.width
		monsterCentreX = self.obList[0].x + (self.obList[0].width/2)

		# If it is closer to left side of the car
		if self.Distance(leftside, self.player.y, monsterCentreX, self.obList[0].y) < self.Distance(rightside, self.player.y, monsterCentreX, self.obList[0].y):
			# Will be quicker if it moves right
			return 'RIGHT'
		else:
			# Otherwise just move left
			return 'LEFT'

	def CheckRight(self):
		# There will be something on the right
		if self.player.x + (self.player.width/2) < self.obList[0].x and self.player.y - self.obList[0].y < self.distanceRange:
			print('on right')
			return False
		print('all clear')
		return True

	def CheckLeft(self):
		# There will be something on the left
		if self.player.x + (self.player.width/2) > self.obList[0].x and self.player.y - self.obList[0].y < self.distanceRange:
			print('on left')
			return False
		print('all clear (l)')
		return True

	def RunGameFSM(self):
		thisAttempt = 1
		attemptLimit = 1
		screenLeft = 130
		screenRight = 900
		screenBumper = 40
		
		# Initial Game Setup
		self.GetSprites()
		self.player.DrawPlayer(self.screen)
		for o in self.obList:
			o.DrawObstacle(self.screen)		
		
		# While the AI still has attempts left
		while thisAttempt <= attemptLimit:
			# Checks for collision
			# If one occurs then reset the game and change attempt number
			if self.collision.CheckCollision(self.obList, self.player):
				thisAttempt += 1
				# Print the final score
				print(' THE FINAL SCORE WAS: ', self.player.score)
				self.obList = [Obstacle(500,-100)]
				self.player.x = 450
				self.player.DrawPlayer(self.screen)
				for o in self.obList:
					o.DrawObstacle(self.screen)
				self.player.score = 0

			distances = []
			for o in self.obList:
				# Get the distance
				distances.append(self.Distance(self.player.x, self.player.y, o.x, o.y))
			
			self.level.GetLevel(self.obList)

			# Checks to see if the user quit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()	

			# FSM HERE

			# IF its underneath the player, ignore it for the minute
			if self.player.y < self.obList[0].y:
				self.player.ReturnStraight()
			# If it is near the left side of the screen and there are no monsters in the way to the right
			elif self.player.x < screenLeft + screenBumper and self.CheckRight():
				self.player.MoveRight()
			# If it is near the right side of the screen and there are no monsters in the way to the left
			elif self.player.x + self.player.width > screenRight - screenBumper and self.CheckLeft():
				self.player.MoveLeft()
			# If the obstacle is close and it is near the right side of the car
			elif distances[0] < self.distanceRange and self.WhichWayToMove() == 'LEFT':
				if self.player.x + self.player.width > self.obList[0].x - 30:
					self.player.MoveLeft()
				elif self.player.x + self.player.width > self.obList[0].x - 30:
					self.player.MoveRight()
				else:
					self.player.ReturnStraight()
			# If the obstacle is close and it is near the right side of the car
			elif distances[0] < self.distanceRange and self.WhichWayToMove() == 'RIGHT':
				if self.player.x < self.obList[0].x + self.obList[0].width + 30:
					self.player.MoveRight()
				else:
					self.player.ReturnStraight()
			else:
				self.player.ReturnStraight()

			# Draw the player
			self.player.DrawPlayer(self.screen)
			
			# Handles Movement and Drawing of Obstalces	
			for o in self.obList:
				o.Move(self.player)
				o.DrawObstacle(self.screen)	

			# Print the score to the screen
			self.text.InGameScore(self.player)
			# Print the attempt number to the screen
			self.text.AttemptNumber(thisAttempt, attemptLimit)
			
			# Refresh Rate
			self.clock.tick(120)

			# Update the Screen
			pygame.display.update()		