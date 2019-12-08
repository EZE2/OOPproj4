from tkinter import *
from tkinter import filedialog
import pygame.midi
import threading
import time
from src.live_play import Instrument

pygame.midi.init()


play_key = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76]


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
    print(sheet_list)
    return sheet_list


def rec_play(key):
    note_list = list(filter(lambda x: x[0] == key, a))
    for i in range(len(note_list)):
        time.sleep(float(note_list[i][2]))
        Instrument.note_on(int(note_list[i][0]))
        time.sleep(float(note_list[i][1]))
        Instrument.note_off(int(note_list[i][0]))


'''def p_thread_initializer(play_key):
    p_thread1 = threading.Thread(target=rec_play, args=(play_key[0],), daemon=True)
    p_thread2 = threading.Thread(target=rec_play, args=(play_key[1],), daemon=True)
    p_thread3 = threading.Thread(target=rec_play, args=(play_key[2],), daemon=True)
    p_thread4 = threading.Thread(target=rec_play, args=(play_key[3],), daemon=True)
    p_thread5 = threading.Thread(target=rec_play, args=(play_key[4],), daemon=True)
    p_thread6 = threading.Thread(target=rec_play, args=(play_key[5],), daemon=True)
    p_thread7 = threading.Thread(target=rec_play, args=(play_key[6],), daemon=True)
    p_thread8 = threading.Thread(target=rec_play, args=(play_key[7],), daemon=True)
    p_thread9 = threading.Thread(target=rec_play, args=(play_key[8],), daemon=True)
    p_thread10 = threading.Thread(target=rec_play, args=(play_key[9],), daemon=True)
    p_thread11 = threading.Thread(target=rec_play, args=(play_key[10],), daemon=True)
    p_thread12 = threading.Thread(target=rec_play, args=(play_key[11],), daemon=True)
    p_thread13 = threading.Thread(target=rec_play, args=(play_key[12],), daemon=True)
    p_thread14 = threading.Thread(target=rec_play, args=(play_key[13],), daemon=True)
    p_thread15 = threading.Thread(target=rec_play, args=(play_key[14],), daemon=True)
    p_thread16 = threading.Thread(target=rec_play, args=(play_key[15],), daemon=True)

    p_thread1.start()
    p_thread2.start()
    p_thread3.start()
    p_thread4.start()
    p_thread5.start()
    p_thread6.start()
    p_thread7.start()
    p_thread8.start()
    p_thread9.start()
    p_thread10.start()
    p_thread11.start()
    p_thread12.start()
    p_thread13.start()
    p_thread14.start()
    p_thread15.start()
    p_thread16.start()
'''


if __name__ == "__main__":
    a = make_sheet()
'''    p_thread_initializer(play_key)'''

