import pygame

COLORS = {
	'BLACK'	 : (0, 0, 0),
	'GREY' 	 : (128, 128, 128),
	'WHITE'	 : (255, 255, 255),
	'ORANGE' : (255, 128, 0),
	'BLUE' 	 : (51, 153, 255),
	'RED'	 : (255, 51, 51)
}

class Text():
	def __init__(self, screen):
		self.screen = screen
		pygame.font.init()
		self.LoadFonts()
		self.screenWidth = 1000
		self.screenHeight = 800

	def LoadFonts(self):
		self.mainHeading = pygame.font.Font("fonts/planetbe.ttf", 70)
		self.headings = pygame.font.Font("fonts/planetbe.ttf", 50)
		self.genText = pygame.font.Font("fonts/ITCKRIST.TTF", 26)
		self.scoreText = pygame.font.Font("fonts/ITCKRIST.TTF", 30)
		self.scoreText.set_bold(True)
		self.mainButText = pygame.font.Font("fonts/Life is goofy.ttf", 100)
		self.buttonText = pygame.font.Font("fonts/Life is goofy.ttf", 60)
		self.aiButton = pygame.font.Font("fonts/Life is goofy.ttf", 80)
		self.dead = pygame.font.Font("fonts/Fiendish.ttf", 60)
		self.lvlDisplay = pygame.font.Font("fonts/Blazed.ttf", 100)
		self.ready = pygame.font.Font("fonts/data-latin.ttf", 120)
		self.set = pygame.font.Font("fonts/data-latin.ttf", 120)
		self.go = pygame.font.Font("fonts/data-latin.ttf", 120)

	def MainMenu(self):
		# Get the text
		mHeading = self.mainHeading.render('Dodge The Monsters', 1, COLORS['ORANGE'])
		mHeadingWidth = mHeading.get_width()
		b1 = self.mainButText.render('Play Human Mode', 1, COLORS['WHITE'])
		b1Width = b1.get_width()
		b2 = self.mainButText.render('Play AI Mode', 1, COLORS['WHITE'])
		b2Width = b2.get_width()
		b3 = self.mainButText.render('How To Play', 1, COLORS['WHITE'])
		b3Width = b3.get_width()
		b4 = self.mainButText.render('Quit', 1, COLORS['WHITE'])
		b4Width = b4.get_width()

		# Write the text to the screen
		# Draw the heading in the centre
		self.screen.blit(mHeading, (self.screenWidth/2 - mHeadingWidth/2, 20))
		self.screen.blit(b1, (self.screenWidth/2 - b1Width/2, 170))
		self.screen.blit(b2, (self.screenWidth/2 - b2Width/2, 320))
		self.screen.blit(b3, (self.screenWidth/2 - b3Width/2, 470))
		self.screen.blit(b4, (self.screenWidth/2 - b4Width/2, 620))

	def TutorialText(self):
		tHeading = self.headings.render('Welcome to Dodge the Monsters!', 1, COLORS['ORANGE'])
		tHeadingWidth = tHeading.get_width()
		t1 = self.genText.render('In this game, your aim is to dodge the monsters and obstacles on the road.', 1, COLORS['BLACK'])
		t2 = self.genText.render('Use the left arrow key to move your car left.', 1, COLORS['BLACK'])
		t3 = self.genText.render('Use the right arrow key to move your car right.', 1, COLORS['BLACK'])
		t4 = self.genText.render('Your score is located in the top left corner of the game screen.', 1, COLORS['BLACK'])
		t5 = self.genText.render('Every time you drive past a monster or obstacle, you get one point.', 1, COLORS['BLACK'])
		t6 = self.genText.render('After a certain score is reached, the game will stop and you will', 1, COLORS['BLACK'])
		t7 = self.genText.render('advance to the next level of the game.', 1, COLORS['BLACK'])
		t8 = self.genText.render('Have fun playing!!! :-)', 1, COLORS['BLACK'])
		b1 = self.buttonText.render('<-- Back', 1, COLORS['WHITE'])

		self.screen.blit(tHeading, (self.screenWidth/2 - tHeadingWidth/2, 15))
		self.screen.blit(t1, (10, 150))
		self.screen.blit(t2, (10, 190))
		self.screen.blit(t3, (10, 230))
		self.screen.blit(t4, (10, 270))
		self.screen.blit(t5, (10, 310))
		self.screen.blit(t6, (10, 350))
		self.screen.blit(t7, (10, 390))
		self.screen.blit(t8, (10, 470))
		self.screen.blit(b1, (45, 720))

	def AIText(self):
		aiHeading = self.mainHeading.render('Select an AI Mode', 1, COLORS['WHITE'])
		backButton = self.buttonText.render('<-- Back', 1, COLORS['WHITE'])
		distinction = self.aiButton.render('Finite State Machine', 1, COLORS['WHITE'])
		hd = self.aiButton.render('Neural Network', 1, COLORS['WHITE'])

		headWidth = aiHeading.get_width()
		distWidth = distinction.get_width()
		hdWidth = hd.get_width()
		
		self.screen.blit(aiHeading, (self.screenWidth/2 - headWidth/2, 60))
		self.screen.blit(backButton, (25, 720))
		self.screen.blit(distinction, (self.screenWidth/2 - distWidth/2, 320))
		self.screen.blit(hd, (self.screenWidth/2 - hdWidth/2, 470))

	def InGameScore(self, player):
		cScore = self.scoreText.render('Score : %s' % player.score, 1, COLORS['RED'])
		self.screen.blit(cScore, (25, 25))

	def AttemptNumber(self, thisAttempt, attemptLimit):
		aNum = self.scoreText.render('Attempt %s / %s' % (thisAttempt, attemptLimit), 1, COLORS['RED'])
		self.screen.blit(aNum, (25, 75))

	def Ready(self):
		ready = self.ready.render('READY', 1, COLORS['WHITE'])
		readyWidth = ready.get_width()
		readyHeight = ready.get_height()
		self.screen.blit(ready, (self.screenWidth/2 - readyWidth/2, self.screenHeight/2 - readyHeight/2))

	def Set(self):
		getset = self.set.render('SET', 1, COLORS['WHITE'])
		setWidth = getset.get_width()
		setHeight = getset.get_height()
		self.screen.blit(getset, (self.screenWidth/2 - setWidth/2, self.screenHeight/2 - setHeight/2))

	def Go(self):
		go = self.go.render('GO', 1, COLORS['WHITE'])
		goWidth = go.get_width()
		goHeight = go.get_height()
		self.screen.blit(go, (self.screenWidth/2 - goWidth/2, self.screenHeight/2 - goHeight/2))

	def FinalScore(self, player):
		m1 = self.dead.render('You Died', 1, COLORS['RED'])
		m1Width = m1.get_width()
		m2 = self.dead.render('Final Score: %s' % player.score, 1, COLORS['RED'])
		m2Width = m2.get_width()

		self.screen.blit(m1, (self.screenWidth/2 - m1Width/2, 50))
		self.screen.blit(m2, (self.screenWidth/2 - m2Width/2, 250))