import pygame

class Button():
	# Detects when the mouse hovers over the button 
	def ButtonHover(self, x, y, width, height, color, screen):
		mouse = pygame.mouse.get_pos()
		if mouse[0] >= x and mouse[0] <= (x+width) and mouse[1] >= y and mouse[1] <= (y+height):
			pygame.draw.rect(screen, color, (x, y, width, height))

	# Detects when the mouse clicks on the button
	def ButtonPress(self, x, y, width, height):
		click = pygame.mouse.get_pressed()
		mouse = pygame.mouse.get_pos()
		if click[0] == 1:
			if mouse[0] >= x and mouse[0] <= (x+width) and mouse[1] >= y and mouse[1] <= (y+height):
				return True