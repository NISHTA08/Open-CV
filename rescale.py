import cv2 as cv
    
#Rescale an image

# img= cv.imread('images/cat_large.jpg')
# cv.imshow('Cat',img)

# def rescaleFrame(frame,scale=0.1):
#     width=int(frame.shape[1]*scale)
#     height=int(frame.shape[0]*scale)
#     dimensions=(width,height)

#     return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# resized_image=rescaleFrame(img)
# cv.imshow('Cat_resized',resized_image)

# cv.waitKey(0)


#Rescale a live video from webcam

# def changeRes(width,height):
#     capture.set(3,width)
#     capture.set(4,height)


#Rescale a video

# capture=cv.VideoCapture('videos/dog.mp4')
# while True:
#     isTrue,frame=capture.read()

#     frame_resized=rescaleFrame(frame)

#     cv.imshow('Video',frame)
#     cv.imshow('Video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
