# NN imports
import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui

# Game Imports
from Player import Player
from Menus import Menus
from Level import Level
from Obstacles import Obstacle
from Text import Text
from CollisionChecker import CollisionChecker


# ADD THE GAME LOOP HERE SO THE GAME CAN RUN, ALSO ATTEMPTS
# CAN USE THE SAME FORMAT AS FSM BUT REMOVING ITS LOGIC

# What the Neural Network is interested in
def RegionOfInterest(image, points):
     mask = np.zeros_like(image)
     cv2.fillPoly(mask, points, 255)
     masked = cv2.bitwise_and(image, mask)
     return masked

def DrawLines(image, lines):
        try:
                for line in lines:
                        coords = line[0]
                        cv2.line(image, (coords[0], coords[1]),(coords[2], coords[3]), [255, 255, 255], 3)
        except:
                 pass

def ProcessImage(image):
	processedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	processedImage = cv2.Canny(processedImage, threshold1=200, threshold2=300)
	points = np.array([[100, 800], [100, 500], [950, 500], [950, 800]])
	processedImage = RegionOfInterest(processedImage, [points])

        # Processed lines as edges
	lines = cv2.HoughLinesP(processedImage, 1, np.pi/180, 180, 20, 15)
	DrawLines(processedImage, lines)
	
	return processedImage

def RunGame(world):
        return True


def Main():
        while True:
                # Grab an image of the screen
                screen = np.array(ImageGrab.grab(bbox=(20,50,1020,840)))

                newScreen = ProcessImage(screen)

                # Movement
        ##        print('down')
        ##        pyautogui.keyDown('left')
        ##        time.sleep(1)
        ##        print('up')
        ##        pyautogui.keyUp('left')
                
                # Show the image on the screen
                cv2.imshow('window', newScreen)
                cv2.moveWindow ('window', 1100, 20)
                if cv2.waitKey(25) and 0xFF == ord('q'):
                        cv2.destroyAllWindows()
                        break

Main()


