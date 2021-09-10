# If you don't have installed al ready install it using the below codes
# pip install opencv-python
# pip install numpy

# Import Libraries
import numpy as np
import cv2
import time
import ctypes  # An included library with Python install / For message boxes 

ctypes.windll.user32.MessageBoxW(0, "Capturing your Background... Please be away from the frame for 2 seconds", "Invisible cloak by Saadh Jawwadh ", 0)  #https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python

# using a webcam to capture the live feed of the person and the background
cap = cv2.VideoCapture(0)
time.sleep(2)  #Adjust the initial background capture time using this    
background = 0

ctypes.windll.user32.MessageBoxW(0, "Use 'Red' cloth as your cloak, To Terminate Press 'Esc'", "Invisible cloak by Saadh Jawwadh ", 0)

# Capturing the Background
for i in range(50):
    ret, background = cap.read()

# Capturing the video feed using Webcam
while(cap.isOpened()): 
    ret, img = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # Setting the cloak colour values
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255]) # HSV values is for "red" colour Cloth you can changed it if you want
    mask1 = cv2.inRange(hsv, lower_red,upper_red)
    lower_red = np.array([170,120,70])
    upper_red =  np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

#Combining the masks
    mask1 = mask1 +mask2

#After combining the mask we are storing the value in deafult mask.
# Using Morphological Transformations to remove noise from the cloth and unnecessary Details.
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)
    mask2 =cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(background,background,mask=mask1)

#The basic work of bitwise_and is to combine these background and store it in res1
    res2 = cv2.bitwise_and(img,img,mask=mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('Invisible Cloak',final_output)
    k = cv2.waitKey(10)
    if k==27: #27 is a code for 'Esc' button
        ctypes.windll.user32.MessageBoxW(0, "Thank you for using! - Saadh Jawwadh", "Invisible cloak by Saadh Jawwadh ", 0)
        break
cap.release()
cv2.destroyAllWindows()

# Reference: https://www.analyticsvidhya.com/blog/2021/07/harry-potters-invisible-cloak-using-opencv-python/
