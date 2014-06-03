#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from constants import Range8, Range16, setSV
from model import model
from view import view


class control:

    def Paint(self):
        setSV(self.V.FUNCTION, self.M.FUNCTION)
        
        self.V.ZERO.set(str(self.M.ZERO))
        self.V.CARRY.set(str(self.M.CARRY))
        self.V.SIGN.set(str(self.M.SIGN))

        setSV(self.V.DATABUS, self.M.DATABUS)
        setSV(self.V.ADDRESSBUS, self.M.ADDRESSBUS)
        
        setSV(self.V.A, self.M.A)
        setSV(self.V.B, self.M.B)
        setSV(self.V.C, self.M.C)
        setSV(self.V.D, self.M.D)
        setSV(self.V.M1, self.M.M1)
        setSV(self.V.M2, self.M.M2)
        setSV(self.V.X, self.M.X)
        setSV(self.V.Y, self.M.Y)
        
        setSV(self.V.J1, self.M.J1)
        setSV(self.V.J2, self.M.J2)
        setSV(self.V.PC1, self.M.PC1)
        setSV(self.V.PC2, self.M.PC2)
        
        setSV(self.V.Inst, self.M.Inst)
        
        setSV(self.V.Inc1, self.M.Inc1)
        setSV(self.V.Inc2, self.M.Inc2)
        setSV(self.V.IncUnit1, self.M.IncUnit1)
        setSV(self.V.IncUnit2, self.M.IncUnit2)

        # This changes the color of the current and old functions.
        oldF = tuple(self.M.oldFUNCTION)
        oldR = self.V.functionLabelsDictionary[oldF]
        self.V.setRegisterLabelColor(oldR, "black", "yellow")
        currentF = tuple(self.M.FUNCTION)
        currentR = self.V.functionLabelsDictionary[currentF]
        self.V.setRegisterLabelColor(currentR, "black", "red")

        oldL = self.V.functionTagLabelDictionary[oldF]
        oldL.config(fg = "yellow")
        currentL = self.V.functionTagLabelDictionary[currentF]
        currentL.config(fg = "red")

        setSV(self.V.Add, self.M.ADD)
        setSV(self.V.Inc, self.M.INC)
        setSV(self.V.And, self.M.AND)
        setSV(self.V.Or, self.M.OR)
        setSV(self.V.Xor, self.M.XOR)
        setSV(self.V.Not, self.M.NOT)
        setSV(self.V.Shl, self.M.SHL)
        setSV(self.V.Clr, self.M.CLR)
        
        setSV(self.V.MEMORY, self.M.getMEMORY())
        
        c = "red" if self.M.NOSTEP == True else "black"
        self.V.noStepButton.config(fg=c)

# ===== Load, Select & Function ================================================

    def mkFunction(self):
        self.V.F0button.config(command = self.M.updateF0)
        self.V.F1button.config(command = self.M.updateF1)
        self.V.F2button.config(command = self.M.updateF2)

    def mkLoad(self):
        self.V.loadA.config(command = self.M.loadA)
        self.V.loadB.config(command = self.M.loadB)
        self.V.loadC.config(command = self.M.loadC)
        self.V.loadD.config(command = self.M.loadD)
        self.V.loadM1.config(command = self.M.loadM1)
        self.V.loadM2.config(command = self.M.loadM2)
        self.V.loadX.config(command = self.M.loadX)
        self.V.loadY.config(command = self.M.loadY)
        self.V.loadJ1.config(command = self.M.loadJ1)
        self.V.loadJ2.config(command = self.M.loadJ2)
        self.V.loadInst.config(command = self.M.loadInst)
        self.V.loadXY.config(command = self.M.loadXY)
        self.V.loadPC.config(command = self.M.loadPC)
        self.V.loadINC.config(command = self.M.loadINC)

    def mkSelect(self):
        self.V.selectA.config(command = self.M.selectA)
        self.V.selectB.config(command = self.M.selectB)
        self.V.selectC.config(command = self.M.selectC)
        self.V.selectD.config(command = self.M.selectD)
        self.V.selectM1.config(command = self.M.selectM1)
        self.V.selectM2.config(command = self.M.selectM2)
        self.V.selectX.config(command = self.M.selectX)        
        self.V.selectY.config(command = self.M.selectY)

        self.V.selectINC.config(command = self.M.selectINC)
        self.V.selectJ.config(command = self.M.selectJ)
        self.V.selectM.config(command = self.M.selectM)
        self.V.selectPC.config(command = self.M.selectPC)
        self.V.selectXY.config(command = self.M.selectXY)

# ===== Buses ==================================================================

    def mkDatabus(self):
        for i in Range8:
            c = lambda x = i : self.M.setDATABUSpart(x)            
            self.V.DATABUSbuttons[i].config(command = c)

    def mkAddressbus(self):
        for i in Range16:
            c = lambda x = i : self.M.setADDRESSBUSpart(x)            
            self.V.ADDRESSBUSbuttons[i].config(command = c)

# ===== Memory =================================================================

    def mkMemory(self):
        self.V.CLEAR.config(command =  self.M.clearMemory)
        self.V.RANDOM.config(command = self.M.randomMemory)
        self.V.READ.config(command = self.M.readMemoryToDatabus)
        self.V.WRITE.config(command = self.M.writeDatabusToMemory)
        self.V.BUSTOMEM.config(command = self.M.addressbusToMemoryAddress)

# ===== Load Program ===========================================================

    def getAndSetPGM(self):
        filename = self.V.getPGMfileName()
        self.M.loadPGMtoMEM(filename)

    def mkPGM(self):
        self.V.loadPGMbutton.config(command = self.getAndSetPGM)

# ===== System Messages ========================================================

    def systemMessage(self, m):
        self.V.addText(m)

# ===== Program Controls =======================================================

    def mkProgramControls(self):
        self.V.runButton.config(command = self.M.run)
        self.V.stepButton.config(command = self.M.step)
        self.V.noStepButton.config(command = self.M.noStep)

# ===== HALT et cetera =========================================================

    def loadREADME(self):
        readmefile = open("README", "r")
        
        for LINE in readmefile:
            self.V.addText(LINE[0:len(LINE) - 1])

        readmefile.close()

    def mkHALT(self):
        self.V.READMEbutton.config(command = self.loadREADME)

# ===== Initialization =========================================================

    def __init__(self):

        self.M = model()
        self.V = view()

        self.M.setPaintCallback(self.Paint)
        self.M.setMessageCallback(self.systemMessage)

        self.mkLoad()
        self.mkSelect()
        self.mkFunction()
        self.mkDatabus()
        self.mkAddressbus()
        self.mkMemory()
        self.mkPGM()
        self.mkProgramControls()
        self.mkHALT()

        self.Paint()

        m = "\n\n                    WELCOME TO VIRTUAL MACHINE\n"
        m = m + "                       Memory: " + str(len(self.M.MEMORY.values())) + " bytes\n"
        m = m + "  ==========================================================\n"
        m = m + "Press README on left...."


        self.systemMessage(m)

        self.V.mainloop()

# ===== Testing ================================================================

if __name__ == '__main__':
    control()











