# NN imports
import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui

from Player import Player

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
          originalImage = image
          processedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
          processedImage = cv2.Canny(processedImage, threshold1=200, threshold2=300)
          points = np.array([[100, 800], [100, 500], [950, 500], [950, 800]])
          processedImage = RegionOfInterest(processedImage, [points])

          leftLine = 100
          rightLine = 900

          # Processed lines as edges
          lines = cv2.HoughLinesP(processedImage, 1, np.pi/180, 180, np.array([]), 20, 15)
          #DrawLines(processedImage, lines)
          DrawLines(originalImage, lines)
          return processedImage, originalImage

def Left():
     print('LEFT')
     pyautogui.keyUp('Right')
     pyautogui.keyDown('left')

def Right():
     print('RIGHT')
     pyautogui.keyUp('Left')
     pyautogui.keyDown('Right')

def Straight():
     print('Straight')
     pyautogui.keyUp('Left')
     pyautogui.keyUp('Right')          

def RunNN(player):
     # Grab an image of the screen
     screen = np.array(ImageGrab.grab(bbox=(20,50,1020,840)))

     newScreen, originalImage = ProcessImage(screen)

     leftLine = 130
     rightLine = 930
     
     # TEMP TO TEST MOVEMENT AND INTEGRATION WITH SUBLIME CODE
     if player.x - leftLine < 50:
          Right()
     elif rightLine - (player.x + player.width) < 50:
          Left()
     else:
          Straight()
           
     # Show the image on the screen
     #cv2.imshow('window', newScreen)
     cv2.imshow('dtm3', cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB))
     #cv2.moveWindow ('window', 1100, 20)
     cv2.moveWindow ('dtm3', 1100, 50)
     if cv2.waitKey(25) and 0xFF == ord('q'):
             cv2.destroyAllWindows()
