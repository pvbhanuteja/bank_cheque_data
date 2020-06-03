mport cv2
import numpy as np

img = cv2.imread("original.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.bitwise_not(img)
th2 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)
cv2.imshow("th2", th2)
cv2.imwrite("th2.jpg", th2)
cv2.waitKey(0)
cv2.destroyAllWindows()

horizontal = th2
vertical = th2
rows,cols = horizontal.shape
horizontalsize = cols / 30
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize,1))
horizontal = cv2.erode(horizontal, horizontalStructure, (-1, -1))
horizontal = cv2.dilate(horizontal, horizontalStructure, (-1, -1))
cv2.imshow("horizontal", horizontal)
cv2.imwrite("horizontal.jpg", horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
