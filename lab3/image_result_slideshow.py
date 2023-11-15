import glob
import subprocess
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import time

import time

import psutil
from helpers import get_user_info
from image_tool import ImageTool


def result_slideshow():
    
    paths = ImageTool.result
    delay = 2000


    root = tk.Tk()
    root.title('Slideshow App')

    SlideshowApp(root, paths, delay)

    root.mainloop()

    


class SlideshowApp:
    def __init__(self, root, image_paths, delay=3000):
        self.root = root
        self.image_paths = image_paths
        self.delay = delay
        self.current_image = None
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(fill=tk.X)

        self.play_button = tk.Button(self.controls_frame, text='Play', command=self.start_slideshow)
        self.play_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self.controls_frame, text='Pause', command=self.pause_slideshow, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT)

        self.image_index = 0
        self.slideshow_running = False

    def start_slideshow(self):
        self.slideshow_running = True
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.update_image()

    def pause_slideshow(self):
        self.slideshow_running = False
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    

    def update_image(self):
        if self.slideshow_running:
            self.current_image = Image.open(self.image_paths[self.image_index])
            self.current_image = self.current_image.resize((500, 500))
            self.photo = ImageTk.PhotoImage(self.current_image)
            self.image_label.config(image=self.photo)
            self.image_index = (self.image_index + 1) % len(self.image_paths)
            self.root.after(self.delay, self.update_image)


