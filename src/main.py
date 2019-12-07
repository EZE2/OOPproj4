# -*- coding: utf-8 -*-
"""
    coded by HJun -메뉴얼
    라이브 플레이를 위한 코드입니다.
    악기 객체를 생성하고,
    threadinitializer(키배열,노트배열,악기)를 실행하면 Liveplay가 가능합니다
    기본적인 악기 교체는 1, 2번 키를 할당해두었으나, 추후 수정시 간단하게 수정 가능합니다.
    0 누르면 모든 스레드 종료
"""

""" 12.06 EZE2
파일 정리 절실히 필요함.
특히 쓰레딩 관련 함수 빼고 나머지는 전부 따로 파일로 빼야하고
안쓰는 코드들은 지우고, 분리할건 분리해야 함.
key_input 에서 저장, 재생, GUI 변경 모두 처리할거임.
"""

import keyboard
import time
import pygame.midi
import threading
from live_play import Instrument, key_list2, key_list, note_list, note_list2, midi_dic # live_play 구현부분 모듈화
from GUI import GUIinit, KeyboardGUI, root
#from tmp_sheet import *

# initialize pygame to use
pygame.midi.init()

def inst_key_pressed(instrument, inst_name):
    print("change instrument:" + inst_name)
    instrument.set_instrument(midi_dic[inst_name])

"""
option function:
1, 2번 키로 악기를 변경가능
0번키는 스레딩 종료
녹음, 프로그램 종료, 기타등등의 키입력이 필요한 기능들을 여기다 추가할 것을 권장함
만약 부족한 부분이나, 수정이 필요한 부분이 있을시 저에게 연락주세요(HJun)
"""
def option(instrument):
    while True:
        if keyboard.is_pressed('1'):
            inst_key_pressed(instrument, 'piano')
        elif keyboard.is_pressed('2'):
            inst_key_pressed(instrument, 'acoustic guitar')
        elif keyboard.is_pressed('3'):
            inst_key_pressed(instrument, 'violin')
        elif keyboard.is_pressed('4'):
            inst_key_pressed(instrument, 'whiparam')
        elif keyboard.is_pressed('0'):
            return


"""
key_input function:
이 프로그램의 핵심 함수임.
key_input 안에 필요한 기능 다 집어넣을 것!!
파라미터 추가하는 방식으로 저장도 이걸로 구현할 것을 권장함.
만약 부족한 부분이나, 수정이 필요한 부분이 있을시 저에게 연락주세요(HJun)
"""
def key_input(_key, _note, instrument):
    while True:
        tmp_note=note_class()
        if keyboard.is_pressed(_key):
            # 눌릴때
            print("Key pressed!")
            start_time=round(time.time(),3)
            if _note == 0:
                continue
            else:
                instrument.note_on(_note)
                tmp_note.set_key(_key)
            for button in KeyboardGUI.button_list:
                if button.name == _key:
                    button.update()
            # player.note_on(60, 127, 1) # 첫 파라미터가 음 60이 도
            while keyboard.is_pressed(_key):
                time.sleep(0.001)
            else:  # 뗄 때
                instrument.note_off(_note)
                for button in KeyboardGUI.button_list:
                    if button.name == _key:
                        button.update()
            end_time=round(time.time(),3)
            tmp_note.set_duration(round(end_time-start_time,3))
            tmp_sheet.add_to_sheet(tmp_note)
        elif keyboard.is_pressed('0'):
            return
        else:
            continue


def thread_initializer(_key_list, _note_list, _instrument):
    thread1 = threading.Thread(target=key_input, args=(_key_list[0], _note_list[0], _instrument), daemon=True)
    thread2 = threading.Thread(target=key_input, args=(_key_list[1], _note_list[1], _instrument), daemon=True)
    thread3 = threading.Thread(target=key_input, args=(_key_list[2], _note_list[2], _instrument), daemon=True)
    thread4 = threading.Thread(target=key_input, args=(_key_list[3], _note_list[3], _instrument), daemon=True)
    thread5 = threading.Thread(target=key_input, args=(_key_list[4], _note_list[4], _instrument), daemon=True)
    thread6 = threading.Thread(target=key_input, args=(_key_list[5], _note_list[5], _instrument), daemon=True)
    thread7 = threading.Thread(target=key_input, args=(_key_list[6], _note_list[6], _instrument), daemon=True)
    thread8 = threading.Thread(target=key_input, args=(_key_list[7], _note_list[7], _instrument), daemon=True)
    thread9 = threading.Thread(target=key_input, args=(_key_list[8], _note_list[8], _instrument), daemon=True)
    thread10 = threading.Thread(target=key_input, args=(_key_list[9], _note_list[9], _instrument), daemon=True)
    thread_inst = threading.Thread(target=option, args=(inst1,), daemon=True)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread_inst.start()


if __name__ == "__main__":
    GUIinit()
    tmp_sheet=sheet_class()
    inst1 = Instrument(2)
    inst2 = Instrument(2)
    thread_initializer(key_list, note_list, inst1)
    thread_initializer(key_list2, note_list2, inst2)
    root.mainloop()
