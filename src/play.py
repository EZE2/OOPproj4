from tkinter import *
from tkinter import filedialog
import pygame.midi
import threading
import time
from src.live_play import key_note_dic
from main import inst1

pygame.midi.init()


_key = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'w', 'e', 't', 'y', 'u', 'o', 'p', '.', '.', '.']
root = Tk()


def make_sheet():

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



# def rec_play():
#     #player = pygame.midi.Output(0)
#     a = make_sheet()
#     print(a)
#     note_list = filter(lambda x: x[0] == 'a', a)
#     print(note_list)
#

'''for i in range(len(note_list)):
        time.sleep(float(note_list[i][2]))
        player.note_on(60, 127, 1)
        time.sleep(float(note_list[i][1]))
        player.note_off(60, 127, 1)'''


def rec_play(key, a):

    note_list = list(filter(lambda x: x[0] == key, a))
    if note_list:
        for i in note_list:
            tmp_note = key_note_dic[i[0]]
            print(tmp_note)
            time.sleep(float(i[2]))
            inst1.note_on(note=key_note_dic[i[0]])
            time.sleep(float(i[1]))
            inst1.note_off(note=key_note_dic[i[0]])


def p_thread_initializer(key, a):
    p_thread1 = threading.Thread(target=rec_play, args=(key[0], a), daemon=True)
    p_thread2 = threading.Thread(target=rec_play, args=(key[1], a), daemon=True)
    p_thread3 = threading.Thread(target=rec_play, args=(key[2], a), daemon=True)
    p_thread4 = threading.Thread(target=rec_play, args=(key[3], a), daemon=True)
    p_thread5 = threading.Thread(target=rec_play, args=(key[4], a), daemon=True)
    p_thread6 = threading.Thread(target=rec_play, args=(key[5], a), daemon=True)
    p_thread7 = threading.Thread(target=rec_play, args=(key[6], a), daemon=True)
    p_thread8 = threading.Thread(target=rec_play, args=(key[7], a), daemon=True)
    p_thread9 = threading.Thread(target=rec_play, args=(key[8], a), daemon=True)
    p_thread10 = threading.Thread(target=rec_play, args=(key[9], a), daemon=True)
    p_thread11 = threading.Thread(target=rec_play, args=(key[10], a), daemon=True)
    p_thread12 = threading.Thread(target=rec_play, args=(key[11], a), daemon=True)
    p_thread13 = threading.Thread(target=rec_play, args=(key[12], a), daemon=True)
    p_thread14 = threading.Thread(target=rec_play, args=(key[13], a), daemon=True)
    p_thread15 = threading.Thread(target=rec_play, args=(key[14], a), daemon=True)
    p_thread16 = threading.Thread(target=rec_play, args=(key[15], a), daemon=True)
    p_thread17 = threading.Thread(target=rec_play, args=(key[16], a), daemon=True)
    # p_thread18 = threading.Thread(target=rec_play, args=(key[17]), daemon=True)
    # p_thread19 = threading.Thread(target=rec_play, args=(key[18]), daemon=True)
    # p_thread20 = threading.Thread(target=rec_play, args=(key[19]), daemon=True)

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
    p_thread17.start()
    # p_thread18.start()
    # p_thread19.start()
    # p_thread20.start()


def play_load_score():
    a = make_sheet()
    p_thread_initializer(_key, a)
if __name__ == "__main__":

    p_thread_initializer(_key)
    root.mainloop()
