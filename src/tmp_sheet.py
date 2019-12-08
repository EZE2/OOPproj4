# -*- coding: utf-8 -*-
import time
import datetime

class note_class:
    def __init__(self):
        self.note_key=0
        self.note_duration=0
        self.time = time.time()
        # after keyboard.is_pressed(key): ,  inst1.note_on(note) && declare note object
        
    def set_key(self,key):
        self.note_key=key
        
    def set_duration(self,duration):
        self.note_duration=duration



class sheet_class:
    def __init__(self):
        self.note_list = list()
        self.instrument=1
        self.time_first_note_pushed=0


    def sheet_clear(self):
        self.note_list = []
        # self.instrument=1     악기 정보는 현재의 악기 정보를 따라가는 게 맞는 것 같아서 놔뒀음.
        self.time_first_note_pushed=0
            
    def set_title(self):
        tmp=input("type the title of the song you will play : " )
        self.title=tmp

    def add_to_sheet(self, note):
        if not self.note_list :
            self.time_first_note_pushed=note.time
            note.time=0
            self.note_list.append(note)
            # we should assemble all notes in order
            # time_first_note_pushed is the time first note making a self.time
            # because time() is not initialized so the starting point is not 0. By using first_note_pushed, it can comfort the time difference
        else :
            note.time=note.time-self.time_first_note_pushed
            self.note_list.append(note)
            
            
# make the sheet to .txt
def making_txt(sheet):
    import os

    BASE_PATH = os.path.dirname(os.path.dirname(__file__))
    now=datetime.datetime.now()
    file_template = now.strftime('%Y_%m_%d_%H_%M_%S.txt')
    file_path = os.path.join(BASE_PATH,'Score',file_template)

    file = open(file_path, 'w', encoding='utf8')
    for i in sheet.note_list:
        time=round(i.time,3)
        if time<0 : time = -time
        line=f'{i.note_key} {i.note_duration} {time}\n'
        file.write(line)
    print("Save txt file!")
    
