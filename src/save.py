"""
    coded by HJun -메뉴얼
    라이브 플레이를 위한 코드입니다.
    악기 객체를 생성하고,
    threadinitializer(키배열,노트배열,악기)를 실행하면 Liveplay가 가능합니다
    기본적인 악기 교체는 1, 2번 키를 할당해두었으나, 추후 수정시 간단하게 수정 가능합니다.
    0 누르면 모든 스레드 종료

"""

import keyboard
import pygame
import time
import pygame.midi
import threading
from tkinter import *

# initialize pygame to use

pygame.midi.init()


class KeyboardGUI:
    def __init__(self):
        scales = 1
        root.geometry('{}x200'.format(300 * scales))
        white_keys = 10 * scales
        black = [1, 1, 0, 1, 1, 1, 0, 1, 1] * scales
        root.bind('<Key>', self.pressed)
        for i in range(white_keys):
            self.button = Button(root, bg='white', activebackground='gray87', command=lambda i=i: self.pressed)
            self.button.grid(row=0, column=i * 3, rowspan=2, columnspan=3, sticky='nsew')

        for i in range(white_keys - 1):
            if black[i]:
                self.button = Button(root, bg='black', activebackground='gray12', command=lambda i=i: self.pressed)
                self.button.grid(row=0, column=(i * 3) + 2, rowspan=1, columnspan=2, sticky='nsew')

        for i in range(white_keys * 3):
            root.columnconfigure(i, weight=1)

        for i in range(2):
            root.rowconfigure(i, weight=1)

    def pressed(self, event=None):
        if self in key_list:
            print('hi')

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


def key_input(_key, _note, instrument):
    while True:
        if keyboard.is_pressed(_key):  # 눌릴때
            print("Key pressed!")
            instrument.note_on(_note)
            # player.note_on(60, 127, 1) # 첫 파라미터가 음 60이 도
            while keyboard.is_pressed(_key):
                time.sleep(0.001)
            else:  # 뗄 때
                instrument.note_off(_note)
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
    inst1 = Instrument(2)
    inst2 = Instrument(2)
    thread_initializer(key_list, note_list, inst1)
    thread_initializer(key_list2, note_list, inst2)
    root = Tk()
    keyboardgui = KeyboardGUI()
    root.mainloop()
