from tkinter import *
from tkinter import filedialog
import pygame.midi
import threading
import time
from src.live_play import Instrument

pygame.midi.init()


def make_sheet():
    root = Tk()
    root.filename = filedialog.askopenfilename(title="choose txt file",
                                               filetypes=(("text files", "*.txt"), ("all files", "*.*")))

    f = open(root.filename, 'r')
    sheet_list = []
    for item in f.readlines():
        item = item.rstrip()
        point = item.split(' ')
        x = point[0]
        y = point[1]
        z = point[2]
        point_as_array = [x, y, z]
        sheet_list.append(point_as_array)
    #print(sheet_list)
    sheet_list.sort()
    return sheet_list


def rec_play():
    #player = pygame.midi.Output(0)
    a = make_sheet()
    print(a)
    note_list = filter(lambda x: x[0] == 'a', a)
    print(note_list)

'''for i in range(len(note_list)):
        time.sleep(float(note_list[i][2]))
        player.note_on(60, 127, 1)
        time.sleep(float(note_list[i][1]))
        player.note_off(60, 127, 1)'''


if __name__ == "__main__":
    sibal = rec_play()
