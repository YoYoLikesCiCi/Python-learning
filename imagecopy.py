import cv2
import numpy as np
 
img = cv2.imread('F:/beauty.jpg')
#print img.item(10, 10, 2)
#img.itemset((10,10,2),100)
#print img.item(10, 10, 2)
#print img.dtype
 
ball = img[350:500, 300:450]#矩形框取样本
img[160:310, 100:250] = ball#粘贴样本
 
cv2.imshow("beauty",img)
cv2.waitKey()
cv2.destroyAllWindows()


