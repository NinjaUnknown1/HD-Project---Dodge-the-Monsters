'''
GameLogic.py

Game loop of Dodge the Monsters

By Caitlyn Sims (100593940)

'''

import pygame
import sys

class GameLogic():
	def __init__(self, world, screen, level, text):
		self.player = world.player
		#self.obList = world.obList
		self.level  = level
		self.screen = screen
		self.text = text

	def TheGame(self, obList):
		# Make sure the obList stays updated for the human player
		self.obList = obList
		self.level.GetLevel()

		# Checks to see if the user quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()	

		# Player Drawing
		self.player.DrawPlayer(self.screen)
		
		# Handles Movement and Drawing of Obstalces	
		for o in self.obList:
			o.Move(self.player)
			o.DrawObstacle(self.screen)	

		self.text.InGameScore(self.player)	
		# Update the Screen
		pygame.display.update()