# Typing Speed Test Program App
from tkinter import *
import random

# variables
time = 60
wpm = 0
cpm = 0
one = 1


# 100 word statements
with open('./100_words.txt') as file:
    statements = file.readlines()
statement = random.choice(statements)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def star_timer(e):
    global time, one, cpm, wpm
    count = 1 * time
    if one == 1:
        count_down(count)
        one += 1
    if e.char != ' ':
        cpm += 1
    else:
        wpm += 1
    wpm_speed.config(text=wpm)
    cpm_speed.config(text=cpm)


def count_down(count):
    global time
    time = count-1
    timer_clock.config(text=time)
    if time > 0:
        window.after(1000, count_down, time)
    else:
        outcome()


def outcome():
    outcome_window = Toplevel()
    outcome_window.minsize(width=200, height=200)
    outcome_window.title("Outcome!")
    outcome_window.configure(bg='white')
    outcome_window.config(padx=80, pady=80)  # padding
    outcome_label = Label(outcome_window, text=f'Great job!, you type with the speed of {wpm} WPM ({cpm} '
                                               f'CPM). It could be better!)', font=('Montserrat', 18, 'bold'),
                          bg='white', wraplength=300)
    outcome_label.grid(column=1, row=1)
    again = Button(outcome_window, text='Try again', height=1, width=8, command=lambda: try_again(outcome_window),
                   borderwidth=2, bg='#4281f5', font=('Montserrat', 14, 'bold'))
    again.grid(column=1, row=2, padx=5,  pady=5,)


def try_again(outcome_window):
    global time, wpm, cpm, one
    outcome_window.destroy()
    time = 60
    wpm = 0
    cpm = 0
    one = 1
    timer_clock.config(text=time)
    wpm_speed.config(text=wpm)
    cpm_speed.config(text=cpm)
    new_statement = random.choice(statements)
    text_to_read.config(text=new_statement)
    text_input.delete(0, END)
    text_input.focus()
    text_input.bind("<Key>", star_timer)


# ---------------------------- UI SETUP ------------------------------- #
# creating a window
window = Tk()
window.title("Typing Speed Test")
window.minsize(width=600, height=600)
window.configure(bg='white')
window.config(padx=100, pady=100)  # padding

# Labels
title_label = Label(text="Test your typing skills", font=('Montserrat ', 40, 'bold'), bg='white')
title_label.grid(column=0, columnspan=5, row=0)
# time label
time_label = Label(text="seconds", font=('Montserrat', 12, 'bold'), bg='white')
time_label.grid(column=1, row=2)
# word per minute
wpm_label = Label(text="word/min", font=('Montserrat', 12, 'bold'), bg='white')
wpm_label.grid(column=2, row=2)
# character per minute
cpm_label = Label(text="chars/min", font=('Montserrat', 12, 'bold'), bg='white')
cpm_label.grid(column=3, row=2)

# text to read
text_to_read = Label(text=f'{statement}', font=('Montserrat', 18, 'normal'), bg='white', wraplength=1000)
text_to_read.grid(column=0, columnspan=5, row=3)

# Input text
text_input = Entry(width=80, font=('Montserrat', 18, 'normal'), bg='white')
text_input.focus()
text_input.grid(column=0, columnspan=5, row=4)
text_input.bind("<Key>", star_timer)

# label results
# time clock
timer_clock = Label(text=f'{time}', font=('Montserrat', 14, 'bold'), bg='white')
timer_clock.grid(column=1, row=1)
# word per minute
wpm_speed = Label(text=f'{wpm}', font=('Montserrat', 14, 'bold'), bg='white')
wpm_speed.grid(column=2, row=1)
# character per minute
cpm_speed = Label(text=f'{cpm}', font=('Montserrat', 14, 'bold'), bg='white')
cpm_speed.grid(column=3, row=1)


window.mainloop()
