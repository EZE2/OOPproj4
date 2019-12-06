"""
    coded by HJun -硫붾돱�뼹
    �씪�씠釉� �뵆�젅�씠瑜� �쐞�븳 肄붾뱶�엯�땲�떎.
    �븙湲� 媛앹껜瑜� �깮�꽦�븯怨�,
    threadinitializer(�궎諛곗뿴,�끂�듃諛곗뿴,�븙湲�)瑜� �떎�뻾�븯硫� Liveplay媛� 媛��뒫�빀�땲�떎
    湲곕낯�쟻�씤 �븙湲� 援먯껜�뒗 1, 2踰� �궎瑜� �븷�떦�빐�몢�뿀�쑝�굹, 異뷀썑 �닔�젙�떆 媛꾨떒�븯寃� �닔�젙 媛��뒫�빀�땲�떎.
    0 �늻瑜대㈃ 紐⑤뱺 �뒪�젅�뱶 醫낅즺

"""

""" 12.06 EZE2
�뙆�씪 �젙由� �젅�떎�엳 �븘�슂�븿.
�듅�엳 �벐�젅�뵫 愿��젴 �븿�닔 鍮쇨퀬 �굹癒몄��뒗 �쟾遺� �뵲濡� �뙆�씪濡� 鍮쇱빞�븯怨�
�븞�벐�뒗 肄붾뱶�뱾�� 吏��슦怨�, 遺꾨━�븷嫄� 遺꾨━�빐�빞 �븿.

key_input �뿉�꽌 ���옣, �옱�깮, GUI 蹂�寃� 紐⑤몢 泥섎━�븷嫄곗엫.
"""

import keyboard
import pygame
import time
import pygame.midi
import threading
from tkinter import *

# initialize pygame to use

pygame.midi.init()

white_button_list = ['a','s','d','f','g']
black_button_list = ['w', 'e', 'z', 't', 'i']
'''
def key_input():
    while True:
        if keyboard.is_pressed('l'):
            print('l pressed!')
            #time.sleep(0.1)
            #tmp_sheet.add_to_sheet(x_note)
            '''
class WhitePianoButton(Button):

    def makename(self,name):
        self.name = name
        self.isPressed = False

    def update(self):
        if self.isPressed:
            self.isPressed = False
            self.configure(bg="white")
        else:
            self.isPressed = True
            self.configure(bg="red")


class BlackPianoButton(Button):
    def makename(self,name):
        self.name = name
        self.isPressed = False

    def update(self):
        if self.isPressed:
            self.isPressed = False
            self.configure(bg="black")
        else:
            self.isPressed = True
            self.configure(bg="red")



class KeyboardGUI:
    button_list = list()
    def __init__(self):
        scales = 1
        root.geometry('{}x200'.format(300 * scales))
        white_keys = 5 * scales
        black = [1, 1, 0, 1, 1, 1, 0, 1, 1] * scales
        # root.bind('<Key>', pressed)
        for i in range(white_keys):
            self.button = WhitePianoButton(root, bg='white', activebackground='gray87')
            self.button.grid(row=0, column=i * 3, rowspan=2, columnspan=3, sticky='nsew')
            self.button.makename(white_button_list[i])
            KeyboardGUI.button_list.append(self.button)
        
            
        for i in range(white_keys - 1):
            if black[i]:
                self.button = BlackPianoButton(root, bg='black', activebackground='gray12')
                self.button.grid(row=0, column=(i * 3) + 2, rowspan=1, columnspan=2, sticky='nsew')
                self.button.makename(black_button_list[i])
                KeyboardGUI.button_list.append(self.button)

        for i in range(white_keys * 3):
            root.columnconfigure(i, weight=1)

        for i in range(2):
            root.rowconfigure(i, weight=1)


#note_class will make a note obj having a key, duration, played time
class note_class:
    def __init__(self):
        self.note_key=0
        self.note_duration=0
        self.time=time.time()
        # after keyboard.is_pressed(key): ,  inst1.note_on(note) && declare note object
    
    def set_key(self,key):
        self.note_key=key
        
    def set_duration(self,duration):
        self.note_duration=duration

