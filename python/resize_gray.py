import cv2
import sys
import os

#path = "D:/software/opencv3/opencv/build/x64/vc14/binHog/posdata/"
path = "D:/software/opencv3/opencv/build/x64/vc14/binFace/faces/"

files = os.listdir(path)

n = 0
for filename in files:
    n = n + 1
    print(filename)
    img = cv2.imread(path + filename, cv2.IMREAD_GRAYSCALE)
    #img = cv2.resize(img, (30, 30))
    cv2.imshow("img", img)
    cv2.waitKey(10)
    cv2.imwrite("D:/software/opencv3/opencv/build/x64/vc14/binFace/posdata/" + str(n) + ".jpg", img)