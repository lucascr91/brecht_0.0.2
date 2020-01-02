import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import brecht as br
from PIL import ImageTk, Image
from time import sleep


def create_instance(*args):
    global text
    text = br.Text(user_text.get())

def create_file(*args):
    user_input = text_widget.get("1.0", 'end-1c')
    f = open('user_text.txt', 'w')
    f.write(user_input)
    f.close

class Brecht_Master(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('600x400')
        self.title('Brecht 0.0.2')
        self.resizable(False, False)

    #     self.frames = dict()

    #     container = ttk.Frame(self)
    #     container.pack()

    #     for FrameClass in (Loading_Window, Second_Window):
    #         frame = FrameClass(container, self)
    #         self.frames[FrameClass] = frame
    #         frame.grid(row=0, column=0, sticky="NSEW")

    # def show_frame(self, container):
    #     frame = self.frames[container]
    #     frame.tkraise()

class Second_Window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

class Upload_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        #WIDGET LABEL
        open_label = ttk.Label(self, text='Open local file: ')
        open_label.pack(side = 'left')

        #WIDGET ENTRY
        open_entry = ttk.Entry(self, textvariable = user_text, font = ('Segoe UI', 15))
        open_entry.pack(side = 'left', fill = 'x')
        open_entry.focus()

class Text_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        #WIDGET LABEL
        paste_label = ttk.Label(self, text='or paste your text here: ')
        paste_label.pack(side = 'top')

class EnterQuit_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        #BUTTON SEND
        quit_button = ttk.Button(self, text = 'Send text', command = create_file)
        quit_button.pack(side = 'left',  fill = 'x')

        #BUTTON QUIT
        quit_button = ttk.Button(self, text = 'Quit', command = root.destroy)
        quit_button.pack(side = 'left', fill = 'x')

root = Brecht_Master()

user_text = tk.StringVar()


#WIDGET TEXT


font.nametofont('TkDefaultFont').configure(size = 15)

window2 = Second_Window(root)
window2.grid(row=0, column=0, sticky="NSEW")
upload = Upload_Frame(window2)
upload.pack(side ='top')
text_w2 = Text_Frame(window2)
text_widget = tk.Text(text_w2)
text_widget.pack(side = 'top')
text_w2.pack(side ='top')
enter_quit = EnterQuit_Frame(window2)
enter_quit.pack(side = 'top')

#******************LOADING WINDOW***************************

def task():
    sleep(4)
    Loading_Frame.destroy()


Loading_Frame = ttk.Frame(root, padding = (30,5))
Loading_Frame.grid(row=0, column=0, sticky="NSEW")

label = tk.Label(Loading_Frame, text="Loading ...")
label.pack()
img = ImageTk.PhotoImage(Image.open('brecht_drawing.jpg'))
panel = tk.Label(Loading_Frame, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")
Loading_Frame.after(200, task)


 #****************END LOADING WINDOW************************

root.mainloop()

