from tkinter.ttk import Label, Button, Entry, Scrollbar
from tkinter import Text
import time
from Keystroke.utils import App


class GUI:
    def __init__(self, master):
        
        # Configuring the main window
        self.master = master
        master.title("Keystroke Generator")
        master.geometry('720x480')
        self.create_start_label()
        self.create_text_area()
        self.press_delay()
        self.submit_button()

    def create_start_label(self):
        # Preliminary text (perhaps instructions)
        self.intro_label = Label(
            self.master,
            text="Welcome to KeyStroke Generator!",
            anchor='center'
        )
        self.intro_label.grid(row=0, pady=(20,40))
        self.intro_label.config(font =("Arial", 11))
        # self.label.pack(fill='both')

        self.enter_text_label = Label(self.master, text='Enter the text to be copied.')
        self.enter_text_label.grid(row=1,pady=(20,30))


    def create_text_area(self):
        self.textbox = Text(self.master, height = 10, width = 79, wrap = 'word')
        vertscroll = Scrollbar(self.master)
        vertscroll.config(command=self.textbox.yview)
        self.textbox.config(yscrollcommand=vertscroll.set)
        self.textbox.grid(column=0, row=1, padx=(30,0))
        vertscroll.grid(column=2, row=1, sticky='NSE')
        
    def submit_button(self):
        self.submit = Button(self.master, text='Submit', command=self.generate_strokes)
        self.submit.grid(column=0, row=4,padx=(30,0),pady=(30,0))

        #self.submit=Button(self.master, text="Submit", command=self.master.quit)
        #self.submit.grid(column=0, row=2)

    def generate_strokes(self):
        app = App()
        # args = app.arguments()
        # if not (os.path.isfile(args.file)):
        #     print("Invalid file path")

        for secs in range(int(self.delay_time_text.get('1.0','end-1c')), 0, -1):
            print(f"\rStarting keystrokes in {secs} seconds", end="")
            time.sleep(1)
        print("\rKeystrokes started" + " "*20)

        # with open(args.file, "r") as inp_file:
        #     file_text = inp_file.read()
        #     app.keystroke(file_text)
        file_text = self.textbox.get('1.0','end-1c')
        app.keystroke(file_text)
        print("Done")

    def press_delay(self):
        self.delay_time_label = Label(self.master, text='Enter the delay in seconds:')
        self.delay_time_label.grid(column=0,row=2,padx=(30,0),pady=(20,0), sticky='W')
        
        self.delay_time_text = Text(self.master,height = 1, width = 20, wrap = 'word')
        self.delay_time_text.grid(column=0,row=3,padx=(30,0),pady=(10,0), sticky='W')