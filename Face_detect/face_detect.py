import cv2
img=cv2.imread('HAN.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faceCascade=cv2.CascadeClassifier('face_detect.xml')
result=faceCascade.detectMultiScale(img,1.1, 3)
print(len(result))
for (x,y,w,h) in result:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)




cv2.imshow('img',img)
cv2.waitKey(0)