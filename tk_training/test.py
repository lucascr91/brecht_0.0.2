from tkinter import *
import tkinter.font as font

class Window:
    def __init__(self):
        root = Tk()
        #print(font.families())  # print list of what's available
        root.title("Serial Connection Program")

        self.mainFrame = Frame(root)
        self.mainFrame.pack()

        for font_style in list(font.families()):    
            def_font=font.Font(family=font_style)
            self.portLabel = Label(self.mainFrame, text=font_style, font=def_font)
            self.portLabel.pack()

        root.mainloop()

win = Window()