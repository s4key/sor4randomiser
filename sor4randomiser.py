import json
from random import choice
from tkinter import *

#Little script to randomise SoR4 survival runs
#Picks a random character then picks random abilities.


class Randomiser:

    def __init__(self):
        with open('sor4randomiser.json') as json_data:
            self.chardict = json.load(json_data)
            json_data.close()

    def picker(self):

        charname = choice(list(self.chardict['characters'].keys()))
        movelist = self.chardict['characters'][charname]
        
        moves = []
        for keyname,valname in movelist.items():
            moves.append((keyname, choice(valname)))
        
        selected = [charname, moves]
        return(selected)


randomiser = Randomiser()

selected = randomiser.picker()
charname = selected[0]
moves = selected[1]

#tkinter stuff
root = Tk()
root.title("Streets of Rage 4 Survival Character Picker")
root.geometry('300x200')

def clicked():
    selected = randomiser.picker()
    charname = selected[0]
    moves = selected[1]
    movelabelcontents = ""
    for moveset,movename in moves:
        movelabelcontents = movelabelcontents + f"{moveset}: {movename}\n"
    charlabel.configure(text=charname)
    movelabel.configure(text=movelabelcontents)

charlabel = Label(root, text=f"")
charlabel.pack()

movelabelcontents = ""
movelabel = Label(root, text=movelabelcontents)
movelabel.pack()
btn = Button(root, text = "Randomise", fg="blue", command=clicked)
btn.place(x=100, y=160)

root.mainloop()
