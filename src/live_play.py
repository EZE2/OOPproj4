import keyboard
import pygame
import time
import pygame.midi
import threading

# initialize pygame to use

pygame.midi.init()

#class KeyInputManager:
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
inst1 = Instrument(2)
inst2 = Instrument(2)

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


def key_input(_key, _note, instrument):
    while True:
        if keyboard.is_pressed(_key):   # 눌릴때
            print("Key pressed!")
            instrument.note_on(_note)
            # player.note_on(60, 127, 1) # 첫 파라미터가 음 60이 도
            while keyboard.is_pressed(_key):
                time.sleep(0.001)
            else:                           # 뗄 때
                instrument.note_off(_note)


def thread_initializer(_key_list, _note_list, _instrument):
    thread1 = threading.Thread(target=key_input, args=(_key_list[0], _note_list[0], _instrument))
    thread2 = threading.Thread(target=key_input, args=(_key_list[1], _note_list[1], _instrument))
    thread3 = threading.Thread(target=key_input, args=(_key_list[2], _note_list[2], _instrument))
    thread4 = threading.Thread(target=key_input, args=(_key_list[3], _note_list[3], _instrument))
    thread5 = threading.Thread(target=key_input, args=(_key_list[4], _note_list[4], _instrument))
    thread_inst = threading.Thread(target=change_inst_key, args=(inst1,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread_inst.start()


#for key, note in key_list, note_list:
#    globals()['thread_{}'.format(key)] = threading.Thread(target=key_input, args=(key, note, inst1))
# 안대네
if __name__ == "__main__":
    thread_initializer(key_list, note_list, inst1)
    thread_initializer(key_list2, note_list, inst2)