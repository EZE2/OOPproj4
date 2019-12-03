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


def inst_key_pressed(inst, inst_name):
    print("change instrument:" + inst_name)
    inst.set_instrument(midi_dic[inst_name])


def change_inst_key(instrument):
    while True:
        if keyboard.is_pressed('1'):
            inst_key_pressed(instrument, 'piano')
        elif keyboard.is_pressed('2'):
            inst_key_pressed(instrument, 'acoustic guitar')


def key_input(key, note, instrument):
    while True:
        if keyboard.is_pressed(key):
            print("q pressed!")
            instrument.note_on(note)
            # player.note_on(60, 127, 1) # 첫 파라미터가 음 60이 도
            while keyboard.is_pressed(key):
                time.sleep(0.01)
        else:
            inst1.note_off(note)
            # player.note_off(60, 127, 1)

key_list = ['q', 'w', 'e', 'r', 't']
for i in key_list:
    globals()['thread_{}'.format(list)]

def key_initializer()

inst1 = Instrument(2)
thread_q = threading.Thread(target=key_input, args=('q', 60, inst1))
thread_w = threading.Thread(target=key_input, args=('w', 62, inst1))
thread_e = threading.Thread(target=key_input, args=('e', 64, inst1))
thread_inst = threading.Thread(target=change_inst_key, args=(inst1,))  # 연산 순서 목적으로 괄호 사용하지 않음

# key_input('q', 60)
thread_q.start()
thread_w.start()
thread_e.start()
thread_inst.start()
