import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui

def ProcessImage(image):
	processedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	processedImage = cv2.Canny(processedImage, threshold1=200, threshold2=300)
	return processedImage

for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

while True:
        # Grab an image of the screen
        screen = np.array(ImageGrab.grab(bbox=(20,50,1020,840)))

        newScreen = ProcessImage(screen)

        # Movement
        print('down')
        pyautogui.keyDown('left')
        time.sleep(1)
        print('up')
        pyautogui.keyUp('left')
	
        # Show the image on the screen
        cv2.imshow('window', newScreen)
        cv2.moveWindow ('window', 1100, 20)
        if cv2.waitKey(25) and 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


