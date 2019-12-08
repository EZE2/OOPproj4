# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Button, Canvas, Frame, Label, Tk, PhotoImage
from tkinter.font import Font
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
from src.tmp_sheet import *
import src.play
import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
IMG_PATH = os.path.join(BASE_PATH, 'resource')

""""""""""""""
# GUI Modules
# Execution Environment - Python 3.7.4 version
# Used tkinter almost / PIL for background(.png)
# There are 7 Classes here,
# MyFrame, KeyboardGUI(White/BlackPianoButton),
# RecordGUI, SheetGUI, instrumentGUI
""""""""""""""

root = Tk()
WIDTH  = 600  # Background image width
HEIGHT = 338  # Background image height

# global font property
arial_font = tk.font.Font(root, family='Arial', size=17, weight='bold')

# sheet object from tmp_sheet.py in src
sheet_obj = sheet_class()

"""
# For program Window / Background
# using tk Canvas for loading background and call image with ImageTk(PIL) 
# set Frame to secure space for background
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

        self.right_frame = Frame(root, width=1, height=HEIGHT, bg='black', bd=0)
        self.right_frame.grid(row=0, column=30)


# Piano Button list(Each of these is a Button name and respond to same keyboard input)
white_button_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';']
black_button_list = ['w', 'e', 'NULL', 't', 'y', 'u', 'NULL', 'o', 'p']


"""
# Keyboard GUI
# WhitePianoButton and BlackPianoButton are child class of KeyboardGUI class
# keyboardGUI is used in main.py's key_input function
# GUI is made by tk Button, grid
# buttons have two state - Pressed or Unpressed
"""
class WhitePianoButton(Button):
    def makename(self, name):
        self.name = name
        self.isPressed = False

    def update(self):
        if self.isPressed:
            self.isPressed = False
            self.configure(bg='Azure')
        else:
            self.isPressed = True
            self.configure(bg='LightCyan2')


class BlackPianoButton(Button):
    def makename(self, name):
        self.name = name
        self.isPressed = False

    def update(self):
        if self.isPressed:
            self.isPressed = False
            self.configure(bg='SteelBlue4')
        else:
            self.isPressed = True
            self.configure(bg='DeepSkyBlue3')


class KeyboardGUI:
    button_list = list()  # It has white button list first and append black "

    def __init__(self):
        scales = 1
        white_keys = 10 * scales
        black = [1, 1, 0, 1, 1, 1, 0, 1, 1, 0] * scales

        for i in range(white_keys):
            self.button = WhitePianoButton(root, relief='raised', bg='Azure', bd=2)
            self.button.grid(row=1, column=i * 3, rowspan=2, columnspan=3, sticky='nsew')
            self.button.makename(white_button_list[i])
            KeyboardGUI.button_list.append(self.button)

        for i in range(white_keys - 1):
            if black[i]:
                self.button = BlackPianoButton(root, relief='raised', bg='SteelBlue4', bd=4, activebackground='gray12')
                self.button.grid(row=1, column=(i * 3) + 2, rowspan=1, columnspan=2, sticky='nsew')
                self.button.makename(black_button_list[i])
                KeyboardGUI.button_list.append(self.button)

        for i in range(white_keys * 3):
            root.columnconfigure(i, weight=1)

        for i in range(2):
            root.rowconfigure(i+1, weight=1)


axisX = 500  # To set x, y place of buttons and labels below
axisY = 20
distY = 75   # Y axis Distance

"""
# Record Button GUI
# made by tk Button, PhotoImage
# button also has two state - recording / stopped (onclick event)
# If clicked, image is changed, and command also changed to deal with two function
"""
class RecordGUI:
    record_img = PhotoImage(file=os.path.join(IMG_PATH, 'recordbutton.png'))
    stop_img = PhotoImage(file=os.path.join(IMG_PATH, 'stopbutton.png'))

    def __init__(self):
        self.button = Button(root, width=95, height=30, bd=0, command=self.start_recording)
        self.button.configure(image=self.record_img)
        self.button.place(x=axisX, y=axisY)

    def start_recording(self):
        sheet_obj.sheet_clear()  # sheet clear to get newly one by one sheet
        self.button.configure(image=self.stop_img)
        self.button['command'] = self.stop_recording
        # start recording

    def stop_recording(self):
        self.button.configure(image=self.record_img)
        self.button['command'] = self.start_recording
        making_txt(sheet_obj)
        # stop recoding and save file


"""
# Current Instruments Label GUI
# made by tk Label and Font
# the main.py has instrumentGUI object so can use change funcion in option func.
# Just simply change Text in label
"""
class InstrumentGUI:
    def __init__(self):
        self.name = 'piano'
        self.label = Label(root, width=10, height=2, bg='black', bd=0,
                           text="_Piano", fg='white', anchor='w', wraplength=100, justify='right')
        self.label['font'] = arial_font
        self.label.place(x=axisX-14, y=axisY+distY+10)

    def change(self, inst_name):
        self.name = inst_name
        if self.name == "piano":
            self.label['text'] = "_Piano"
        elif self.name == "acoustic guitar":
            self.label['text'] = "Acoustic_Guitar"
        elif self.name == "violin":
            self.label['text'] = "_Violin"
        elif self.name == "whiparam":
            self.label['text'] = "_Whitle"


"""
# Sheet Load Button GUI
# It uses tkinter.filedialog to load saved sheet music(we used txt file)(onclick event)
# After load, it play sheet music soon
"""
class SheetGUI:
    def __init__(self):
        self.button = Button(root, width=5, height=1, bg='black', bd=0, activebackground='black', text="OPEN",
                             fg='Aquamarine', anchor='w', activeforeground='Aquamarine4', command=self.load_file)
        self.button['font'] = arial_font
        self.button.place(x=axisX-3, y=axisY+distY+distY)

    def load_file(self):
        filename = askopenfilename(initialdir=BASE_PATH, filetypes=(
                                              ('text files', 'txt'),
                                              ('All files', '*.*') ))
        if filename:
            try:
                print("""Success loading file: self.settings["template"].set(filename)""")
                src.play.play_load_score(filename)
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % filename)
            return


# init all class in GUI.py except InstrumentGUI(it is in main.py)
def GUIinit():
    myframe = MyFrame()
    keyboard = KeyboardGUI()
    record = RecordGUI()
    sheet = SheetGUI()



