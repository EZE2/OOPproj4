import threading
import time
import keyboard
#keyboard 모듈 필요 pip3 install keyboard


def key_input():
    while True:
        if keyboard.is_pressed('q'):
            print('q pressed!')
            time.sleep(0.2)

def key_input2():
    while True:
        if keyboard.is_pressed('x'):
            print('x pressed!')
            time.sleep(0.2)


keythread = threading.Thread(target=key_input)
keythread2 = threading.Thread(target=key_input2)
keythread.start()
keythread2.start()