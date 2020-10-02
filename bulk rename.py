import os
from tkinter import *


def rename():
    folder = r''+path.get()
    counter = 1

    for filename in os.listdir(folder):
        os.rename(folder + '//' + filename, folder + '//' + word.get() + str(counter) + exe.get())
        counter = counter+1

    ent.delete(0, END)
    ent1.delete(0, END)


root = Tk()
root.title('BULK RENAMER')
root.geometry('300x200')

path = StringVar()

Label(root, text='PASTE FOLDER PATH HERE', font=('TIMES NEW ROMAN', 12)).pack()
ent = Entry(root, textvariable=path, font=('TIMES NEW ROMAN', 12))
ent.pack()

word = StringVar()
Label(root, text='NEW WORD', font=('TIMES NEW ROMAN', 12)).pack()
ent1 = Entry(root, textvariable=word, font=('TIMES NEW ROMAN', 12))
ent1.pack()

exe = StringVar()
Label(root, text='ENTER FILE EXTENSION', font=('TIMES NEW ROMAN', 12)).pack()
ent1 = Entry(root, textvariable=exe, font=('TIMES NEW ROMAN', 12))
ent1.pack()

Button(root, text='RENAME', command=rename).pack()
Label(root, text='CODED BY VARUN HERLEKAR', font=('TIMES NEW ROMAN', 8)).pack()
