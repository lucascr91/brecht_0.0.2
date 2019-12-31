from tkinter import *  
import sys
from random import randint

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = 10
y = 10

def key(event):
    if event.char == 'c':
        xloc = randint(0, 100)
        yloc = randint(0, 100)
        T.mark_set("insert", "%d.%d" % (0, 0))
        T.insert('%d.%d' % (xloc, yloc), 'something')

    if event.char == 'q':
        sys.exit()


canvas = Canvas(width=100, height=100, bg='white')
canvas.focus_set()
canvas.bind("<Key>", key)
canvas.pack(expand=YES, fill=BOTH)

T = Text(canvas, height=screen_height, width=screen_width, bg="white", fg="blue")
T.mark_set("insert", "%d.%d" % (0, 0))
T.pack()

root.mainloop()