'''
CollisionChecker.py

By Caitlyn Sims (100593940)
'''
import pygame

class CollisionChecker():
	def CheckCollision(self, olist, player):
		# Set Masks for collision
		player.playerSprite.mask = pygame.mask.from_surface(player.playerSprite.image)
		obstacleMask = []
		for o in olist:
			o.oSprite.mask = pygame.mask.from_surface(o.oSprite.image)
		
		for o in olist:
			if pygame.sprite.collide_mask(player.playerSprite, o.oSprite) != None:
				return True