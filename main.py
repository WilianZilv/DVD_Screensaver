from tkinter import *
from logo import Logo


window_size = (960, 640)
root = Tk()
root.title('DVD Screensaver')

root.geometry('{}x{}'.format(window_size[0], window_size[1]))
root.minsize(width=256, height=256)

Logo(root, window_size)

root.mainloop()
