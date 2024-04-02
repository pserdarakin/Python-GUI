import time
import tkinter

window = tkinter.Tk()
window.title("Typing Speed")
window.minsize(width=400, height=600)


Sample_text = "create typing speed gui test"

text_label = tkinter.Label(window, text=Sample_text)
text_label.pack(pady=20)

text_entry = tkinter.Text(window, height=10, width=50)
text_entry.pack(pady=20)

start_button = tkinter.Button(window,text="Start Test", command=lambda: start_test())
start_button.pack(pady=20)


def start_test():
    timer = time.time()
    if time.time() - timer > 2:
        test_finished = tkinter.Label(window, text="Test finished")
        test_finished.pack(pady=20)


window.mainloop()