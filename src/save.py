# by rojong-00
# 이 파일은 음표 클래스와 악보 클래스를 위한 파일입니다
# 키보드 눌림 인풋을 받고 그걸 연주하는 타 파일의 펑션 존재와 함께
# 이것은 그 인풋을 여기 노트 클래스도 받는 경우입니다
# 즉 인풋 시 노트 객체 생성해서 거기에 음높이와 음길이를 받습니다
# 또한 나중에 다시 재생할 때 참고하기 위해 시간도 기록합니다.
# 그리고 그 노트 객체를 쉿 객체에서 애드투쉿으로 받습니다. 쉿객체는 곡 시작 전에 선언 해야.
# 이상 종료
# 그리고 악보 만들 때 필요할 테니 제목과 악기 종류 세팅도 해놓았음
# 위 2개는 쓰려면 곡 시작하기 전에 미리 입력하는 식으로 해야.

import time

# c:\users\default\desktop default file location?

class note_class:
    def __init__(self,key,duration):
        self.note_key=key
        self.note_duration=duration
        self.time = time.time()
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
        self.note_list.append(note)
        if not self.note_list :
            self.time_first_note_pushed=note.time
            # we should assemble all notes in order
            # time_first_note_pushed means the time first note making a self.time
            # time() is not initialized as a starting point is not 0. so by using first_note_pushed, it can comfort the time variable.
            
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
    
    