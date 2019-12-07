# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
IMG_PATH = os.path.join(BASE_PATH, 'resource')

"""
# GUI Modules
# Execution Environment - Python 3.7.4 version
# Used tkinter, tkinter.font almost / PIL for background, button image
# There are 6 Classes here,
# MyFrame, KeyboardGUI(White/BlackPianoButton(child class)),
# RecordGUI, InstrumentsGUI
"""

root = Tk()
WIDTH  = 600  # Background image width
HEIGHT = 338  # Background image height

"""
" For Window / Background
" using tk Canvas for loading background and call image with ImageTk(PIL) 
" set Frame to secure space for background
"""
class MyFrame:
    def __init__(self):
        root.geometry('600x538')
        root.title("Virtual Instruments")
        root.resizable(False, False)

        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT)
        self.bg_img = ImageTk.PhotoImage(Image.open(os.path.join(IMG_PATH, 'gris.png')).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        self.canvas.background = self.bg_img
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_img)
        self.canvas.place(x=0, y=0)

        self.right_frame = Frame(root, width=1, height=HEIGHT, bg='black')
        self.right_frame.grid(row=0, column=30)
        self.right_frame['borderwidth'] = 0

        # self.left_frame = Frame(root, width=1, bg='white')
        # self.left_frame.grid(row=0, column=0)
        # self.left_frame['borderwidth'] = 0


# Piano Button list(Each of these is a Button name and respond to same keyboard input)
white_button_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';']
black_button_list = ['w', 'e', 'NULL', 't', 'y', 'u', 'NULL', 'o', 'p']


"""
# Keyboard GUI
# WhitePianoButton and BlackPianoButton are child class of KeyboardGUI class
# keyboardGUI is used in main.py's key_input function
# made with tk Button, grid
# buttons have two state - Pressed or Unpressed
"""
class WhitePianoButton(Button):
    def makename(self, name):
        self.name = name
        self.isPressed = False

    def update(self):
        if self.isPressed:
            self.isPressed = False
            self.configure(bg='white')
        else:
            self.isPressed = True
            self.configure(bg='LightSkyBlue')


class BlackPianoButton(Button):
    def makename(self, name):
        self.name = name
        self.isPressed = False

    def update(self):
        if self.isPressed:
            self.isPressed = False
            self.configure(bg='black')
        else:
            self.isPressed = True
            self.configure(bg='DimGray')


class KeyboardGUI:
    button_list = list()  # It has white button list first and append black "

    def __init__(self):
        scales = 1
        white_keys = 10 * scales
        black = [1, 1, 0, 1, 1, 1, 0, 1, 1, 0] * scales

        for i in range(white_keys):
            self.button = WhitePianoButton(root, relief='raised', bg='white', bd=2)
            self.button.grid(row=1, column=i * 3, rowspan=2, columnspan=3, sticky='nsew')
            self.button.makename(white_button_list[i])
            KeyboardGUI.button_list.append(self.button)

        for i in range(white_keys - 1):
            if black[i]:
                self.button = BlackPianoButton(root, relief='raised', bg='black', bd=4, activebackground='gray12')
                self.button.grid(row=1, column=(i * 3) + 2, rowspan=1, columnspan=2, sticky='nsew')
                self.button.makename(black_button_list[i])
                KeyboardGUI.button_list.append(self.button)

        for i in range(white_keys * 3):
            root.columnconfigure(i, weight=1)

        for i in range(2):
            root.rowconfigure(i+1, weight=1)


"""
# Record Button GUI
# made with tk Button and Using PhotoImage(PIL)
# button also has two state - recording / stopped
"""
class RecordGUI:
    def __init__(self):
        self.record_img = PhotoImage(file=os.path.join(IMG_PATH, 'recordbutton.png'))
        self.stop_img = PhotoImage(file=os.path.join(IMG_PATH, 'stopbutton.png'))

        self.button = Button(root, command=self.recording)
        self.button.config(image=self.record_img, width=95, height=30, bd=0)
        self.button.place(x=500, y=25)

        # self.button.bind('<Button-1>', self.recording())
        # self.button.bind('<Return>', self.stop_recording())

        # self.button = PlayButton(root, width=7, height=3, text="PLAY", bg='black', fg='white')
        # self.button.grid(row=0, column=30)
        # self.button.makename(record_button[0])
        # RecordGUI.record_button_list.append(self.button)

    def recording(self):
        self.button.config(image=self.stop_img)
        self.button['command'] = self.stop_recording
        # start recording

    def stop_recording(self):
        self.button.config(image=self.record_img)
        self.button['command'] = self.recording


# Used to show what instrument is currently playing with tk Label and Font
class PlayLabelGUI:
    def __init__(self):
        self.label_font = tk.font.Font(root, family='Arial', size=17, weight='bold')
        self.label = Label(root, width=10, height=1, bg='black', bd=0,
                           text="Piano", fg='white', anchor='w')
        self.label['font'] = self.label_font
        self.label.place(x=500, y=92)
        # self.label_button = Button(root, bg='black', bd=0, command=self.change)
        # self.label_button.place(x=600, y=10)

    def change(self, _key):
        if _key == 1:
            self.label.configure(text="Piano")
        elif _key == 2:
            self.label.configure(text="Acoustic Guitar")
        elif _key == 3:
            self.label.configure(text="Violin")


# init all in GUI
def GUIinit():
    myframe = MyFrame()
    keyboardgui = KeyboardGUI()
    recordgui = RecordGUI()
    playlabelgui = PlayLabelGUI()




