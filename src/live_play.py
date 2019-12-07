# -*- coding: utf-8 -*-
import time
import pygame.midi

pygame.midi.init()

# parameter for key_input function and threading
midi_dic = {'piano': 2, 'acoustic guitar': 24}  # midi 표 -1 = 악기번호

key_list = ['a', 's', 'd', 'f', 'g']
key_list2 = ['w', 'e', 't', 'y', 'i']
note_list = [60, 62, 64, 65, 67]
note_list2 = [61, 63, 66, 68, 70]


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
