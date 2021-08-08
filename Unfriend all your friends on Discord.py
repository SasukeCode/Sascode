import time
import pyautogui

friends = 3

for i in range(friends):
    pyautogui.click(1349, 254)
    pyautogui.click(1463, 371)
    time.sleep(0.5)
    pyautogui.click(1154, 606)
    time.sleep(0.5)
    
print("Done")