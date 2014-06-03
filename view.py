#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from constants import Range3, Range8, Range16
from Tkinter import Tk, Button, Frame, Label, GROOVE, StringVar, LEFT, BOTH, \
    TOP, BOTTOM, RIGHT, Scrollbar, Text, LabelFrame, Y, END
from tkFileDialog import askopenfilename


class view(Tk):
    
    def mkStringVar(self, s):
        R = StringVar()
        R.set(s)
        return R
    
    def mkLabel(self, f, T, r, c, rs=1, cs=1):
        if isinstance(T, type(StringVar())):
            R = Label(f, textvariable = T, relief=GROOVE, borderwidth=2)
        else:
            R = Label(f, text = T, relief=GROOVE, borderwidth=2)
        R.grid(row=r, column=c, rowspan=rs, columnspan=cs, sticky="wens")
        return R

    def mkLabelList(self, f, SV, r):
        R = []
        for i in range(len(SV)):
            R.append(self.mkLabel(f, SV[i], r, i+1))
        return R

    def mkButton(self, f, t, r, c, rs=1, cs=1):
        R = Button(f, text=t)
        R.grid( row=r, column=c, rowspan=rs, columnspan=cs, sticky="wens")
        return R

# ===== HALT et cetera =========================================================

    def mkHaltArea(self, f):
        self.HALTframe = Frame(f)
        self.HALTframe.config(relief=GROOVE)
        self.HALTframe.config(borderwidth=2)

        self.HALTbutton = Button(self.HALTframe, text = "HALT", width=10)
        self.READMEbutton = Button(self.HALTframe, text = "README", width=10)

        self.HALTbutton.config(borderwidth=2, relief=GROOVE, fg="red")
        self.HALTbutton.config(command = self.quit)
        self.READMEbutton.config(borderwidth=2, relief=GROOVE, fg="red")

        self.HALTbutton.pack(side=LEFT, fill=BOTH)
        self.READMEbutton.pack(side=RIGHT, fill=BOTH)

        self.HALTframe.grid(row=0, column=9, rowspan=1, columnspan=4, sticky="wens")

# ==============================================================================

    def mkProgramControl(self, f):        
        self.PROGRAMCONTROLframe = Frame(f)
        self.PROGRAMCONTROLframe.config(relief=GROOVE)
        self.PROGRAMCONTROLframe.config(borderwidth=2)

        self.runButton = Button(self.PROGRAMCONTROLframe, text="RUN", width=10)
        self.runButton.grid(row=0, column=0, sticky="wens", padx=29, pady=7)

        self.stepButton = Button(self.PROGRAMCONTROLframe, text="STEP", width=10)
        self.stepButton.grid(row=1, column=0, sticky="wens", padx=29, pady=5)

        self.noStepButton = Button(self.PROGRAMCONTROLframe, text="NOSTEP", width=10)
        self.noStepButton.grid(row=2, column=0, sticky="wens", padx=29, pady=7)

        self.PROGRAMCONTROLframe.grid(row=17, column=11, rowspan=6, columnspan=2, sticky="wens")

# ==============================================================================

    def getPGMfileName(self):
        options = {'filetypes': [('pgm files', '.pgm')]}
        f = askopenfilename(**options)
        g = f.split('/')
        self.filenameVar.set(g[len(g) - 1])
        return f

    def mkProgramLoad(self, f):
        self.PROGRAMLOADframe = Frame(f)
        self.PROGRAMLOADframe.config(relief=GROOVE)
        self.PROGRAMLOADframe.config(borderwidth=2)

        self.loadPGMbutton = Button(self.PROGRAMLOADframe, text="Load PGM")
        self.loadPGMbutton.config(width=14)
        self.loadPGMbutton.pack(side=LEFT, fill=BOTH, padx=20, pady=5)
        
        self.filenameVar = StringVar()
        self.filenameVar.set("*****.pgm")
        
        self.fileNameLabel = Label(self.PROGRAMLOADframe, textvariable=self.filenameVar)
        self.fileNameLabel.config(relief=GROOVE, borderwidth=2, width=17)
        self.fileNameLabel.pack(side=RIGHT, fill=BOTH, padx=20, pady=5)

        self.PROGRAMLOADframe.grid(row=15, column=9, rowspan=2, columnspan=4, sticky="wens")

