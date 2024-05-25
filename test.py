import pyautogui

b  =True

while b:
    print('a')
    if(pyautogui.press('enter')):
        b = False


