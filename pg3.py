import numpy as np
import cv2
b = np.zeros([480,480],dtype = 'uint8')
for j in range(60,480,120):
        for i in range (60,480,120):   
            b[j-60:j,i-60:i] = 255
            b[j:j+60,i:i+60] = 255 
cv2.imshow('checker board 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
