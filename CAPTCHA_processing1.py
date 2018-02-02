import cv2
import numpy as np
from matplotlib import pyplot as plt
np.set_printoptions(threshold=np.inf)
for z in range(0,100):
    img=cv2.imread('%s.jpg' %z)
    GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
    images = thresh1
    Listx = []
    Listy = []
    mtr=np.array(images)
    for j in range(0,80):
        for i in range(0,25):
            if(mtr[i,j]==0):
                Listx.append(j)
                break
    print(Listx)
    Listy.append(Listx[0]-1)
    for k in range (1,len(Listx)):
        if(Listx[k]!=Listx[k-1]+1):
            Listy.append(Listx[k-1])
            Listy.append(Listx[k])
    Listy.append(Listx[-1])
    print(Listy)
    m=0
    while(m<len(Listy)):
        roi = images[0:,Listy[m]:Listy[m+1]]
        if(Listy[m+1]-Listy[m]>=11):
            cv2.imwrite('C:\\Users\\Gaz\\Desktop\\Cappp\\mul\\%s%s.png' %(z,m),roi)
        else:
            cv2.imwrite('C:\\Users\\Gaz\\Desktop\\Cappp\\sin\\%s%s.png' %(z,m),roi)            
        m=m+2