import keyboard
import time
import pygame.midi
import threading
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

pygame.midi.init()

WIDTH  = 600  # Background image width
HEIGHT = 338  # Background image height


class MyFrame:
    def __init__(self):
        root.geometry('600x538')
        root.title("Virtual Instruments")
        root.resizable(False, False)

        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT)
        self.bg_img = ImageTk.PhotoImage(Image.open('gris2.jpg').resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        self.canvas.background = self.bg_img
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_img)
        self.canvas.place(x=0, y=0)

        self.left_frame = Frame(root, width=1, height=340, bg='white')
        self.left_frame.grid(row=0, column=0)
        self.left_frame['borderwidth'] = 0

        # self.right_frame = Frame(root, width=1, bg='white')
        # self.right_frame.grid(row=0, column=31)
        # self.right_frame['borderwidth'] = 0


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
            self.button = WhitePianoButton(root, relief='ridge', bg='white', bd=3, activebackground='gray87')
            self.button.grid(row=5, column=i * 3 + 1, rowspan=2, columnspan=3, sticky='nsew')
            self.button.makename(white_button_list[i])
            KeyboardGUI.button_list.append(self.button)

        for i in range(white_keys - 1):
            if black[i]:
                self.button = BlackPianoButton(root, relief='raised', bg='black', bd=4, activebackground='gray12')
                self.button.grid(row=5, column=(i * 3) + 3, rowspan=1, columnspan=2, sticky='nsew')
                self.button.makename(black_button_list[i])
                KeyboardGUI.button_list.append(self.button)

        for i in range(white_keys * 3):
            root.columnconfigure(i+1, weight=1)

        for i in range(2):
            root.rowconfigure(i+5, weight=1)


record_button_list = ['m']


class RecordButton(Button):
    def makename(self, name):
        self.name = name
        self.isPressed = False

    def update(self):
        if self.isPressed:
            self.isPressed = False
            self.configure(bg='black', text='RECORD')
        else:
            self.isPressed = True
            self.configure(bg='Red', text='STOP')
            # 녹화시작
            print("start record...")


class RecordGUI:
    button_list2 = list()

    def __init__(self):
        self.record_img = PhotoImage(file="recordbutton.png")
        self.button = RecordButton(root)
        self.button.config(image=self.record_img, width=95, height=30, activebackground='Red', bd=0)
        self.button.place(x=500, y=25)
        self.button.makename(record_button_list[0])
        RecordGUI.button_list2.append(self.button)

        # self.button = PlayButton(root, width=7, height=3, text="PLAY", bg='black', fg='white')
        # self.button.grid(row=0, column=30)
        # self.button.makename(record_button[0])
        # RecordGUI.record_button_list.append(self.button)


# class KeyInputManager:
#    def key_input(self, key, note):


class Instrument:
    player = pygame.midi.Output(1)

    def __init__(self, inst_no):
        self.player.set_instrument(inst_no, 1)

    def set_instrument(self, inst_no):
        self.player.set_instrument(inst_no, 1)

    def note_on(self, note):
        self.player.note_on(note, 127, 1)
        time.sleep(0.1)

    def note_off(self, note):
        self.player.note_off(note, 127, 1)


# test zone--------------------------------------------------


midi_dic = {'piano': 2, 'acoustic guitar': 24}  # midi 표 -1 = 악기번호

key_list = ['q', 'w', 'e', 'r', 't']
key_list2 = ['a', 's', 'd', 'f', 'g']
note_list = [60, 62, 64, 65, 67]


def inst_key_pressed(instrument, inst_name):
    print("change instrument:" + inst_name)
    instrument.set_instrument(midi_dic[inst_name])


def change_inst_key(instrument):
    while True:
        if keyboard.is_pressed('1'):
            inst_key_pressed(instrument, 'piano')
        elif keyboard.is_pressed('2'):
            inst_key_pressed(instrument, 'acoustic guitar')
        elif keyboard.is_pressed('0'):
            return


"""
이 프로그램의 핵심 함수임.
key_input 안에 필요한 기능 다 집어넣을 것!!
파라미터 추가하는 방식으로 저장도 이걸로 구현할 것을 권장함.
"""


def key_input(_key, _note, instrument):
    while True:
        if keyboard.is_pressed(_key):
            # 눌릴때
            print("Key pressed!")
            instrument.note_on(_note)
            for button in KeyboardGUI.button_list:
                if button.name == _key:
                    button.update()
            # player.note_on(60, 127, 1) # 첫 파라미터가 음 60이 도
            while keyboard.is_pressed(_key):
                time.sleep(0.001)
            else:  # 뗄 때
                instrument.note_off(_note)
                for button in KeyboardGUI.button_list:
                    if button.name == _key:
                        button.update()

        elif keyboard.is_pressed('m'):
            recording = True
            while recording:
                for button in RecordGUI.button_list2:
                    if keyboard.is_pressed('m'):
                        button.update()
                    elif keyboard.is_pressed('m'):
                        recording = False

        elif keyboard.is_pressed('0'):
            return


def thread_initializer(_key_list, _note_list, _instrument):
    thread1 = threading.Thread(target=key_input, args=(_key_list[0], _note_list[0], _instrument), daemon=True)
    thread2 = threading.Thread(target=key_input, args=(_key_list[1], _note_list[1], _instrument), daemon=True)
    thread3 = threading.Thread(target=key_input, args=(_key_list[2], _note_list[2], _instrument), daemon=True)
    thread4 = threading.Thread(target=key_input, args=(_key_list[3], _note_list[3], _instrument), daemon=True)
    thread5 = threading.Thread(target=key_input, args=(_key_list[4], _note_list[4], _instrument), daemon=True)
    thread_inst = threading.Thread(target=change_inst_key, args=(inst1,), daemon=True)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread_inst.start()


# for key, note in key_list, note_list:
#    globals()['thread_{}'.format(key)] = threading.Thread(target=key_input, args=(key, note, inst1))
# 안대네
if __name__ == "__main__":
    root = Tk()
    myframe = MyFrame()
    keyboardgui = KeyboardGUI()
    recordgui = RecordGUI()

    inst1 = Instrument(2)
    inst2 = Instrument(2)
    thread_initializer(key_list, note_list, inst1)
    thread_initializer(key_list2, note_list, inst2)

    root.mainloop()



