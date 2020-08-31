import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import ImageTk, Image
root = tk.Tk()
Height = 600
Width = 700

def browse_function():
	filename = filedialog.askopenfilename()
	if filename:
		img_bgr = cv2.imread(filename)
		gray_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
		for p in range(1, 15):
			i = "C:/Users/rahul/Desktop/Project2/features/" + "feature" + str(p) + ".jpg"
			template = cv2.imread(i, 0)	
			w1, h1 = template.shape[::-1]
			res1 = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
			threshold = 0.85
			loc1 = np.where(res1 >= threshold)
			for pt in zip(*loc1[::-1]):
				cv2.rectangle(img_bgr, pt, (pt[0]+w1, pt[1]+h1), (0, 255, 255), 1)
		cv2.imshow('detected', img_bgr)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		pathlabel.config(text=filename)	

canvas = tk.Canvas(root, height=Height, width = Width)
canvas.pack()

#background_image = tk.PhotoImage(file='C:/Users/rahul/Desktop/Project2/103 (2).jpg')
#background_label = tk.Label(root, image = background_image)
#background_label.place(relwidth=1, relheight=1)
upper_frame = tk.Frame(root, bg = '#41f0db')
upper_frame.place(relx = 0.5, rely = 0.1, relwidth=0.92, relheight=0.4, anchor = 'n')

upper_label_1 = tk.Label(upper_frame, text = 'Defect Detection', bg = '#41f0db', fg = '#2f4544', font = 'Calibri 30')
upper_label_1.place(x = 18, y = 50)

upper_label_2 = tk.Label(upper_frame, text = 'Powered by Python', bg = '#41f0db', fg = '#2f4544', font = 'Calibri 20')
upper_label_2.place(x = 27, y = 95)

frame = tk.Frame(root, bg = '#7acf59', bd = 5)
frame.place(relx = 0.19, rely = 0.55, relwidth=0.3, relheight=0.06, anchor = 'n')

button = tk.Button(frame, text = "Choose file", font = 'Calibri 12',  command=browse_function)
button.place(x = 12, y=4, relwidth=0.5, relheight=0.8)

pathlabel = tk.Label(root)
pathlabel.pack()

root.mainloop()
