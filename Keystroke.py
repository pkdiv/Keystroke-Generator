from pynput.keyboard import Controller, Key, KeyCode
import time

keyboard = Controller()

contents = input("Enter the text :")

time.sleep(6)
characters = r'qwertyuiopasdfghjklzxcvbnm,./;{}1234567890!@#$%^&*()<>"  '

for char in contents:
    try:
        if char == "\n":
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif char == "\t":
            pass
        else:
            keyboard.press(char)
            keyboard.release(char)
        time.sleep(0.1)
    except:
        pass
