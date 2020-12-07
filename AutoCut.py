import cv2

img = cv2.imread(r"D:\pythonExp\opencv\cars.jpg")
#img = cv2.imread(r"D:\pythonExp\opencv\cars.jpg")
#add a line

a = 100
b = 60
c = 0
for y in range(7): 
    y0 = y * b
	
    for x in range(28):
        x0 = x * a
        #cv2.rectangle(img, (x0,y0), (x0+a,y0+b), (0,0,255), 2)
        cut_img = img[y0:y0+b, x0:x0+a]

        cv2.imwrite("D:\pythonExp\opencv\cuts\cut" + str(y) + str(x) + ".jpg",cut_img)
        cv2.imshow('image', cut_img)
        cv2.waitKey(20)

cv2.waitKey(0)