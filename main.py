from tkinter import *
import sample
import os

ws = Tk()
ws.geometry('400x300')
ws.title('Testing')
ws['bg']='#5d8a82'

f = ("Times bold", 14)

def speech_page():
    ws.destroy()
    import speech_rec

def sample_page():
    ws.destroy()
    sample.create_text_field()

Label(
    ws,
    text="Test",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Speech Recognition", 
    font=f,
    command=speech_page
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Sample Audio", 
    font=f,
    command=sample_page
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
