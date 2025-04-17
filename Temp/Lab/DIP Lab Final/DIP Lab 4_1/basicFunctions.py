import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston',img)

#1.Converting to gray scasle
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

#2.Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('BLUR',blur)

#3.Edge Cascade
canny = cv.Canny(blur, 125 ,175)
cv.imshow('Edge Casecade',canny)

#4.Dilating image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

#5.Eroding
eroding = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroding)

#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Crop
crop = img[50:200,200:400]
cv.imshow('Cropped',crop)

cv.waitKey(0)