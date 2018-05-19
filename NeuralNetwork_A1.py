import numpy as np
from PIL import ImageGrab
import cv2
import time

while True:
        # Grab an image of the screen
	printscreen_pil = ImageGrab.grab(bbox=(20,50,1020,840))
	
        # Show the image on the screen
	cv2.imshow('window', np.array(printscreen_pil))
	cv2.moveWindow ('window', 1100, 20)
	if cv2.waitKey(25) and 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break
