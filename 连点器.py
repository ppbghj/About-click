from pynput import mouse
from pynput import keyboard
import time
f=float(input('please input click frequency'))
control=mouse.Controller()
def speed_monitor():
    position1=control.position
    position2=control.position
    speed=((position1[0]-position2[0])**2+(position1[1]-position2[1])**2)**0.5/0.00001
    if speed==0:
        return True
    else:
        return False

def main():
    while 1:
        if speed_monitor():
            control.click(mouse.Button.left,1)
        else:
            print('stop process')
            time.sleep((1/f)-0.006)
            return None

def key_press(key):
    if key==keyboard.Key.enter:
        return False
with keyboard.Listener(on_press=key_press) as listener:
    listener.join()
main()
    
