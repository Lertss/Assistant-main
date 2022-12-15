from tkinter import *
import Glos
import Tasks

def ClicText():
    Tasks.makeSomething(txt.get())
    txt.delete(0, END)

def ClicGlos():
    Tasks.makeSomething(Glos.command())

def CommandChar(event):
    if event.char == "\r":
        ClicText()

if __name__ == "__main__":
    window = Tk()
    window.title("Добро пожаловать!")
    window.geometry('350x400')

    window.resizable(False, False)

    lbl = Label(window, text="Привет!")
    lbl.grid(column=0, row=0)

    txt = Entry(window, width=20)
    txt.grid(column=1, row=0)

    btn = Button(window, text="Давай", command=ClicText)
    btn.grid(column=2, row=0)
    window.bind("<Key>", CommandChar)

    # enabling the voice assistant
    bt = Button(window, text="Голосовой помошник", command=ClicGlos)
    bt.grid(column=0, row=4)
    Glos.RunGlos("Привет")

    window.mainloop()
