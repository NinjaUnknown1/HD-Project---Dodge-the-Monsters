import pygame
from Button import Button
from Text import Text

COLORS = {
	'BLACK': (0, 0, 0),
	'GREY' : (128, 128, 128),
	'WHITE': (255, 255, 255),
	'RED'  : (255, 0, 0),
	'ORANGE': (255, 128, 0),
	'GREEN' : (0, 255, 0)
}

button = Button()
gameState = ''

class Menus():
	def __init__(self, screen):
		self.LoadImages()
		self.gameState = 'MainMenu'
		self.text = Text(screen)
		self.screenWidth = 1000
		self.screenHeight = 800
	# Main Menu Screen
	def MainMenu(self, screen):
		background = self.mm
		screen.blit(background, (0,0))
		
		# Draw Buttons
		pygame.draw.rect(screen, COLORS['BLACK'], (200, 150, 600, 100))
		pygame.draw.rect(screen, COLORS['BLACK'], (200, 300, 600, 100))
		pygame.draw.rect(screen, COLORS['BLACK'], (200, 450, 600, 100))
		pygame.draw.rect(screen, COLORS['BLACK'], (200, 600, 600, 100))

		# Check for Hover
		button.ButtonHover(200, 150, 600, 100, COLORS['GREY'], screen)
		button.ButtonHover(200, 300, 600, 100, COLORS['GREY'], screen)
		button.ButtonHover(200, 450, 600, 100, COLORS['GREY'], screen)
		button.ButtonHover(200, 600, 600, 100, COLORS['GREY'], screen)
		
		# Draw Text
		self.text.MainMenu()

		# Check Button Presses
		if button.ButtonPress(200, 150, 600, 100):
			self.gameState = 'PlayGameHuman'
		if button.ButtonPress(200, 300, 600, 100):
			self.gameState = 'PlayGameAI'
		if button.ButtonPress(200, 450, 600, 100):
			self.gameState = 'TuteMenu'
		if button.ButtonPress(200, 600, 600, 100):
			self.gameState = 'Quit' 

	def TutorialMenu(self, screen):
		background = self.tm
		screen.blit(background, (0,0))

		# Draw Button
		pygame.draw.rect(screen, COLORS['BLACK'], (10, 700, 250, 75))

		# Check for Hover
		button.ButtonHover (10, 700, 250, 75, COLORS['GREY'], screen)

		# Draw Text
		self.text.TutorialText()

		# Check Button Presses
		if button.ButtonPress(10, 700, 250, 75):
			self.gameState = 'MainMenu'

	# Will Start AI
	def HighScoresMenu(self, screen):
		background = self.ai
		screen.blit(background, (0,0))

		# Draw Button
		pygame.draw.rect(screen, COLORS['BLACK'], (10, 700, 250, 75))

		# Draw AI Options
		pygame.draw.rect(screen, COLORS['BLACK'], (200, 300, 600, 100))
		pygame.draw.rect(screen, COLORS['BLACK'], (200, 450, 600, 100))

		# Check for Hover
		button.ButtonHover(10, 700, 250, 75, COLORS['GREY'], screen)
		button.ButtonHover(200, 300, 600, 100, COLORS['GREY'], screen)
		button.ButtonHover(200, 450, 600, 100, COLORS['GREY'], screen)

		#DrawText
		self.text.AIText()

		# Check Button Presses
		if button.ButtonPress(10, 700, 250, 75):
			self.gameState = 'MainMenu'

	def EndGameScreen(self, screen, player):
		screen.fill(COLORS['BLACK'])
		self.text.FinalScore(player)
		pygame.display.update()

	def StartGame(self, screen):
		screen.fill(COLORS['RED'])
		self.text.Ready()
		pygame.display.update()
		pygame.time.delay(1000)
		screen.fill(COLORS['ORANGE'])
		self.text.Set()
		pygame.display.update()
		pygame.time.delay(1000)
		screen.fill(COLORS['GREEN'])
		self.text.Go()
		pygame.display.update()
		pygame.time.delay(1000)

	def GetState(self):
		return self.gameState

	def LoadImages(self):
		self.mm = pygame.image.load("images/Background_Blue.png")
		self.tm = pygame.image.load("images/Background_Green.png")
		self.ai = pygame.image.load("images/Background_Red.png")

	def SetState(self, newState):
		self.gameState = newState
		return self.gameState