# ==============================================================================

    def mkMemory(self, f):
        self.MEMORYframe = Frame(f)
        self.MEMORYframe.config(relief=GROOVE)
        self.MEMORYframe.config(borderwidth=2)

        E = Frame(self.MEMORYframe)

        self.CLEAR = self.mkButton(E, "ClearMem", 0, 0)
        self.RANDOM = self.mkButton(E, "RandomMem", 0, 1)
        self.READ = self.mkButton(E, "ReadMem", 1, 0)
        self.WRITE = self.mkButton(E, "WriteMem", 1, 1)
        self.BUSTOMEM = self.mkButton(E, "BusToMem", 2, 0, 1, 2)

        F = Frame(self.MEMORYframe)
        
        for i in Range8:
            L = Label(F, textvariable=self.MEMORY[i])
            L.config(relief=GROOVE, borderwidth=2, bg="black", fg="yellow", height=1)
            L.grid(row=0, column=i, sticky="wens", ipadx=5)

        E.pack(side=TOP)
        F.pack(side=BOTTOM)

        self.MEMORYframe.grid(row=18, column=9, rowspan=5, columnspan=2, sticky="wens")

# ==============================================================================

    def mkDataBus(self, f):
        self.DBframe = Frame(f)
        self.DBframe.config(relief=GROOVE)
        self.DBframe.config(borderwidth=2, bg="red")
        self.DBframe.grid(row=0, column=0, rowspan=1, \
                          columnspan=9, sticky="wens")
        
        self.databusLabel = Label(self.DBframe, text="Data\nBus", width=10)
        self.databusLabel.pack(side=LEFT)

        self.DATABUSbuttons = []
        for i in Range8:
            b = Button(self.DBframe, textvariable=self.DATABUS[i])
            b.pack(side=LEFT, fill=BOTH)
            self.DATABUSbuttons.append(b)

    def mkAddressBus(self, f):
        self.ABframe = Frame(f)
        self.ABframe.config(relief=GROOVE)
        self.ABframe.config(borderwidth=2, bg="red")
        self.ABframe.grid(row=26, column=0, rowspan=1, columnspan=13, sticky="wens")
        
        self.AddressBusLabel = Label(self.ABframe, text="Address\nBus", width=12)
        self.AddressBusLabel.pack(side=LEFT)
        
        self.ADDRESSBUSbuttons = []
        for i in Range16:
            b = Button(self.ABframe, textvariable=self.ADDRESSBUS[i])
            b.pack(side=LEFT, fill=BOTH, ipadx=2)
            self.ADDRESSBUSbuttons.append(b)

# ==============================================================================

    def mkALU(self, f):
        self.ALUframe = Frame(f)
        self.ALUframe.config(relief=GROOVE)
        self.ALUframe.config(borderwidth=2)
        
        self.mkFunctionChoice(self.ALUframe)
        self.mkStates(self.ALUframe)
        
        self.ALUframe.grid(row=23, column=9, rowspan=3, columnspan=4, sticky="wens")
        
    def mkFunctionChoice(self, f):
        self.FUNCTIONframe = Frame(f)
        self.FUNCTIONframe.config(relief=GROOVE)
        self.FUNCTIONframe.config(borderwidth=2)

        self.F0label = Label(self.FUNCTIONframe, text="F0", borderwidth=2, relief=GROOVE)
        self.F0label.grid(row=0, column=0, sticky="wens", padx=5)

        self.F1label = Label(self.FUNCTIONframe, text="F1", borderwidth=2, relief=GROOVE)
        self.F1label.grid(row=0, column=1, sticky="wens", padx=8)

        self.F2label = Label(self.FUNCTIONframe, text="F2", borderwidth=2, relief=GROOVE)
        self.F2label.grid(row=0, column=2, sticky="wens", padx=5)

        self.FUNCTIONbuttons = []

        self.F0button = Button(self.FUNCTIONframe)
        self.F0button.config(textvariable=self.FUNCTION[0], borderwidth=2, relief=GROOVE)
        self.F1button = Button(self.FUNCTIONframe)
        self.F1button.config(textvariable=self.FUNCTION[1], borderwidth=2, relief=GROOVE)
        self.F2button = Button(self.FUNCTIONframe)
        self.F2button.config(textvariable=self.FUNCTION[2], borderwidth=2, relief=GROOVE)

        self.FUNCTIONbuttons.append(self.F0button)        
        self.FUNCTIONbuttons.append(self.F1button)
        self.FUNCTIONbuttons.append(self.F2button)

        for i in Range3:
            self.FUNCTIONbuttons[i].grid(row=1, column=i, sticky="wens", padx=5)

        self.FUNCTIONframe.pack(side=LEFT, padx=8, pady=3)

    def mkStates(self, f):
        self.STATESframe = Frame(f)
        self.STATESframe.config(relief=GROOVE)
        self.STATESframe.config(borderwidth=2)

        self.CARRYtag = Label(self.STATESframe, text = " carry ", borderwidth=2, relief=GROOVE)
        self.CARRYtag.grid(row=0, column=0, padx=5, pady=2, sticky="wens")
        
        self.ZEROtag = Label(self.STATESframe, text =  "  zero ", borderwidth=2, relief=GROOVE)
        self.ZEROtag.grid(row=0, column=1, padx=5, pady=1, sticky="wens")
        
        self.SIGNtag = Label(self.STATESframe, text =  "  sign ", borderwidth=2, relief=GROOVE)
        self.SIGNtag.grid(row=0, column=2, padx=5, pady=2, sticky="wens")

        self.CARRY = self.mkStringVar("0")
        self.ZERO  = self.mkStringVar("0")
        self.SIGN  = self.mkStringVar("0")
        
        self.CARRYlabel = Label(self.STATESframe, textvariable = self.CARRY, borderwidth=2, relief=GROOVE)
        self.CARRYlabel.grid(row=1, column=0, padx=5, pady=2, sticky="wens")
        
        self.ZEROlabel = Label(self.STATESframe, textvariable = self.ZERO, borderwidth=2, relief=GROOVE)
        self.ZEROlabel.grid(row=1, column=1, padx=5, pady=1, sticky="wens")
        
        self.SIGNlabel = Label(self.STATESframe, textvariable = self.SIGN, borderwidth=2, relief=GROOVE)
        self.SIGNlabel.grid(row=1, column=2, padx=5, pady=2, sticky="wens")
        
        self.STATESframe.pack(side=RIGHT, padx=8, pady=3)

