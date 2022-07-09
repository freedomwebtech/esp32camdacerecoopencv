import cv2
from esp32tst import cam
while True:
     frame=cam()
     frame=cv2.resize(frame,(640,480))
     frame=cv2.flip(frame,1)
    
    

     cv2.imshow('FRAME',frame)
    
     if cv2.waitKey(1) == ord('a'):
        a=input("username:-")
        frame=cv2.imwrite(("/home/pi/images/")+str(a)+".jpg",frame) 
        print ("pressed a")
        break         
cv2.destroyAllWindows()