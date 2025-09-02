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

        #Main window
        self.root = Tk()
        self.root.title("Streets of Rage 4 Survival Randomiser")
        self.root.geometry("280x300")

        #Filter frame
        self.filterframe = LabelFrame(self.root, text="Filters:")
        self.filterframe.pack(fill="both")

        #Character frame
        self.charframe = LabelFrame(self.root, text="Character:")
        self.charframe.pack(fill="both", expand="yes")

        self.gamefilter = ["SOR1", "SOR2", "SOR3", "SOR4"] # List for the filters. Used to select which games to select characters from
        self.gamenumbers = (1, 2, 3, 4)
        self.filter=[]
        for game in self.gamenumbers:
            self.filter.append(BooleanVar(value=True))

        self.filterboxes=[]

        for game in self.gamenumbers:
            self.filterboxes.append(Checkbutton(self.filterframe, text=f"SoR {game}", variable=self.filter[game-1], onvalue=True, offvalue=False, command=self.chbox))

        for boxes in self.filterboxes:
            boxes.select()
            boxes.pack(side=LEFT)

        self.charlabel = Label(self.charframe, text=f"", font="bold")
        self.charlabel.pack()

        self.movelabelcontents = ""
        self.movelabel = Label(self.charframe, text=self.movelabelcontents, justify=LEFT)
        self.movelabel.pack()

        self.btn = Button(self.root, text = "Randomise", fg="blue", command=self.clicked)
        self.btn.config(height=1, width=10)
        self.btn.pack(fill="both")
        #end gui intiialisation

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

    def chbox(self):
        self.gamefilter.clear()
        for count, game in enumerate(self.filter):
            if game.get() == True:
                self.gamefilter.append(f"SOR{count+1}")
            else:
                self.gamefilter.append("")

randomiser = Randomiser()
