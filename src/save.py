import time

#timer start whem push the key?
#c:\users\default\desktop default file location?

class note_class:
    def __init__(self,key,interval):
        self.note_key=key
        self.note_interval=interval
        self.time = time.time()
        '''
        event_key to key
        interval is length of the note
        '''

class sheet_class:
    def __init__(self):
        self.note_list = list()
        self.title="title of the song : "
        self.instrument=1
        self.set_title()
        self.set_instrument()
        

    def add_to_sheet(self, note):
        if len(self.note_list)==0 :
            self.note_list[0] = note
        else :
            self.note_list.append(note)

    def set_title(self):
        tmp=input("type the title of the song you will play")
        self.title=tmp

    def set_instrument(self):
        print("choose the instrument you wanna play'")
        tmp=input("1.piano'\n' 2.violin '\n' 3.orcarina '\n' 4. voice '\n' : ")
        if tmp==1 : pass
        elif tmp==2 : tmp=41
        elif tmp==3 : tmp=80
        elif tmp==4 : tmp=54
        else :
            print("u chosed wrong instrument")

        self.instrument=tmp
        
    def get_instrument(self):
        return self.instrument