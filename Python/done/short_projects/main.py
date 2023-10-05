# python -m pip install --upgrade pip
# pip install pillow numpy opencv-contrib-python pywin32

from PIL import ImageGrab
import numpy as qqq
import cv2
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
print (width, height)

# Here I add an image to process it later
bbox = (0, 0, width, height)
img = ImageGrab.grab(bbox)
img_np = qqq.array(img)
img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

cv2.imshow('Captura de ecran', img_final)
cv2.waitKey(100000)

print ("Programul a finisat!")