# ==============================================================================
        
    def mkTagLabels(self, f):
        self.ALabel          = self.mkLabel(f, "A",             1, 0)
        self.BLabel          = self.mkLabel(f, "B",             2, 0)
        self.BLabel.config(bg="black", fg="yellow")
        self.CLabel          = self.mkLabel(f, "C",             3, 0)
        self.CLabel.config(bg="black", fg="yellow")
        self.DLabel          = self.mkLabel(f, "D",             4, 0)
        self.M1Label         = self.mkLabel(f, "M1",            5, 0)
        self.M2Label         = self.mkLabel(f, "M2",            6, 0)
        self.XLabel          = self.mkLabel(f, "X",             7, 0)
        self.YLabel          = self.mkLabel(f, "Y",             8, 0)
        self.J1Label         = self.mkLabel(f, "J1",            9, 0)
        self.J2Label         = self.mkLabel(f, "J2",           10, 0)
        self.PC1Label        = self.mkLabel(f, "PC1",          11, 0)
        self.PC2Label        = self.mkLabel(f, "PC2",          12, 0)
        self.Inc1Label       = self.mkLabel(f, "Inc1",         13, 0)
        self.Inc2Label       = self.mkLabel(f, "Inc2",         14, 0)
        self.IncUnit1Label   = self.mkLabel(f, "IncUnit1",     15, 0)
        self.IncUnit2Label   = self.mkLabel(f, "IncUnit2",     16, 0)
        self.InstLabel       = self.mkLabel(f, "Inst",         17, 0)
        self.addLabel        = self.mkLabel(f, "ADD",          18, 0)
        self.incLabel        = self.mkLabel(f, "INC",          19, 0)
        self.andLabel        = self.mkLabel(f, "AND",          20, 0)
        self.orLabel         = self.mkLabel(f, "OR",           21, 0)
        self.xorLabel        = self.mkLabel(f, "XOR",          22, 0)
        self.notLabel        = self.mkLabel(f, "NOT",          23, 0)
        self.shlLabel        = self.mkLabel(f, "SHL",          24, 0)
        self.clrLabel        = self.mkLabel(f, "CLR",          25, 0)

        self.functionTagLabelDictionary = { (0,0,0) : self.addLabel, \
                                 (0,0,1) : self.incLabel, \
                                 (0,1,0) : self.andLabel, \
                                 (0,1,1) : self.orLabel, \
                                 (1,0,0) : self.xorLabel, \
                                 (1,0,1) : self.notLabel, \
                                 (1,1,0) : self.shlLabel, \
                                 (1,1,1) : self.clrLabel \
                                 }

        for i in self.functionTagLabelDictionary.values():
            i.config(bg="black", fg="yellow")

