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
        
        #This section is all the initalisation for the interface and the buttons/filters
        self.root = Tk()
        self.root.title("Streets of Rage 4 Survival Randomiser")
        self.root.geometry('600x400')

        #These are the variables for the filter check boxes. These need declared before the check boxes are created.
        self.sor1filter = IntVar()
        self.sor2filter = IntVar()
        self.sor3filter = IntVar()
        self.sor4filter = IntVar()

        self.filterlabel = Label(self.root, text="Filters:")
        self.filterlabel.place(x=450, y=10)

        self.sor1filterbox = Checkbutton(self.root, text="SoR 1", variable=self.sor1filter, onvalue=1, offvalue=0, command=partial(self.chbox, "sor1"))
        self.sor1filterbox.select()
        self.sor1filterbox.place(x=450, y=50)

        self.sor2filterbox = Checkbutton(self.root, text="SoR 2", variable=self.sor2filter, onvalue=1, offvalue=0, command=partial(self.chbox, "sor2"))
        self.sor2filterbox.select()
        self.sor2filterbox.place(x=450, y=80)

        self.sor3filterbox = Checkbutton(self.root, text="SoR 3", variable=self.sor3filter, onvalue=1, offvalue=0, command=partial(self.chbox, "sor3"))
        self.sor3filterbox.select()
        self.sor3filterbox.place(x=450, y=110)

        self.sor4filterbox = Checkbutton(self.root, text="SoR 4", variable=self.sor4filter, onvalue=1, offvalue=0, command=partial(self.chbox, "sor4"))
        self.sor4filterbox.select()
        self.sor4filterbox.place(x=450, y=140)

        self.chartitlelabel = Label(self.root, text="Character: ")
        self.chartitlelabel.place(x=20, y=10)

        self.charlabel = Label(self.root, text=f"")
        self.charlabel.place(x=120, y=10)

        self.movelabelcontents = ""
        self.movelabel = Label(self.root, text=self.movelabelcontents, justify=LEFT)
        self.movelabel.place(x=20, y=50)

        self.btn = Button(self.root, text = "Randomise", fg="blue", command=self.clicked)
        self.btn.config(height=1, width=10)
        self.btn.place(x=240, y=360)
        #end gui intiialisation

        self.gamefilter = ["SOR1", "SOR2", "SOR3", "SOR4"] # List for the filters. Used to select which games to select characters from,

        self.moves = [] # List to hold the moves for the selected character
        self.charname = "" # String to hold the name of the selected character

        self.root.mainloop() #Run the main loop

    def picker(self):
        self.moves.clear() # Clear the moves list to prepare it for the new data
        if self.gamefilter[0] == "" and self.gamefilter[1] == "" and self.gamefilter[2] == "" and self.gamefilter[3] == "":
            self.charname= "No filter selected"
            self.moves.append(("Please select a filter and randomise again.", ""))
            return()
        filterselect = 0
        while filterselect == 0:
            self.charname = choice(list(self.chardict['characters'].keys()))
            if self.charname.split(" ")[1] in self.gamefilter:
                filterselect = 1
        
        movelist = self.chardict['characters'][self.charname]
        
        for keyname,valname in movelist.items():
            self.moves.append((keyname, choice(valname)))
    
    def clicked(self): #Method that runs when the "Randomise" button is clicked
        self.picker()
        if self.charname == "Dr_Zan SOR3":
            self.charname = self.charname.replace("_", ". ")
        movelabelcontents = ""
        for moveset,movename in self.moves:
            movelabelcontents = movelabelcontents + f"{moveset}: {movename}\n"
        self.charlabel.configure(text=self.charname)
        self.movelabel.configure(text=movelabelcontents)

    def chbox(self, game):
        if game == "sor1":
            if self.sor1filter.get() == 1:
                self.gamefilter[0] = "SOR1"
            elif self.sor1filter.get() == 0:
                self.gamefilter[0] = ""
        
        if game == "sor2":
            if self.sor2filter.get() == 1:
                self.gamefilter[1] = "SOR2"
            elif self.sor2filter.get() == 0:
                self.gamefilter[1] = ""

        if game == "sor3":
            if self.sor3filter.get() == 1:
                self.gamefilter[2] = "SOR3"
            elif self.sor3filter.get() == 0:
                self.gamefilter[2] = ""
        
        if game == "sor4":
            if self.sor4filter.get() == 1:
                self.gamefilter[3] = "SOR4"
            elif self.sor4filter.get() == 0:
                self.gamefilter[3] = ""

randomiser = Randomiser()
