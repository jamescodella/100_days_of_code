from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text='Timer')
    canvas.itemconfig(time_left,text=f'00:00')
    check_marks.config(text='', bg=YELLOW)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    '''
    Initializes timer and updates title label with session title
    '''
    global reps
    reps +=1

    work_time = WORK_MIN * 60
    short_time = SHORT_BREAK_MIN * 60
    long_time = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        countdown(work_time)
        title_label.config(text='Work ', fg=GREEN)
 
    elif reps % 8 == 0:
        countdown(long_time )
        title_label.config(text='Break ☕️', fg=RED)
    else:
        countdown(short_time)
        title_label.config(text='Break 🚶', fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    '''
    Decreases time, tracks timer object, and displays check marks for completed sessions
    '''
    sec = count % 60
    min = count // 60
    if sec < 10:
        sec = '0' + str(sec)


    canvas.itemconfig(time_left,text=f'{min}:{sec}')
    if count > 0:
        global timer
        timer =  window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:   
            check_marks.config(text='✅'*(reps//2), bg=YELLOW)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title('Pymodoro')
window.config(padx=20, pady=20, bg=YELLOW)


# Pomodoro image and time remaining
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=pomodoro_image)
time_left = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1,row=1)

# Buttons

start_button = Button(text='Start', command=start_timer, bd=0,borderwidth=0, highlightthickness=0, border=0, padx=0, pady=0)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset', command=reset_timer, bd=0,borderwidth=0, highlightthickness=0, border=0, padx=0, pady=0)
reset_button.grid(column=2,row=2)

# Labels
check_marks = Label(text='', bg=YELLOW)
check_marks.grid(column=1, row=4)

title_label = Label(text = 'Timer',bg=YELLOW, font=("Helvetica", 30, 'normal'))
title_label.grid(column=1, row=0)

window.mainloop()