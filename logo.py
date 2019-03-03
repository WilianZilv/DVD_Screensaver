from random import randint, choice
from tkinter import PhotoImage, Label

class DVDLogo:

    def __init__(self, w, window_size):

        self.w = w
        self.window_size = window_size
        self.initialized = False

        self.pos_x = randint(0, window_size[0])
        self.pos_y = randint(0, window_size[1])

        self.tick = 10
        self.speed = .25
        self.dir_x = choice((-1, 1))
        self.dir_y = choice((-1, 1))

        self.img = PhotoImage(file="dvd_logo.png")
        self.img_size = (self.img.width(), self.img.height())

        self.obj = Label()
        self.obj.config(width=self.img.width(), height=self.img.height(), image=self.img)

        self.update()

    def update(self):

        w = self.w
        obj = self.obj

        max_x = w.winfo_width() - self.img_size[0]
        max_y = w.winfo_height() - self.img_size[1]

        if self.initialized is False:
            max_x = self.window_size[0] - self.img_size[0]
            max_y = self.window_size[1] - self.img_size[1]
            self.initialized = True

        self.pos_x += self.speed * self.dir_x * self.tick
        self.pos_y += self.speed * self.dir_y * self.tick

        if self.pos_x >= max_x or self.pos_x <= 0:
            self.dir_x *= -1

            if self.pos_x >= max_x:
                self.pos_x = max_x
            else:
                self.pos_x = 0

        if self.pos_y >= max_y or self.pos_y <= 0:
            self.dir_y *= -1

            if self.pos_y >= max_y:
                self.pos_y = max_y
            else:
                self.pos_y = 0

        obj.place(x=self.pos_x, y=self.pos_y)
        w.after(self.tick, lambda: self.update())

