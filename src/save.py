# by rojong-00
# �� ������ ��ǥ Ŭ������ �Ǻ� Ŭ������ ���� �����Դϴ�
# Ű���� ���� ��ǲ�� �ް� �װ� �����ϴ� Ÿ ������ ��� ����� �Բ�
# �̰��� �� ��ǲ�� ���� ��Ʈ Ŭ������ �޴� ����Դϴ�
# �� ��ǲ �� ��Ʈ ��ü �����ؼ� �ű⿡ �����̿� �����̸� �޽��ϴ�
# ���� ���߿� �ٽ� ����� �� �����ϱ� ���� �ð��� ����մϴ�.
# �׸��� �� ��Ʈ ��ü�� �� ��ü���� �ֵ��������� �޽��ϴ�. ����ü�� �� ���� ���� ���� �ؾ�.
# �̻� ����
# �׸��� �Ǻ� ���� �� �ʿ��� �״� ����� �Ǳ� ���� ���õ� �س�����
# �� 2���� ������ �� �����ϱ� ���� �̸� �Է��ϴ� ������ �ؾ�.

import time

# c:\users\default\desktop default file location?

class note_class:
    def __init__(self,key,duration):
        self.note_key=key
        self.note_duration=duration
        self.time = round(time.time(),3)
        # after keyboard.is_pressed(key): ,  inst1.note_on(note) && declare note object


class sheet_class:
    def __init__(self):
        self.note_list = list()
        self.title="title of the song"
        self.instrument=1
        self.set_title()
        self.set_instrument()
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
            
    def set_title(self):
        tmp=input("type the title of the song you will play : " )
        self.title=tmp

    def set_instrument(self):
        while True:
            print("choose the instrument you want to play'")
            tmp=int(input("1. accoustic piano     2. grand piano     3.violin     4.ocarina     5. voice      6. xylophone  : " ))
            if tmp==1 : break;
            elif tmp==2 : tmp=3; break
            elif tmp==3 : tmp=41; break
            elif tmp==4 : tmp=80; break
            elif tmp==5 : tmp=54; break
            elif tmp==6 : tmp=14; break
            else :
                print("u chose wrong instrument" )
        self.instrument=tmp
        
    def get_instrument(self):
        return self.instrument
    
    
def making_txt(sheet):
    file = open(f'{tmp_sheet.title}.txt', 'w', encoding='utf8')
    for i in tmp_sheet.note_list:
        line=f'{i.note_key} {i.note_duration} {i.time}\n'
        file.write(line)
    
    