import json
from random import choice
from tkinter import *
from functools import partial

#Little script to randomise SoR4 survival runs
#Picks a random character then picks random abilities.


class Randomiser:

    def __init__(self):
        with open('sor4randomiser.json') as json_data:
            self.chardict = json.load(json_data)
            json_data.close()

    def picker(self, gamefilter):
        moves = []
        if gamefilter[0] == "" and gamefilter[1] == "" and gamefilter[2] == "" and gamefilter[3] == "":
            charname= "No filter selected"
            moves.append(("Please select a filter and randomise again.", ""))
            selected = [charname, moves]
            return(selected)
        filterselect = 0
        while filterselect == 0:
            charname = choice(list(self.chardict['characters'].keys()))
            if charname.split(" ")[1] in gamefilter:
                filterselect = 1
        
        movelist = self.chardict['characters'][charname]
        
        for keyname,valname in movelist.items():
            moves.append((keyname, choice(valname)))
        
        selected = [charname, moves]
        return(selected)


randomiser = Randomiser()

#tkinter stuff
root = Tk()
root.title("Streets of Rage 4 Survival Character Picker")
root.geometry('600x400')

def clicked():
    selected = randomiser.picker(gamefilter)
    charname = selected[0]
    moves = selected[1]
    if charname == "Dr_Zan SOR3":
        charname = charname.replace("_", ". ")
    movelabelcontents = ""
    for moveset,movename in moves:
        movelabelcontents = movelabelcontents + f"{moveset}: {movename}\n"
    charlabel.configure(text=charname)
    movelabel.configure(text=movelabelcontents)

def chbox(gamefilter, game):
    if game == "sor1":
        if sor1filter.get() == 1:
            gamefilter[0] = "SOR1"
        elif sor1filter.get() == 0:
            gamefilter[0] = ""
    
    if game == "sor2":
        if sor2filter.get() == 1:
            gamefilter[1] = "SOR2"
        elif sor2filter.get() == 0:
            gamefilter[1] = ""

    if game == "sor3":
        if sor3filter.get() == 1:
            gamefilter[2] = "SOR3"
        elif sor3filter.get() == 0:
            gamefilter[2] = ""
    
    if game == "sor4":
        if sor4filter.get() == 1:
            gamefilter[3] = "SOR4"
        elif sor4filter.get() == 0:
            gamefilter[3] = ""

gamefilter = ["SOR1", "SOR2", "SOR3", "SOR4"]
sor1filter = IntVar()
sor2filter = IntVar()
sor3filter = IntVar()
sor4filter = IntVar()

selected = randomiser.picker(gamefilter)
charname = selected[0]
moves = selected[1]

#These are the variables for the checkboxes. They need to be created before the check boxes

filterlabel = Label(root, text="Filters:")
filterlabel.place(x=450, y=10)

sor1filterbox = Checkbutton(root, text="SoR 1", variable=sor1filter, onvalue=1, offvalue=0, command=partial(chbox, gamefilter, "sor1"))
sor1filterbox.select()
sor1filterbox.place(x=450, y=50)

sor2filterbox = Checkbutton(root, text="SoR 2", variable=sor2filter, onvalue=1, offvalue=0, command=partial(chbox, gamefilter, "sor2"))
sor2filterbox.select()
sor2filterbox.place(x=450, y=80)

sor3filterbox = Checkbutton(root, text="SoR 3", variable=sor3filter, onvalue=1, offvalue=0, command=partial(chbox, gamefilter, "sor3"))
sor3filterbox.select()
sor3filterbox.place(x=450, y=110)

sor4filterbox = Checkbutton(root, text="SoR 4", variable=sor4filter, onvalue=1, offvalue=0, command=partial(chbox, gamefilter, "sor4"))
sor4filterbox.select()
sor4filterbox.place(x=450, y=140)

chartitlelabel = Label(root, text="Character: ")
chartitlelabel.place(x=20, y=10)

charlabel = Label(root, text=f"")
charlabel.place(x=120, y=10)

movelabelcontents = ""
movelabel = Label(root, text=movelabelcontents, justify=LEFT)
movelabel.place(x=20, y=50)

btn = Button(root, text = "Randomise", fg="blue", command=partial(clicked))
btn.config(height=1, width=10)
btn.place(x=240, y=360)

root.mainloop()
