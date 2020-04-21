import tkinter as tk

window = tk.Tk()
window.title("Timer")


def countdown(count):
    mins, secs = divmod(count, 60)
    if mins >= 60:
        hours, mins = divmod(mins, 60)
    else:
        hours = 0
    label1['text'] = str(hours).zfill(2) + ":" + str(mins).zfill(2) + ":" + str(secs).zfill(2)
    if count > 0:
        window.after(1000, countdown, count - 1)


label1 = tk.Label(window, justify='center', font=("arial", 40))
label1.pack()
# Timer in seconds
countdown(7210)
window.mainloop()

# TODO
# user input
# notification when time finishes
