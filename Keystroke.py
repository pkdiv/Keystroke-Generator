from pynput.keyboard import Controller, Key
import time
import argparse
import os

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


if __name__ == '__main__':
    app = App()
    args = app.arguments()
    if not (os.path.isfile(args.file)):
        print("Invalid file path")

    for secs in range(args.time, 0, -1):
        print(f"\rStarting keystrokes in {secs} seconds", end="")
        time.sleep(1)
    print("\rKeystrokes started" + " "*20)

    with open(args.file, "r") as inp_file:
        file_text = inp_file.read()
        app.keystroke(file_text)
    print("Done")
