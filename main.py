from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#A3DC9A"
YELLOW = "#FFF9BD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

def button_clicked():
    pass

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
title_label = Label(text='Timer', font=(FONT_NAME, 34, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white')
canvas.grid(column=1, row=1)

start_button = Button(text='Start', command=button_clicked)
start_button.grid(column=0, row=2)
reset_button = Button(text='Reset', command=button_clicked)
reset_button.grid(column=2, row=2)

check_marks = Label(text='✔', font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)




window.mainloop()