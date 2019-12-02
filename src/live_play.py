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


def key_input(key, note):
    while True:
        if keyboard.is_pressed(key):
            print("q pressed!")
            inst1.note_on(note)
            # player.note_on(60, 127, 1) # 첫 파라미터가 음 60이 도
            time.sleep(0.1)
            while keyboard.is_pressed(key):
                time.sleep(0.1)
        else:
            inst1.note_off(note)
            # player.note_off(60, 127, 1)


inst1 = Instrument(1)
thread1 = threading.Thread(target=key_input, args=('q', 60))
thread2 = threading.Thread(target=key_input, args=('w', 62))
thread3 = threading.Thread(target=key_input, args=('e', 64))

# key_input('q', 60)
thread1.start()
thread2.start()
thread3.start()