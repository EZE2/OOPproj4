import keyboard
import pygame
import time
import pygame.midi
import threading
from tkinter import *

pygame.midi.init()

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