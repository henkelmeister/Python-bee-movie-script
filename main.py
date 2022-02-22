# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
import pyautogui

def runProg():
    # Use a breakpoint in the code line below to debug your script.
    f = open('gistfile1.txt', 'r')
    print("Hello, writing will commence in...")
    for x in range(5, 0, -1):
        print(x)
        time.sleep(1)
    count = 10
    for line in f.readlines():
        if len(line.split()) < 1:
            continue
        pyautogui.write(line, interval=0.02)
        time.sleep(0.5)
        pyautogui.press('enter')
        print(line.strip())
        count -= 1
        if count < 1:
            break



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runProg()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
