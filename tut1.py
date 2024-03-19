from tkinter import *
import os
from PIL import ImageTk, Image

w_root = Tk()

# WIDTH X HEIGHT
w_root.geometry("600x600")
# WIDTH, HEIGHT
w_root.minsize(100, 100)
# WIDTH, HEIGHT
w_root.maxsize(1000, 700)

newlabel = Label(text="Aster")
newlabel.pack()
image_path = Image.open('assets/images/image_my.png')
image = ImageTk.PhotoImage(image_path)
image_label = Label(image=image)
image_label.pack()

# gui logic
w_root.mainloop()