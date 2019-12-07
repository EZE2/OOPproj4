import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

WIDTH  = 600  # Background image width
HEIGHT = 338  # Background image height


class MyFrame:
    def __init__(self):
        root.geometry('600x538')
        root.title("Virtual Instruments")
        root.resizable(False, False)

        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT)
        self.bg_img = ImageTk.PhotoImage(Image.open('gris.jpg').resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        self.canvas.background = self.bg_img
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_img)
        self.canvas.place(x=0, y=0)

        self.right_frame = Frame(root, width=1, height=340, bg='black')
        self.right_frame.grid(row=0, column=30)
        self.right_frame['borderwidth'] = 0

        # self.left_frame = Frame(root, width=1, bg='white')
        # self.left_frame.grid(row=0, column=0)
        # self.left_frame['borderwidth'] = 0


# Piano Button list(Each of these is a Button name)
white_button_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';']
black_button_list = ['q', 'w', 'NULL', 'e', 'r', 't', 'NULL', 'y', 'u']


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
    button_list = list()

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


class RecordGUI:
    def __init__(self):
        self.record_img = PhotoImage(file="recordbutton.png")
        self.stop_img = PhotoImage(file="stopbutton.png")

        self.button = Button(root)
        self.button.config(image=self.record_img, width=95, height=30, bd=0)
        self.button.place(x=500, y=25)

        self.button.bind('<Button-1>', self.recording())
        self.button.bind('<Return>', self.stop_recording())

        # self.button = PlayButton(root, width=7, height=3, text="PLAY", bg='black', fg='white')
        # self.button.grid(row=0, column=30)
        # self.button.makename(record_button[0])
        # RecordGUI.record_button_list.append(self.button)

    def recording(self):
        self.button.config(image=self.stop_img)

    def stop_recording(self):
        self.button.config(image=self.record_img)


if __name__ == "__main__":
    root = Tk()
    myframe = MyFrame()
    keyboardgui = KeyboardGUI()
    recordgui = RecordGUI()

    root.mainloop()



