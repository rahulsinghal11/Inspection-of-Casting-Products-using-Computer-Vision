import cv2
import numpy as np
img_bgr = cv2.imread("C:/Users/rahul/Desktop/Project2/features/8d2417f7ec9640df9f5a6baa041a565c.jpg")
gray_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
for p in range(1, 15):
	i = "C:/Users/rahul/Desktop/Project2/features/" + "feature" + str(p) + ".jpg"
	template = cv2.imread(i, 0)	
	w1, h1 = template.shape[::-1]
	res1 = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
	threshold = 0.85
	loc1 = np.where(res1 >= threshold)	

	for pt in zip(*loc1[::-1]):
		print(type(pt[0]))
		cv2.rectangle(img_bgr, pt, (pt[0]+w1, pt[1]+h1), (0, 255, 255), 1)
cv2.imshow('detected', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()