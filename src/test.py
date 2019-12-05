import pygame.midi
import pygame
import sys
from tkinter import *
import keyboard
from src.save import *

pygame.midi.init()


class KeyboardGUI:
    def __init__(self):
        scales = 1
        root.geometry('{}x200'.format(300 * scales))
        white_keys = 10 * scales
        black = [1, 1, 0, 1, 1, 1, 0, 1, 1] * scales
        root.bind('<Key>', key_input)
        for i in range(white_keys):
            self.button = Button(root, bg='white', activebackground='gray87', command=lambda i=i: key_input)
            self.button.grid(row=0, column=i * 3, rowspan=2, columnspan=3, sticky='nsew')

        for i in range(white_keys - 1):
            if black[i]:
                self.button = Button(root, bg='black', activebackground='gray12', command=lambda i=i: key_input)
                self.button.grid(row=0, column=(i * 3) + 2, rowspan=1, columnspan=2, sticky='nsew')

        for i in range(white_keys * 3):
            root.columnconfigure(i, weight=1)

        for i in range(2):
            root.rowconfigure(i, weight=1)


if __name__ == "__main__":
    root = Tk()
    keyboardgui = KeyboardGUI()
    root.mainloop()