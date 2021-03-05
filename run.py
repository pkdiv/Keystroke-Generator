from Keystroke.utils import App
import time
import os


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
