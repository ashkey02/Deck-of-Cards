#Ash Garcia
#02-03-22
#Deck Of Cards

#import libraries
import random
from tkinter import *

#the main GUI
class MainGUI(Frame):
    #the constructer
    def __init__(self, parent):
        #sets up big white screen at the top
        Frame.__init__(self, parent, bg="white")
        #parent.attributes("-fullscreen", True)
        self.setupGUI()

    #sets up the GUI
    def setupGUI(self):
        #the calculator uses the TexGyreAdvento font
        self.display = Label(self, text="", anchor=E, bg="white", fg = "black", height=2, font=("Times", 50))
        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)
        #0-1
        for row in range(2):
            Grid.rowconfigure(self, row, weight=1)
        #0-4
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)

        w = random.randint(1,54)
        x = random.randint(1,54)
        y = random.randint(1,54)
        z = random.randint(1,54)
        
        img = PhotoImage(file="cards/" + str(w) + ".gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white")
        button.image = img
        button.grid(row=0, column=0, sticky=N+S+E+W)

        img = PhotoImage(file="cards/" + str(x) + ".gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white")
        button.image = img
        button.grid(row=0, column=1, sticky=N+S+E+W)

        img = PhotoImage(file="cards/" + str(y) + ".gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white")
        button.image = img
        button.grid(row=0, column=2, sticky=N+S+E+W)

        img = PhotoImage(file="cards/" + str(z) + ".gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white")
        button.image = img
        button.grid(row=0, column=3, sticky=N+S+E+W)

        shuffle = Button(self, text="Shuffle", bg="white", borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process())
        shuffle.grid(row=1, column=1, columnspan=2, sticky=N+S+E+W)

        #pack the GUI
        self.pack(fill=BOTH, expand=0)

    def process(self):
        w = random.randint(1,54)
        x = random.randint(1,54)
        y = random.randint(1,54)
        z = random.randint(1,54)

        img = PhotoImage(file="cards/" + str(w) + ".gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white")
        button.image = img
        button.grid(row=0, column=0, sticky=N+S+E+W)

        img = PhotoImage(file="cards/" + str(x) + ".gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white")
        button.image = img
        button.grid(row=0, column=1, sticky=N+S+E+W)

        img = PhotoImage(file="cards/" + str(y) + ".gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white")
        button.image = img
        button.grid(row=0, column=2, sticky=N+S+E+W)

        img = PhotoImage(file="cards/" + str(z) + ".gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white")
        button.image = img
        button.grid(row=0, column=3, sticky=N+S+E+W)

        shuffle = Button(self, text="Shuffle", bg="white", borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process())
        shuffle.grid(row=1, column=1, columnspan=2, sticky=N+S+E+W)
            
##############################
#the main part of the program#
##############################

#create the window
window = Tk()
#set the window title
window.title("Deck Of Cards")
#generate the GUI
p = MainGUI(window)
#display the GUI and wait for user interaction
window.mainloop()
