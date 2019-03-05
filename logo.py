from random import randint, choice
from tkinter import Label
import cv2
from PIL import Image, ImageTk


class Logo:

    photo_image = None

    tick = 10
    speed = .25

    dir_2d = [choice((-1, 1)), choice((-1, 1))]

    def __init__(self, root, window_size):

        self.root = root
        self.window_size = window_size
        self.obj = Label(root)

        self.pos_2d = [randint(0, window_size[0]-256), randint(0, window_size[1]-256)]

        # -= sets a value for 'self.photo_image'
        self.load_and_tint_image()

        self.bounds = (self.photo_image.width(), self.photo_image.height())

        self.loop()

    def loop(self):
        self.root.after(self.tick, self.render)

    def render(self):

        # -Getting current window size
        max_pos_2d = [self.root.winfo_width() - self.bounds[0], self.root.winfo_height() - self.bounds[1]]

        # -For each axis in the position vector
        for i in range(len(self.pos_2d)):

            cur_pos_axis = self.pos_2d[i]
            cur_dir_axis = self.dir_2d[i]
            cur_max_pos_axis = max_pos_2d[i]

            # -Increases or decreases position value based on update rate, speed, direction of the current axis
            self.pos_2d[i] += self.speed * cur_dir_axis * self.tick

            # -Collision check
            if cur_pos_axis > cur_max_pos_axis or cur_pos_axis < 0:

                if cur_pos_axis > cur_max_pos_axis:
                    self.pos_2d[i] = cur_max_pos_axis
                    self.dir_2d[i] = -1
                else:
                    self.pos_2d[i] = 0
                    self.dir_2d[i] = 1

                self.load_and_tint_image()

        # -Apply new position
        self.obj.place(x=self.pos_2d[0], y=self.pos_2d[1])

        # -Do this function again
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
