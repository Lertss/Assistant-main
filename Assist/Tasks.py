import sys
import webbrowser
from tkinter import messagebox

import Glos
# Check the text for compliance
# If the text says that the user said there are words, then run the command

List = [["поиск", "ищи", "найди"], ["ютюб", "видео"], ["пока", "бывай", "стоп"], ["имя"]]

def makeSomething(zadanie):

    if ' '.join(zadanie.split(' ')[:1]) in List[0]:
        #google search
        url = "https://google.com/search?q=" + ' '.join(zadanie.split(' ')[1:])
        webbrowser.get().open(url)
    elif ' '.join(zadanie.split(' ')[:1]) in List[1]:
        #youtube search
        url = "https://www.youtube.com/results?search_query=" + ' '.join(zadanie.split(' ')[1:])
        webbrowser.get().open(url)
    elif ' '.join(zadanie.split(' ')[:1]) in List[2]:
        Glos.RunGlos("Да, конечно, без проблем")
        # Exit the program
        sys.exit()
    elif ' '.join(zadanie.split(' ')[:1]) in List[3]:
        Glos.RunGlos("Меня зовут Катя")
    else:
        #incomprehensible command
        Glos.RunGlos("Простите я не поняла, введите повторно пожалуйста!")
        messagebox.showinfo('Внимание', "Я не могу понять ваш запрос, введите повторно пожалуйста!!")