# ==============================================================================

    def mkRegisterStringVars(self):
        self.FUNCTION   = [ self.mkStringVar("0") for unused_i in Range3 ]
        self.DATABUS    = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.Inst       = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.A          = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.B          = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.C          = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.D          = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.M1         = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.M2         = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.X          = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.Y          = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.J1         = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.J2         = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.PC1        = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.PC2        = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.Inc1       = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.Inc2       = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.IncUnit1   = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.IncUnit2   = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.Add        = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.Inc        = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.And        = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.Or         = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.Xor        = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.Not        = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.Shl        = [ self.mkStringVar("0") for unused_i in Range8 ] 
        self.Clr        = [ self.mkStringVar("0") for unused_i in Range8 ]
        self.ADDRESSBUS = [ self.mkStringVar("0") for unused_i in Range16 ]
        self.MEMORY     = [ self.mkStringVar("0") for unused_i in Range8 ]

# ==============================================================================

    def setRegisterLabelColor(self, L, bc, fc="black"):
        for i in L:
            i.config(bg=bc, fg=fc)
    
    def mkRegisterLabels(self, f):
        self.Alabels        = self.mkLabelList(f, self.A,           1)
        self.setRegisterLabelColor(self.Alabels, "gray90")
        self.Blabels        = self.mkLabelList(f, self.B,           2)
        self.setRegisterLabelColor(self.Blabels, "black", "yellow")
        self.Clabels        = self.mkLabelList(f, self.C,           3)
        self.setRegisterLabelColor(self.Clabels, "black", "yellow")
        self.Dlabels        = self.mkLabelList(f, self.D,           4)
        self.setRegisterLabelColor(self.Dlabels, "gray90")
        self.M1labels       = self.mkLabelList(f, self.M1,          5)
        self.setRegisterLabelColor(self.M1labels, "gray90")
        self.M2labels       = self.mkLabelList(f, self.M2,          6)
        self.setRegisterLabelColor(self.M2labels, "gray90")
        self.Xlabels        = self.mkLabelList(f, self.X,           7)
        self.setRegisterLabelColor(self.Xlabels, "gray90")
        self.Ylabels        = self.mkLabelList(f, self.Y,           8)
        self.setRegisterLabelColor(self.Ylabels, "gray90")

        self.J1labels       = self.mkLabelList(f, self.J1,          9)
        self.J2labels       = self.mkLabelList(f, self.J2,         10)
        self.PC1labels      = self.mkLabelList(f, self.PC1,        11)
        self.PC2labels      = self.mkLabelList(f, self.PC2,        12)
        
        self.Inc1labels     = self.mkLabelList(f, self.Inc1,       13)
        self.setRegisterLabelColor(self.Inc1labels, "gray95")
        self.Inc2labels     = self.mkLabelList(f, self.Inc2,       14)
        self.setRegisterLabelColor(self.Inc2labels, "gray95")

        self.IncUnit1labels = self.mkLabelList(f, self.IncUnit1,   15)
        self.setRegisterLabelColor(self.IncUnit1labels, "gray95")
        self.IncUnit2labels = self.mkLabelList(f, self.IncUnit2,   16)
        self.setRegisterLabelColor(self.IncUnit2labels, "gray95")
        
        self.Instlabels     = self.mkLabelList(f, self.Inst,       17)
        
        self.addlabels      = self.mkLabelList(f, self.Add,        18)
        self.setRegisterLabelColor(self.addlabels, "black", "red")
        self.inclabels      = self.mkLabelList(f, self.Inc,        19)
        self.setRegisterLabelColor(self.inclabels, "black", "yellow")
        self.andlabels      = self.mkLabelList(f, self.And,        20)
        self.setRegisterLabelColor(self.andlabels, "black", "yellow")
        self.orlabels       = self.mkLabelList(f, self.Or,         21)
        self.setRegisterLabelColor(self.orlabels, "black", "yellow")
        self.xorlabels      = self.mkLabelList(f, self.Xor,        22)
        self.setRegisterLabelColor(self.xorlabels, "black", "yellow")
        self.notlabels      = self.mkLabelList(f, self.Not,        23)
        self.setRegisterLabelColor(self.notlabels, "black", "yellow")
        self.shllabels      = self.mkLabelList(f, self.Shl,        24)
        self.setRegisterLabelColor(self.shllabels, "black", "yellow")
        self.clrlabels      = self.mkLabelList(f, self.Clr,        25)
        self.setRegisterLabelColor(self.clrlabels, "black", "yellow")
        
        self.functionLabelsDictionary = { (0,0,0) : self.addlabels, \
                                 (0,0,1) : self.inclabels, \
                                 (0,1,0) : self.andlabels, \
                                 (0,1,1) : self.orlabels, \
                                 (1,0,0) : self.xorlabels, \
                                 (1,0,1) : self.notlabels, \
                                 (1,1,0) : self.shllabels, \
                                 (1,1,1) : self.clrlabels \
                                 }

