
import time

class note_class:
    def __init__(self):
        self.note_key=0
        self.note_duration=0
        self.time = time.time()
        if self.time<0 : self.time=-(self.time)
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
    file = open(f'{tmp_sheet.title}.txt', 'w', encoding='utf8')
    for i in tmp_sheet.note_list:
        time=round(i.time,3)
        line=f'f{i.note_key} {i.note_duration} {i.time}'
        file.write(line)
    
