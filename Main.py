'''
Main.py

By Caitlyn Sims (100593940)
'''
import pygame
import sys

from GameWorld import World

if __name__ == '__main__':
	# World Creation
	world = World()
	runGame = True
	
	# Game Loop
	while runGame:
		runGame = world.RunningStatus()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or runGame == False:
				pygame.quit()
				sys.exit()
		
		world.GameStatus()
		pygame.display.update()