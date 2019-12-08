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
        point = item.split(' ')
        x = point[0]
        y = point[1]
        z = point[2]
        point_as_array = [x, y, z]
        sheet_list.append(point_as_array)
    #print(sheet_list)
    return sheet_list

def rec_play(_key, _note):
    a = make_sheet()
    note_list = list(filter(lambda x: x == key, a))

    for i in range(len(note_list)):
        time.sleep(float(note_list[i][2]))
        Instrument.note_on(_note)
        time.sleep(float(note_list[i][1]))
        Instrument.note_off(_note)