#sheet_class will make a sheet obj that starts with key_input and makes list consisting of note objs
class sheet_class:
    def __init__(self):
        self.note_list = list()
        self.title="title of the song"
        self.set_title()
        self.time_first_note_pushed=0
        
    def add_to_sheet(self, note):
        if not self.note_list :
            self.time_first_note_pushed=note.time
            note.time=0
            self.note_list.append(note)
            # we should assemble all notes in order
            # time_first_note_pushed is the time first note making a self.time
            # because time() is not initialized so the starting point is not 0. By using first_note_pushed, it can comfort the time difference
        else :
            note.time=note.time-self.time_first_note_pushed
            self.note_list.append(note)
            
    def set_title(self):
        tmp=input("type the title of the song you will play : " )
        self.title=tmp

    def get_instrument(self):
        return self.instrument
    

def making_txt(sheet):
    file = open(f'{tmp_sheet.title}.txt', 'w', encoding='utf8')
    for i in tmp_sheet.note_list:
        time=round(i.time,3)
        line=f'{i.note_key} {i.note_duration} {time},3)\n'
        file.write(line)
    
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


midi_dic = {'piano': 2, 'acoustic guitar': 24}  # midi �몴 -1 = �븙湲곕쾲�샇

key_list = ['a', 's', 'd', 'f', 'g', 'q']
key_list2 = ['w', 'e', 't', 'y', 'i', 'q']
note_list = [60, 62, 64, 65, 67]
note_list2 = [61, 63, 66, 68, 70]


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
�씠 �봽濡쒓렇�옩�쓽 �빑�떖 �븿�닔�엫.
key_input �븞�뿉 �븘�슂�븳 湲곕뒫 �떎 吏묒뼱�꽔�쓣 寃�!!
�뙆�씪誘명꽣 異붽��븯�뒗 諛⑹떇�쑝濡� ���옣�룄 �씠嫄몃줈 援ы쁽�븷 寃껋쓣 沅뚯옣�븿.
"""

def key_input(_key,_note,instrument):
    while True:
        if keyboard.is_pressed(_key):
            print("end of sheet")
            making_txt(tmp_sheet)
        elif keyboard.is_pressed('0'):
            return    

def key_input_1(_key, _note, instrument):
    while True:
        tmp_note_1=note_class()
        if keyboard.is_pressed(_key):
            # �닃由대븣
            print("Key pressed!")
            instrument.note_on(_note)
            start_time=round(time.time(),3)
            tmp_note_1.set_key(_key)
            for button in KeyboardGUI.button_list:
                if button.name == _key:
                    button.update()
            # player.note_on(60, 127, 1) # 泥� �뙆�씪誘명꽣媛� �쓬 60�씠 �룄
            while keyboard.is_pressed(_key) : 
                time.sleep(0.001)
            else:  
                instrument.note_off(_note)
                for button in KeyboardGUI.button_list:
                    if button.name == _key:
                        button.update()

            end_time=round(time.time(),3)
            tmp_note_1.set_duration(round(end_time-start_time,3))
            tmp_sheet.add_to_sheet(tmp_note_1)
            
        elif keyboard.is_pressed('0'):
            return


def key_input_2(_key, _note, instrument):
    while True:
        tmp_note_2=note_class()
        if keyboard.is_pressed(_key):
            # �닃由대븣
            print("Key pressed!")
            instrument.note_on(_note)
            start_time=round(time.time(),3)
            tmp_note_2.set_key(_key)
            for button in KeyboardGUI.button_list:
                if button.name == _key:
                    button.update()
            # player.note_on(60, 127, 1) # 泥� �뙆�씪誘명꽣媛� �쓬 60�씠 �룄
            while keyboard.is_pressed(_key) :
                time.sleep(0.001)
            
            else:  # �뾼 �븣
                instrument.note_off(_note)
                for button in KeyboardGUI.button_list:
                    if button.name == _key:
                        button.update()
            
            end_time=round(time.time(),3)
            tmp_note_2.set_duration(round(end_time-start_time,3))
            tmp_sheet.add_to_sheet(tmp_note_2)
   
        elif keyboard.is_pressed('0'):
            return

def key_input_3(_key, _note, instrument):
    while True:
        tmp_note_3=note_class()
        if keyboard.is_pressed(_key):
            # �닃由대븣
            print("Key pressed!")
            instrument.note_on(_note)
            start_time=round(time.time(),3)
            tmp_note_3.set_key(_key)
            for button in KeyboardGUI.button_list:
                if button.name == _key:
                    button.update()
            # player.note_on(60, 127, 1) # 泥� �뙆�씪誘명꽣媛� �쓬 60�씠 �룄
            while keyboard.is_pressed(_key) :
                time.sleep(0.001)
             
            else:  # �뾼 �븣
                instrument.note_off(_note)
                for button in KeyboardGUI.button_list:
                    if button.name == _key:
                        button.update()
            
            end_time=round(time.time(),3)
            tmp_note_3.set_duration(round(end_time-start_time,3))
            tmp_sheet.add_to_sheet(tmp_note_3)

        elif keyboard.is_pressed('0'):
            return

def key_input_4(_key, _note, instrument):
    while True:
        tmp_note_4=note_class()
        if keyboard.is_pressed(_key):
            # �닃由대븣
            print("Key pressed!")
            instrument.note_on(_note)
            start_time=round(time.time(),3)
            tmp_note_4.set_key(_key)
            for button in KeyboardGUI.button_list:
                if button.name == _key:
                    button.update()
            # player.note_on(60, 127, 1) # 泥� �뙆�씪誘명꽣媛� �쓬 60�씠 �룄
            while keyboard.is_pressed(_key) :
                time.sleep(0.001)
            
            else:  # �뾼 �븣
                instrument.note_off(_note)
                for button in KeyboardGUI.button_list:
                    if button.name == _key:
                        button.update()
            
            end_time=round(time.time(),3)
            tmp_note_4.set_duration(round(end_time-start_time,3))
            tmp_sheet.add_to_sheet(tmp_note_4)
            
        elif keyboard.is_pressed('0'):
            return

def key_input_5(_key, _note, instrument):
    while True:
        tmp_note_5=note_class()
        if keyboard.is_pressed(_key):
            # �닃由대븣
            print("Key pressed!")
            instrument.note_on(_note)
            tmp_note_5=note_class()
            start_time=round(time.time(),3)
            tmp_note_5.set_key(_key)
            for button in KeyboardGUI.button_list:
                if button.name == _key:
                    button.update()
            # player.note_on(60, 127, 1) # 泥� �뙆�씪誘명꽣媛� �쓬 60�씠 �룄
            while keyboard.is_pressed(_key) :
                time.sleep(0.001)
                
            else:  # �뾼 �븣
                instrument.note_off(_note)
                for button in KeyboardGUI.button_list:
                    if button.name == _key:
                        button.update()

            end_time=round(time.time(),3)
            tmp_note_5.set_duration(round(end_time-start_time,3))
            tmp_sheet.add_to_sheet(tmp_note_5)

        elif keyboard.is_pressed('0'):
            return

def thread_initializer(_key_list, _note_list, _instrument):
    thread1 = threading.Thread(target=key_input_1, args=(_key_list[0], _note_list[0], _instrument), daemon=True)
    thread2 = threading.Thread(target=key_input_2, args=(_key_list[1], _note_list[1], _instrument), daemon=True)
    thread3 = threading.Thread(target=key_input_3, args=(_key_list[2], _note_list[2], _instrument), daemon=True)
    thread4 = threading.Thread(target=key_input_4, args=(_key_list[3], _note_list[3], _instrument), daemon=True)
    thread5 = threading.Thread(target=key_input_5, args=(_key_list[4], _note_list[4], _instrument), daemon=True)
    thread6 = threading.Thread(target=key_input, args=(_key_list[5], _note_list[4], _instrument), daemon=True)
    thread_inst = threading.Thread(target=change_inst_key, args=(inst1,), daemon=True)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread_inst.start()


# for key, note in key_list, note_list:
#    globals()['thread_{}'.format(key)] = threading.Thread(target=key_input, args=(key, note, inst1))
# �븞���꽕
if __name__ == "__main__":
    root = Tk()
    tmp_sheet=sheet_class()
    keyboardgui = KeyboardGUI()

    inst1 = Instrument(2)
    inst2 = Instrument(2)
    thread_initializer(key_list, note_list, inst1)
    thread_initializer(key_list2, note_list2, inst2)
    root.mainloop()

