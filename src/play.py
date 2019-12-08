from tkinter import *
from tkinter import filedialog
import pygame.midi
import threading
import time
from operator import itemgetter

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

