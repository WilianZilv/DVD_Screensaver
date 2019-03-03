from tkinter import *
from logo import DVDLogo

class Main:

    def __init__(self):

        window_size = (960, 640)

        # -WINDOW INITIALIZE
        w = Tk()
        w.title('DVD Screensaver')
        w.geometry('{}x{}'.format(window_size[0], window_size[1]))
        w.minsize(width=256, height=256)

        # -ELEMENT
        DVDLogo(w, window_size)

        w.mainloop()

Main()
