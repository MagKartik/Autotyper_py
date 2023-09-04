import pyautogui, time
time.sleep(5)

# pyautogui.hotkey('ctrl', 'A')

# pyautogui.hotkey('shift', 'tab')
with open('temp.txt', 'r') as file:
    data = file.read()
    data = data.replace("  ", "")

with open('temp.txt', 'w') as file:
    file.write(data)

f = open("temp.txt", "r")
for x in f:
    pyautogui.typewrite(x)
# pyautogui.hotkey('ctrl', 'shift', 'end')
#pyautogui.press('delete')