import threading
import keyboard
import pygame
import time
import pygame.midi

pygame.midi.init()
player = pygame.midi.Output(1)
player.set_instrument(1, 1)


def key_input(key):
    while True:
        if keyboard.is_pressed(key):
            print("q pressed!")
            player.note_on(60, 127, 1) # 첫 파라미터가 음
            time.sleep(0.1)
            while keyboard.is_pressed(key):
                time.sleep(0.1)
        else:
            player.note_off(60, 127, 1)



major=[0,4,7,12]

def go(note):
    player.note_on(note, 127,1)
    player.note_off(note,127,1)

def arp(base,ints):
    for n in ints:
        go(base+n)

def chord(base, ints):
    player.note_on(base,127,1)
    player.note_on(base+ints[1],127,1)
    player.note_on(base+ints[2],127,1)
    player.note_on(base+ints[3],127,1)
    time.sleep(1)
    player.note_off(base,127,1)
    player.note_off(base+ints[1],127,1)
    player.note_off(base+ints[2],127,1)
    player.note_off(base+ints[3],127,1)
def end():
       pygame.quit()


#thread1 = threading.Thread(target=a.key_input)
#thread1.start()
key_input('q')