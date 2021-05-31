from  tkinter import *
from PIL import Image, ImageTk
# wczytanie obrazu tła
plotno.pack()
background_image=Image.open('lava.jpg')
background_imageTk=ImageTk.Photoimage(background_image)
plotno.create_image(350, 200,image=background_imageTk)

from random import randint, choice
import subprocess
import platform
import time

class PuzzlePath():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.start = (0, 0)
        self.goal = (width-1, height-1)
        self.player = (0, 0)

    def move_puzzle(self, d):
        x = self.player[0]
        y = self.player[1]
        pos = None

        if d[0] == 'r':
            pos = (x + 1, y)
        if d[0] == 'l':
            pos = (x - 1, y)
        if d[0] == 'u':
            pos = (x, y - 1)
        if d[0] == 'd':
            pos = (x, y + 1)

        if pos not in self.walls:
            self.player = pos

        if pos == self.goal:
            print("You made it to the end!")

