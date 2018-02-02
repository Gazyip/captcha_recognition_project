import cv2
import numpy as np
from matplotlib import pyplot as plt
np.set_printoptions(threshold=np.inf)

img=cv2.imread('850.png')

GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
images = thresh1
mtr=np.array(images)
h, w = img.shape[:2]
flag = []
flagg = []
'''
buttom_point = []
def buttom():
    for i in range(h-1,1,-1):
        for j in range(0,w):
            if(mtr[i,j]==0):
                buttom_point.append(i)
                buttom_point.append(j)
                return (i,j)
            
buttom()
print (buttom_point)
'''
def projection():
    for j in range(0,w):
        for i in range(0,h):
            if(mtr[i,j]==0):
                flagg.append(11-i)
                break
            
projection()
print(flagg)
for i in range(1,len(flagg)):
    flag.append(abs(flagg[i]-flagg[i-1]))

print(flag)

for j in range(len(flag)-1,0,-1):
    if(flag[j]>3):
        print(w-flag[j])
        break


plt.imshow(images)
plt.show()
