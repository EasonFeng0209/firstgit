import cv2
import numpy as np

img = cv2.imread(r'D:\pythonExp\opencv\20.pgm')



cv2.imshow('corners', img)
cv2.imwrite(r'D:\pythonExp\opencv\201.jpg', img)
cv2.waitKey(0)
