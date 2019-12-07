"""
    coded by HJun -메뉴얼
    라이브 플레이를 위한 코드입니다.
    악기 객체를 생성하고,
    threadinitializer(키배열,노트배열,악기)를 실행하면 Liveplay가 가능합니다
    기본적인 악기 교체는 1, 2번 키를 할당해두었으나, 추후 수정시 간단하게 수정 가능합니다.
    0 누르면 모든 스레드 종료

"""

""" 12.06 EZE2
파일 정리 절실히 필요함.
특히 쓰레딩 관련 함수 빼고 나머지는 전부 따로 파일로 빼야하고
안쓰는 코드들은 지우고, 분리할건 분리해야 함.

key_input 에서 저장, 재생, GUI 변경 모두 처리할거임.
"""

import keyboard
import time
import pygame.midi
import threading
from tkinter import *

pygame.midi.init()


# 버튼 리스트 수동으로 쭉 추가해야 함. 버튼의 이름으로 사용됨.
white_button_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';']
black_button_list = ['q', 'w', 'NULL', 'e', 'r', 't', 'NULL', 'y', 'u']
record_button = ['8']


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
        root.title("Virtual Instruments")
        root.configure(background='white')

        scales = 1
        root.geometry('{}x600'.format(900 * scales))
        white_keys = 10 * scales
        black = [1, 1, 0, 1, 1, 1, 0, 1, 1, 0] * scales
        # root.bind('<Key>', pressed)
        for i in range(white_keys):
            self.button = WhitePianoButton(root, relief='raised', bg='white', bd=3, activebackground='gray87')
            self.button.grid(row=0, column=i * 3, rowspan=2, columnspan=3, sticky='nsew')
            self.button.makename(white_button_list[i])
            KeyboardGUI.button_list.append(self.button)

        for i in range(white_keys - 1):
            if black[i]:
                self.button = BlackPianoButton(root, relief='ridge', bg='black', bd=4, activebackground='gray12')
                self.button.grid(row=0, column=(i * 3) + 2, rowspan=1, columnspan=2, sticky='nsew')
                self.button.makename(black_button_list[i])
                KeyboardGUI.button_list.append(self.button)

        for i in range(white_keys * 3):
            root.columnconfigure(i, weight=1)

        for i in range(2):
            root.rowconfigure(i, weight=1)


class MyFrame:
    def __init__(self):
        right_frame = Button(root, width=15, bg='white')
        right_frame.grid(row=0, column=30, sticky='nsew')
        right_frame['borderwidth'] = 0

        bottom_frame = Button(root, height=15, bg='white')
        bottom_frame.grid(row=4, column=0, sticky='nsew')
        bottom_frame['borderwidth'] = 0


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
    record_button_list = list()

    def __init__(self):
        self.button = RecordButton(root, width=7, height=3, text="RECORD", bg='black', fg='white')
        self.button.grid(row=0, column=30)
        self.button.makename(record_button[0])
        RecordGUI.record_button_list.append(self.button)

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
key_list3 = ['m']
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
                for button in RecordGUI.record_button_list:
                    button.update()
                    if keyboard.is_pressed('m'):
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



