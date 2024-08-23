from pynput import mouse
from pynput import keyboard
import time
times=int(input('input frequency/60'))
print('{0} times per seceond'.format(str(times*62.5)))
control=mouse.Controller()
def speed_monitor():
    position1=control.position
    time.sleep(0.0001)
    position2=control.position
    speed=((position1[0]-position2[0])**2+(position1[1]-position2[1])**2)**0.5/0.00001
    if speed==0:
        return True
    else:
        return False

def main():
    while 1:
        if speed_monitor():
            control.click(mouse.Button.left,times)
        else:
            print('stop process')
            return None

def key_press(key):
    if key==keyboard.Key.enter:
        return False
with keyboard.Listener(on_press=key_press) as listener:
    listener.join()
main()
