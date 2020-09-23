import pyautogui
import time

def login():
    time.sleep(3)
    f = open("Logininfo.txt", "r")
    m = (f.readlines(1))
    n = (f.readlines(2))

    f = str(m)
    g = str(n)
    
    print(n)
    print(m)
    pyautogui.write(f)



login()
['ArcazAdedventure1\n']