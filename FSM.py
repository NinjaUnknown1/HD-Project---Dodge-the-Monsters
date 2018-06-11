'''
FSM.py

Distinction Project

This AI runs of a Finite State Machine

By Caitlyn Sims (100593940)
'''
import random
import pygame
import sys
import operator
from math import sqrt
from Player import Player
from Level import Level
from Obstacles import Obstacle
from CollisionChecker import CollisionChecker
from Button import Button
from Text import Text

class FiniteStateMachine():
	def __init__(self, world):
		self.world = world
		self.screen = world.screen
		self.obList = [Obstacle(200,-100, 1), Obstacle(460, -100, 2), Obstacle(720, -100, 3)]
		self.player = world.player
		self.clock = world.clock
		self.text = world.text
		self.collision = CollisionChecker()
		self.level = Level(self.screen, self.player)
		self.distanceRange = 250

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
		monsterCentreX = self.sortedObstacles[0].x + (self.sortedObstacles[0].width/2)

		# If it is closer to left side of the car
		if self.Distance(leftside, self.player.y, monsterCentreX, self.sortedObstacles[0].y) < self.Distance(rightside, self.player.y, monsterCentreX, self.sortedObstacles[0].y):
			# Will be quicker if it moves right
			return 'RIGHT'
		else:
			# Otherwise just move left
			return 'LEFT'

	def CheckRight(self):
		result = None
		for o in self.obList:
			if result == False:
				break
			# There will be something on the right
			if (self.player.x + self.player.width) < o.x and (self.player.x + self.player.width) - o.x < 30 and (self.player.x + self.player.width) - o.x > 0 and (self.player.y - o.y < self.distanceRange/2 or self.player.y + 80 < o.y + o.height):
				result = False
			# Nothing is in the way
			else:
				result = True

		return result


	def CheckLeft(self):
		result = None
		for o in self.obList:
			if result == False:
				break
			# There will be something on the left
			if self.player.x > (o.x + o.width) and self.player.x - (o.x + o.width) < 30 and self.player.x - (o.x + o.width) > 0 and (self.player.y - o.y < self.distanceRange/1.5 or self.player.y + 20 < o.y + o.height):
				return False
			# Nothing is in the way
			else:
				result = True
		return result

	def RunGameFSM(self):
		thisAttempt = 1
		attemptLimit = 30
		screenLeft = 150
		screenRight = 900
		screenBumper = 40
		file = open('Scores.txt', 'w')
		quitB = Button()
		quitT = Text(self.screen)
		
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
				finalScore = 'Attempt %s had a score of %s\n' % (thisAttempt, self.player.score)
				file.write(finalScore)
				thisAttempt += 1
				self.obList = [Obstacle(200,-100, 1), Obstacle(460, -100, 2), Obstacle(720, -100, 3)]
				self.player.ResetPlayer()
				self.player.DrawPlayer(self.screen)
				for o in self.obList:
					o.DrawObstacle(self.screen)

			# Clear the distances and sorted distances
			distances = {}
			sortedDistance = None
			for o in self.obList:
				# Get the distance
				distances[o.index] = self.Distance(self.player.x, self.player.y, o.x, o.y)
			# Sort the distances and returned as tuple
			sortedDistance = sorted(distances.items(), key=lambda x: x[1])
			
			self.sortedObstacles = []
			# Sort the obstacles
			index = [i[0] for i in sortedDistance]
			for i in index:
				for o in self.obList:
					if i == o.index:
						self.sortedObstacles.append(o)	

			# Removes the obstacle from the list if it below a certain point, AI doesn't need to look at it anymore
			for o in self.obList:
				if o.y + o.height > self.player.y + 45:
					self.sortedObstacles.remove(o)

			# Draws the current level
			self.level.GetLevel()
			# The quit button
			pygame.draw.rect(self.screen, (255, 0, 0), (15, 720, 100, 70))
			quitT.FSMQuit()
			if quitB.ButtonPress(15, 720, 100, 70):
				break

			# Checks to see if the user quit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()	

			###   FSM HERE   ###
			if self.sortedObstacles	== []:
				pass	

			# If the obstacle is close and it is near the right side of the car
			elif sortedDistance[0][1] < self.distanceRange and self.WhichWayToMove() == 'LEFT':
				if self.player.x + self.player.width > self.sortedObstacles[0].x - 30 and self.CheckLeft():
					if self.CheckLeft():
						self.player.MoveLeft()
					elif not self.player.CheckLeft() and self.CheckRight():
						self.player.MoveRight()
					else:
						self.player.ReturnStraight()
				else:
					self.player.ReturnStraight()

			# If the obstacle is close and it is near the left side of the car
			elif sortedDistance[0][1] < self.distanceRange and self.WhichWayToMove() == 'RIGHT':
				if self.player.x < self.sortedObstacles[0].x + self.sortedObstacles[0].width + 30:
					if self.CheckRight():
						self.player.MoveRight()
					elif not self.CheckRight() and self.CheckLeft():
						self.player.MoveLeft()
					else:
						self.player.ReturnStraight()
				else:
					self.player.ReturnStraight()

			# If it is near the left side of the screen and there are no monsters in the way to the right
			elif self.player.x < screenLeft + screenBumper and self.CheckRight():
				self.player.MoveRight()
			
			# If it is near the right side of the screen and there are no monsters in the way to the left
			elif self.player.x + self.player.width > screenRight - screenBumper and self.CheckLeft():
				self.player.MoveLeft()
			
			# Otherwise do nothing and return to default position (straight)
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

		# Close the score text file
		file.close()	