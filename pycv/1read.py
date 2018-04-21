import numpy as ny
import cv2

img=cv2.imread('/Users/zorro/test.jpeg')
cv2.imshow('image',img)
k=cv2.waitKey(0)

if k==27:
	cv2.destroyAllWindows()
elif k==ord('s'):
	cv2.imwrite('./messigray.png',img)
	cv2.destroyAllWindows()
