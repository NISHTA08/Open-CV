import cv2 as cv

# img=cv.imread('images/lady.jpg')
# cv.imshow('Lady',img)

img=cv.imread('images/grp of humans.jpg')
cv.imshow('Group of 5 people', img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Lady',gray)

haar_cascade= cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)

print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)