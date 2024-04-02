import time
import tkinter


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed")
        self.minsize(width=400, height=600)
        self.resizable(False, False)
        self.timer_count = 61
        self.create_widgets()

    def create_widgets(self):
        self.create_timer()
        self.create_textbox()

    def create_timer(self):
        timer_label = tkinter.Label(text="Timer: ")
        timer_label.grid(row=0, column=0, padx=5, pady=5)
        self.timer = tkinter.Label(text="", fg="red")
        self.timer.grid(row=0, column=1, padx=5, pady=5)
        self.start_btn = tkinter.Button(text="Start!", command=self.start_timer)
        self.start_btn.grid(row=2, column=0, padx=5, pady=5)

    def create_textbox(self):
        self.textbox = tkinter.Text(width=35, height=5)
        self.textbox['state'] = 'disabled'
        self.textbox.grid(row=1, column=0, columnspan=4, padx=7, pady=7)

    def start_timer(self):
        self.timer_count = 60
        self.start_btn['state'] = 'disabled'
        self.textbox['state'] = 'normal'
        self.textbox.delete("1.0", tkinter.END)
        self.timer.configure(text=self.timer_count)
        self.update_timer()

    def update_timer(self):
        if self.timer_count != 0:
            self.timer_count -= 1
            self.timer.configure(text=self.timer_count)
            self.after(1000, self.update_timer)
        else:
            self.calculate_wpm()

    def calculate_wpm(self):
        text_input = self.textbox.get("1.0", 'end-1c')
        words = text_input.split(" ")
        chars = "".join(words)
        words_per_minute = round((len(chars)/5)/1)
        self.display_wpm(words_per_minute)

    def display_wpm(self, wpm):
        popup = tkinter.Toplevel(self)
        popup.title("WPM Score")
        wpm_label = tkinter.Label(popup, text=f"Words per minute: {wpm}")
        wpm_label.pack(pady=20)


app = App()
app.mainloop()