from pynput.keyboard import Controller, Key
import argparse
import time

class App:
    def arguments(self):
        parser = argparse.ArgumentParser()
        requiredNamed = parser.add_argument_group('required named arguments')

        requiredNamed.add_argument("-f", "--file", help="Path to text file", dest="file", required=True)
        parser.add_argument("-t", "--time", help="Time to wait before generating keystrokes (in secs)", type=int, dest="time", default=5)
        return parser.parse_args()


    def keystroke(self,contents):
        keyboard = Controller()
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