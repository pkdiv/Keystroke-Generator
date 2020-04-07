from pynput.keyboard import Controller,Key,KeyCode
import time
keyboard = Controller()


with open("file.txt","r") as f:
    contents = f.read()
time.sleep(6)
characters = r'qwertyuiopasdfghjklzxcvbnm,./;{}1234567890!@#$%^&*()<>"  '


for char in contents:
    try:
        if char == "\n":
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif char == "\t":
            pass
            # keyboard.press(Key.space)
            # keyboard.release(Key.space)
            # keyboard.press(Key.space)
            # keyboard.release(Key.space)
            # keyboard.press(Key.space)
            # keyboard.release(Key.space)
            # keyboard.press(Key.space)
            # keyboard.release(Key.space)
        else:
            keyboard.press(char)
            keyboard.release(char)
        time.sleep(0.1)
    except:
        pass
    # elif char == " ":
    #     keyboard.press(Key.space)
    #     keyboard.release(Key.space)
    # else:
    #     keyboard.press(KeyCode.from_char(char))
    #     keyboard.release(KeyCode.from_char(char))


