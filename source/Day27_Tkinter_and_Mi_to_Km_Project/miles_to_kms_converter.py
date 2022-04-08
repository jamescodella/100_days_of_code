from tkinter import *

# Global var with conversion from mi to km
conversation_mult = 1.60934

def convert(miles):
    '''
    convert input from one unit to the other
    '''
    print(conversation_mult)
    label_result['text'] = round(miles * conversation_mult,2)

def conversion(val):
    '''
    change conversion units from mi to km
    '''
    global conversation_mult
    if val == 1:
        conversation_mult = 1.60934
        label_top['text'] = 'mi'
        label_bottom['text'] = 'km'

    else:
        conversation_mult = 1.0/1.60934 
        label_top['text'] = 'km'
        label_bottom['text'] = 'mi'

# Window setup
window = Tk()
window.title('Miles to Kilometers Converter')
window.minsize(width=300, height = 130)
window.maxsize(width=300, height = 130)
window.config(padx=20, pady=20)

# Labels
label_eq = Label(text='is equal to')
label_eq.grid(column=0, row=2)

label_top = Label(text='mi')
label_top.grid(column=2, row=1)

label_bottom = Label(text='km')
label_bottom.grid(column=2, row=2)

radio_label = Label(text='Convert to:')
radio_label.grid(column=0, row=0)

label_result = Label(text='')
label_result.grid(column=1, row=2)

# Entry
entry = Entry(width=10, text=0)
entry.grid(column=1, row=1)

# Button
calc_button = Button(text='Calculate', command = lambda: convert(float(entry.get())))
calc_button.grid(column=1, row=4)

# Radio buttons
radio_state = IntVar()
km_radio = Radiobutton(text='Km', value=1, variable=radio_state, command=lambda: conversion(radio_state.get()))
km_radio.grid(column=1, row=0)
mi_radio = Radiobutton(text='mi', value=2, variable=radio_state, command=lambda: conversion(radio_state.get()))
mi_radio.grid(column=2, row=0)

window.mainloop()