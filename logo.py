from random import randint, choice
from tkinter import Label
import cv2
from PIL import Image, ImageTk


class Logo:

    photo_image = None

    tick = 10
    speed = .25

    dir_x = choice((-1, 1))
    dir_y = choice((-1, 1))

    def __init__(self, root, window_size):

        self.root = root
        self.window_size = window_size
        self.obj = Label(root)

        self.pos_x = randint(0, window_size[0]-256)
        self.pos_y = randint(0, window_size[1]-256)

        # -= sets a value for 'self.photo_image'
        self.load_and_tint_image()

        self.bounds = (self.photo_image.width(), self.photo_image.height())

        self.loop()

    def loop(self):
        self.root.after(self.tick, self.render)

    def render(self):

        max_x = self.root.winfo_width() - self.bounds[0]
        max_y = self.root.winfo_height() - self.bounds[1]

        self.pos_x += self.speed * self.dir_x * self.tick
        self.pos_y += self.speed * self.dir_y * self.tick

        if self.pos_x >= max_x or self.pos_x <= 0:
            self.dir_x *= -1

            if self.pos_x >= max_x:
                self.pos_x = max_x
            else:
                self.pos_x = 0

            self.load_and_tint_image()

        if self.pos_y >= max_y or self.pos_y <= 0:
            self.dir_y *= -1

            if self.pos_y >= max_y:
                self.pos_y = max_y
            else:
                self.pos_y = 0

            self.load_and_tint_image()

        self.obj.place(x=self.pos_x, y=self.pos_y)

        self.loop()

    def load_and_tint_image(self):

        # -Getting PhotoImage
        self.photo_image = self.tint_image('dvd_logo.png', 25, 200)

        # -Applying PhotoImage to Label
        self.obj.config(image=self.photo_image)

    def tint_image(self, path, min_brightness, max_brightness):

        # -Loading image data from path
        rgba_data = cv2.imread(path, cv2.IMREAD_UNCHANGED)

        # -Generate random RGB color
        tint = self.random_rgb_color(min_brightness, max_brightness)

        # -Get 'tint' R G B and apply it in rgba_data's R G B
        for channel in range(len(tint)):
            rgba_data[:, :, channel] = tint[channel]

        # -Converting from image data to tkinter's PhotoImage
        image = Image.fromarray(rgba_data)
        return ImageTk.PhotoImage(image)

    @staticmethod
    def random_rgb_color(min_brightness, max_brightness):
        rgb = []
        for c in range(3):
            rgb.append(randint(min_brightness, max_brightness))

        return rgb
