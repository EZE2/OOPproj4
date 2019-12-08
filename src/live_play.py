# -*- coding: utf-8 -*-
import time
import pygame.midi

pygame.midi.init()

# parameter for key_input function and threading
midi_dic = {'piano': 2, 'acoustic guitar': 24, 'violin': 40, 'whiparam': 78}  # midi 표 -1 = 악기번호

key_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';']
key_list2 = ['w', 'e', 't', 'y', 'u', 'o', 'p', '.', '.', '.']
note_list = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76]
note_list2 = [61, 63, 66, 68, 70, 73, 75, 0, 0, 0]

key_list_all = key_list + key_list2
note_list_all = note_list + note_list2

key_note_dic = dict(zip(key_list_all,note_list_all))



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
