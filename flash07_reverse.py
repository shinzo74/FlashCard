import csv
from tkinter import *
import tkinter.font as font
from tkmacosx import Button
import random


f = open('data/lastKanji.csv', 'r')

reader = csv.reader(f)

lista = {}

for row in reader:
    lista[row[1]] = row[2]

root = Tk()

root.title("Kanji Flashcard")
root.resizable(False, False)

myFont = font.Font(family="Helvetica", size=200, weight='bold')
myFont2 = font.Font(family="Helvetica", size=30, weight='bold')

frame1 = Frame(root, width=500, height=300)
frame1.grid(row=0, column=0, pady=30)
frame2 = Frame(root)
frame2.grid(row=1, column=0)
frame3 = Frame(root)
frame3.grid(row=2, column=0, padx=30, pady=20)

random_kanji = 1000


def flip_kanji():
    global random_kanji
    if random_kanji != 1000:
        global label_words
        label_kanji.config(text=nuovo_kanji, fg='black')



def next_kanji():
    if len(lista) > 0:
        global label_kanji
        global random_kanji
        random_kanji = random.randint(0, (len(lista)-1))
        selected_kanji = list(lista.values())[random_kanji]
        label_words.config(text=selected_kanji)
        label_kanji.config(text="?", fg='red')
        global nuovo_kanji
        nuovo_kanji = list(lista.keys())[random_kanji]
        lista.pop(nuovo_kanji)

label_kanji = Label(frame1, text="気", font=myFont)
label_kanji.grid(row=0, column=0, columnspan=5)
label_words = Label(frame2, text="soul, spirit", font=myFont2)
label_words.grid(row=0, column=0, columnspan=5)

flip_button = Button(frame3, text="Flip!", padx=50, pady=10, bg='#ADEFD1', fg='#00203F', borderless=1,
                     command=flip_kanji, font=myFont2)
flip_button.grid(row=0, column=0, padx=10)
next_button = Button(frame3, text="Next", padx=50, pady=10, bg='#E69A8D', fg='#00203F', borderless=1,
                     activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', command=next_kanji,
                     font=myFont2)
next_button.grid(row=0, column=1)

root.mainloop()