# ===== Load & Select ==========================================================

    def mkLoad8Buttons(self, f):
        self.loadA    = self.mkButton(f, "load A",     1, 9, 1, 2)
        self.loadB    = self.mkButton(f, "load B",     2, 9, 1, 2)
        self.loadC    = self.mkButton(f, "load C",     3, 9, 1, 2)
        self.loadD    = self.mkButton(f, "load D",     4, 9, 1, 2)
        self.loadM1   = self.mkButton(f, "load M1",    5, 9, 1, 2)
        self.loadM2   = self.mkButton(f, "load M2",    6, 9, 1, 2)
        self.loadX    = self.mkButton(f, "load X",     7, 9)
        self.loadY    = self.mkButton(f, "load Y",     8, 9)
        self.loadJ1   = self.mkButton(f, "load J1",    9, 9, 1, 2)
        self.loadJ2   = self.mkButton(f, "load J2",   10, 9, 1, 2)

        self.loadInst = self.mkButton(f, "load Inst", 17, 9, 1, 2)


    def mkLoad16Buttons(self, f):
        self.loadXY  = self.mkButton(f, "load XY",    7, 10, 2, 1)
        self.loadPC  = self.mkButton(f, "load PC",   11,  9, 2, 2)
        self.loadINC = self.mkButton(f, "load INC",  13,  9, 2, 2)

    def mkSelect8Buttons(self, f):
        self.selectA    = self.mkButton(f, "select A",    1, 11, 1, 2)
        self.selectB    = self.mkButton(f, "select B",    2, 11, 1, 2)
        self.selectC    = self.mkButton(f, "select C",    3, 11, 1, 2)
        self.selectD    = self.mkButton(f, "select D",    4, 11, 1, 2)
        self.selectM1   = self.mkButton(f, "select M1",   5, 11)
        self.selectM2   = self.mkButton(f, "select M2",   6, 11)
        self.selectX    = self.mkButton(f, "select X",    7, 11)
        self.selectY    = self.mkButton(f, "select Y",    8, 11)

    def mkSelect16Buttons(self, f):
        self.selectM   = self.mkButton(f, "select M",    5, 12, 2, 1)
        self.selectXY  = self.mkButton(f, "select XY",   7, 12, 2, 1)
        self.selectJ   = self.mkButton(f, "select J",    9, 11, 2, 2)
        self.selectPC  = self.mkButton(f, "select PC",  11, 11, 2, 2)
        self.selectINC = self.mkButton(f, "select INC", 13, 11, 2, 2)

# ===== System Messages ========================================================

    def mkMessageArea(self, f):
        self.text = Text(f, height=36, width=64)
        self.text.configure(font=("Courier", 11, "bold"), bg="black", fg="green")
        self.scroll = Scrollbar(f, command = self.text.yview)        
        self.text.configure(yscrollcommand = self.scroll.set)
        
        self.text.pack(side=LEFT, padx=3, pady=2)
        self.scroll.pack(side=RIGHT, fill=Y, padx=3, pady=2)

    def addText(self, text):
        self.text.insert(END, text + "\n")
        self.text.yview(END)

# ===== Initialization =========================================================

    def __init__(self):
        Tk.__init__(self)
        
        self.title("Virtual Machine")
        self.config(bg="blue")

        self.registers = LabelFrame(self, bg="blue")
        self.registers.config(relief=GROOVE)
        self.registers.config(borderwidth=2)
        self.registers.config(text = "Virtual Machine: controls and states")
        self.registers.config(labelanchor = "nw")
        self.registers.pack(side = LEFT, fill=BOTH)
        
        self.mkRegisterStringVars()
        
        self.mkTagLabels(self.registers)
        self.mkDataBus(self.registers)
        
        self.mkRegisterLabels(self.registers)
        
        self.mkLoad8Buttons(self.registers)
        self.mkLoad16Buttons(self.registers)
        self.mkSelect8Buttons(self.registers)
        self.mkSelect16Buttons(self.registers)
        
        self.mkAddressBus(self.registers)
        
        self.mkALU(self.registers)
        self.mkMemory(self.registers)
        self.mkProgramLoad(self.registers)
        self.mkProgramControl(self.registers)
        self.mkHaltArea(self.registers)

        self.messages = LabelFrame(self, bg="blue")
        self.messages.config(relief=GROOVE)
        self.messages.config(borderwidth=2)
        self.messages.config(text = "Virtual Machine: system messages")
        self.messages.config(labelanchor = "nw")
        self.messages.pack(side = RIGHT, fill=BOTH)

        self.mkMessageArea(self.messages)

# ===== Testing ================================================================

if __name__ == '__main__':
    f = view()
    f.mainloop()

        


