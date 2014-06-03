#!/usr/bin/python2.7


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


from constants import Range8, Egnar8, Egnar16, listToList, \
    listToLists, listsToList, RangeMEM
from random import randint
from thread import start_new_thread
#from _thread import start_new_thread
#import threading


class model:
    
# ===== Load ===================================================================
    
    def loadA(self):
        self.setMessage("load A")
        listToList(self.DATABUS, self.A)
        self.paintView()

    def loadB(self):
        self.setMessage("load B")
        listToList(self.DATABUS, self.B)
        self.updateALU()
        self.paintView()

    def loadC(self):
        self.setMessage("load C")
        listToList(self.DATABUS, self.C)
        self.updateALU()
        self.paintView()

    def loadD(self):
        self.setMessage("load D")
        listToList(self.DATABUS, self.D)
        self.paintView()

    def loadM1(self):
        self.setMessage("load M1")
        listToList(self.DATABUS, self.M1)
        self.paintView()
        
    def loadM2(self):
        self.setMessage("load M2")
        listToList(self.DATABUS, self.M2)
        self.paintView()
        
    def loadX(self):
        self.setMessage("load X")
        listToList(self.DATABUS, self.X)
        self.paintView()
        
    def loadY(self):
        self.setMessage("load Y")
        listToList(self.DATABUS, self.Y)
        self.paintView()
        
    def loadJ1(self):
        self.setMessage("load J1")        
        listToList(self.DATABUS, self.J1)
        self.paintView()

    def loadJ2(self):
        self.setMessage("load J2")
        listToList(self.DATABUS, self.J2)
        self.paintView()
        
    def loadInst(self):
        self.setMessage("load Inst")
        listToList(self.DATABUS, self.Inst)
        self.paintView()
        
    def loadXY(self):
        self.setMessage("load XY")
        listToLists(self.X, self.Y, self.ADDRESSBUS)
        self.paintView()
        
    def loadPC(self):
        self.setMessage("load PC")
        listToLists(self.PC1, self.PC2, self.ADDRESSBUS)
        self.paintView()
        
    def loadINC(self):
        self.setMessage("load INC")
        listToList(self.IncUnit1, self.Inc1)
        listToList(self.IncUnit2, self.Inc2)
        self.paintView()
        
# ===== Select =================================================================
    
    def selectA(self):
        self.setMessage("select A")
        listToList(self.A, self.DATABUS)
        self.paintView()
        
    def selectB(self):
        self.setMessage("select B")
        listToList(self.B, self.DATABUS)
        self.paintView()
        
    def selectC(self):
        self.setMessage("select C")
        listToList(self.C, self.DATABUS)
        self.paintView()

    def selectD(self):
        self.setMessage("select D")
        listToList(self.D, self.DATABUS)
        self.paintView()

    def selectM1(self):
        self.setMessage("select M1")
        listToList(self.M1, self.DATABUS)
        self.paintView()
        
    def selectM2(self):
        self.setMessage("select M2")
        listToList(self.M2, self.DATABUS)
        self.paintView()
        
    def selectX(self):
        self.setMessage("select X")
        listToList(self.X, self.DATABUS)
        self.paintView()
        
    def selectY(self):
        self.setMessage("select Y")
        listToList(self.Y, self.DATABUS)
        self.paintView()
        
    def selectM(self):
        self.setMessage("select M")
        listsToList(self.M1, self.M2, self.ADDRESSBUS)
        self.updateIncrUnit()
        self.paintView()
        
    def selectXY(self):
        self.setMessage("select XY")
        listsToList(self.X, self.Y, self.ADDRESSBUS)
        self.updateIncrUnit()
        self.paintView()
                
    def selectJ(self):
        self.setMessage("select J")
        listsToList(self.J1, self.J2, self.ADDRESSBUS)
        self.updateIncrUnit()
        self.paintView()
                
    def selectPC(self):
        self.setMessage("select PC")
        listsToList(self.PC1, self.PC2, self.ADDRESSBUS)
        self.updateIncrUnit()
        self.paintView()
                
    def selectINC(self):
        self.setMessage("select INC")
        listsToList(self.Inc1, self.Inc2, self.ADDRESSBUS)
        self.updateIncrUnit()
        self.paintView()
        
# ===== ALU ====================================================================

    def setFUNCTION(self, f):
        self.oldFUNCTION = self.FUNCTION[:]
        listToList(f, self.FUNCTION)
        self.updateALU()

    def updateF0(self):
        listToList(self.FUNCTION, self.oldFUNCTION)
        self.FUNCTION[0] = (0 if self.FUNCTION[0] == 1 else 1)
        self.updateALU()
        self.paintView()

    def updateF1(self):
        listToList(self.FUNCTION, self.oldFUNCTION)
        self.FUNCTION[1] = (0 if self.FUNCTION[1] == 1 else 1)
        self.updateALU()
        self.paintView()

    def updateF2(self):
        listToList(self.FUNCTION, self.oldFUNCTION)
        self.FUNCTION[2] = (0 if self.FUNCTION[2] == 1 else 1)
        self.updateALU()
        self.paintView()

# ===== Mathematics ============================================================

    def getSum(self, k, b, c):
        return int(((not k) and (not b) and c) or \
                ((not k) and b and (not c)) or \
                (k and (not b) and (not c)) or \
                (k and b and c))

    def getCarry(self, k, b, c):
        return int(((not k) and b and c ) or \
                (k and (not b) and c) or \
                (k and b and (not c)) or \
                (k and b and c))

    def addBandC(self):
        self.ADDcarry = 0
        for i in Egnar8:
            b = self.B[i]
            c = self.C[i]
            self.ADD[i] = self.getSum(self.ADDcarry, b, c)
            self.ADDcarry = self.getCarry(self.ADDcarry, b, c)

    def incB(self):
        self.INCcarry = 1
        for i in Egnar8:
            b = self.B[i]
            self.INC[i] = self.getSum(self.INCcarry, b, 0)
            self.INCcarry = self.getCarry(self.INCcarry, b, 0)

    def shlB(self):
        x = self.B[:]
        x = x[1:] + [x[0]]
        listToList(x, self.SHL)

# ===== Update =================================================================

    def updateALU(self):
        self.updateFunctions()
        self.updateDatabus()
        self.updateStates()

    def updateFunctions(self):
        self.addBandC()
        self.incB()
        self.shlB()
        for i in Range8:
            b = self.B[i]
            c = self.C[i]
            self.AND[i] = int(b and c)
            self.OR[i] = int(b or c)
            self.NOT[i] = (0 if b == 1 else 1)
            self.XOR[i] = int(b ^ c)

    def updateDatabus(self):
        f = tuple(self.FUNCTION)
        F = self.functionLabelsDictionary[f]
        listToList(F, self.DATABUS)
        # Sets DATABUS relative to current function
        # as linked in functionLabelsDictionary.

    def updateStates(self):
        self.setCarryState()
        self.setZeroState()
        self.setSignState()

    def setCarryState(self):
        self.CARRY = int(self.ADDcarry == 1 or self.INCcarry == 1)

    def setZeroState(self):
        self.ZERO = int(self.DATABUS == [0,0,0,0,0,0,0,0])

    def setSignState(self):
        self.SIGN = int(self.DATABUS[0] == 1)
        
# ===== BUSES ==================================================================

    def setADDRESSBUSpart(self, i):
        self.ADDRESSBUS[i] = (1 if self.ADDRESSBUS[i] == 0 else 0)
        self.updateIncrUnit()
        self.paintView()

    def setDATABUSwhole(self, x):
        listToList(x, self.DATABUS)

    def setDATABUSpart(self, i):
        self.DATABUS[i] = (1 if self.DATABUS[i] == 0 else 0)
        self.paintView()

# ===== Increment Unit =========================================================

    def updateIncrUnit(self):
        Cy = 1
        x = [0]*16
        for i in Egnar16:
            A = self.ADDRESSBUS[i]
            x[i] = self.getSum(Cy, A, 0)
            Cy = self.getCarry(Cy, A, 0)
        listToList(x[0:8], self.IncUnit1)
        listToList(x[8:16], self.IncUnit2)

# ===== Memory =================================================================

    def increment(self, A):
        Cy = 1
        R = [0] * len(A)

        # Since this is little endian, a reversed list is needed for
        # the for loop.
        L = list( range( len(A) ) )
        L.reverse()
        
        for i in L:
            R[i] = self.getSum(Cy, A[i], 0)
            Cy = self.getCarry(Cy, A[i], 0)
        return R

    def mkMemory(self):
        A = [0]*15
        R = {}
        for unused_i in RangeMEM:
            R.update({tuple(A) : [0,0,0,0,0,0,0,0]})
            A = self.increment(A)
        return R

    def getMEMORY(self):
        return self.MEMORY[tuple(self.MEMORYADDRESS)]

    def addressbusToMemoryAddress(self):
        listToList(self.ADDRESSBUS[1:], self.MEMORYADDRESS)
        self.paintView()
        self.setMessage("Address bus to memory address: BusToMem")
  
    def readMemoryToDatabus(self):
        listToList(self.MEMORY[tuple(self.MEMORYADDRESS)], self.DATABUS)
        self.paintView()
        self.setMessage("Write memory to databus: WRITE MEM")
 
    def writeDatabusToMemory(self):
        listToList(self.DATABUS, self.MEMORY[tuple(self.MEMORYADDRESS)])
        self.paintView()
        self.setMessage("Write databus to memory: READ MEM")
 
    def CLEARMEM(self):
        self.setMessage("Clear Memory: start")
        A = [0]*15
        for unused_i in RangeMEM:
            listToList([0,0,0,0,0,0,0,0], self.MEMORY[tuple(A)])
            A = self.increment(A)
        self.paintView()
        self.setMessage("Clear Memory: end")

    def clearMemory(self):
        start_new_thread( self.CLEARMEM, () )

    def RANDMEM(self):
        self.setMessage("Random Memory: start")
        A = [0]*15
        for unused_i in RangeMEM:
            r = [ randint(0,1) for unused_i in range(8) ]
            listToList(r, self.MEMORY[tuple(A)])
            A = self.increment(A)
        self.paintView()
        self.setMessage("Random Memory: end")

    def randomMemory(self):
        start_new_thread( self.RANDMEM, () )

    def loadPGMtoMEM(self, filename):
        try:
            pgmFile = open(filename, 'r')
            for LINE in pgmFile:
                LINE = LINE.split()
                Address = [ int(i) for i in LINE[0]]
                Code = [ int(i) for i in LINE[1]]
                listToList(Code, self.MEMORY[tuple(Address[1:])])
            pgmFile.close()
            fn = filename.split('/')
            self.setMessage("Loaded " + fn[len(fn) - 1] + " to MEMORY")
            self.paintView()        
        except IOError:
            self.setMessage("File IO Error")

# ===== CALLBACKS ==============================================================

    def setPaintCallback(self, cb):
        self.paintView = cb

    def setMessageCallback(self, tcb):
        self.setMessage = tcb

# ===== Fetch, Increment & Execute =============================================

    def FETCH(self):
        self.setMessage("<<< FETCH >>>")
        self.selectPC()
        self.addressbusToMemoryAddress()
        self.readMemoryToDatabus()
        self.loadInst()
        
    def INCREMENT(self):        
        self.setMessage("<<< INCREMENT >>>")
        self.loadINC()
        self.selectINC()
        self.loadPC()

    def MOVfunction(self):
        self.setMessage("MOVE")
        if self.Inst[2:5] == self.Inst[5:8]:
            self.setDATABUSwhole([0,0,0,0,0,0,0,0])
            self.setMessage("D = S: set to [0,0,0,0,0,0,0,0]")
        else:
            self.setMessage("Moving stuff: ")
            self.regSelectMap[tuple(self.Inst[5:8])]()
        self.regLoadMap[tuple(self.Inst[2:5])]()

    def SETABfunction(self):
        self.setMessage("SETABfunction")
        p = [1,1,1] if self.Inst[3] == 1 else [0,0,0]
        # Since the negative numbers are represented by "two's
        # complement" the first three digits will be either 0s or
        # 1s depending on whether the number is positive, zero or
        # negative. This fixes that. 
        self.setDATABUSwhole(p + self.Inst[3:8])
        if self.Inst[2] == 0:
            self.loadA()
        else:
            self.loadB()
        self.setMessage(str(p + self.Inst[3:8]))

    def ALUfunction(self):
        self.setMessage("ALU function: " + str(self.Inst[5:8]))
        self.setFUNCTION(self.Inst[5:8])
        if self.Inst[4] == 0:
            self.loadA()
        else:
            self.loadD()

    def LOADfunction(self):
        self.setMessage("LOADfunction")
        self.selectM()
        self.addressbusToMemoryAddress()
        self.readMemoryToDatabus()
        if self.Inst[6:8] == [0,0]:
            self.loadA()
        else:
            if self.Inst[6:8] == [0,1]:
                self.loadB()
            else:
                if self.Inst[6:8] == [1,0]:
                    self.loadC()
                else:
                    self.loadD()

    def STOREfunction(self):
        self.setMessage("STOREfunction")
        self.selectM()
        if self.Inst[6:8] == [0,0]:
            self.selectA()
        else:
            if self.Inst[6:8] == [0,1]:
                self.selectB()
            else:
                if self.Inst[6:8] == [1,0]:
                    self.selectC()
                else:
                    self.selectD()
        self.addressbusToMemoryAddress()
        self.writeDatabusToMemory()

    def RET_MOV16function(self):
        self.setMessage("RETURN / MOVE 16 bits: " + str(self.Inst))
        RUN = True
        if self.Inst[5:7] == [1,1]:
            self.setMessage("HALT ")
            # Set PC to zero................................
            listToList([0,0,0,0,0,0,0,0], self.PC1)
            listToList([0,0,0,0,0,0,0,0], self.PC2)
            RUN = False 
        else:
            self.setMessage("MOV16")
            if self.Inst[4] == 0: # d is XY
                if self.Inst[5:7] == [0,0]:
                    self.selectM()
                    
                if self.Inst[5:7] == [0,1]: # What would Harry's machine do?
                    self.selectXY() 

                if self.Inst[5:7] == [1,0]:
                    self.selectJ()
                    
                self.loadXY()
            else: # d is PC
                if self.Inst[5:7] == [0,0]:
                    self.selectM()
                    
                if self.Inst[5:7] == [0,1]:
                    self.selectXY()
                    
                if self.Inst[5:7] == [1,0]:
                    self.selectJ()

                self.loadPC()
        return RUN

    def INCfunction(self):
        self.setMessage("INC: XY > XY + 1")
        self.selectXY()
        self.loadINC()
        self.selectINC()
        self.loadXY()

    def SETMfunction(self):
        self.setMessage("SETMfunction: Move next 16 bits to M")
        self.addressbusToMemoryAddress()
        self.readMemoryToDatabus()
        self.loadM1()
        self.loadINC()
        self.selectINC()
        self.addressbusToMemoryAddress()
        self.readMemoryToDatabus()
        self.loadM2()
        self.loadINC()
        self.selectINC()
        self.loadPC()

    def GOTOfunction(self):
        self.setMessage("GOTOfunction: set address bus, PC, to next 16 bits")
        self.addressbusToMemoryAddress()
        self.readMemoryToDatabus()
        self.loadJ1()
        self.loadINC()
        self.selectINC()
        self.addressbusToMemoryAddress()
        self.readMemoryToDatabus()
        self.loadJ2()
        self.selectJ()
        self.loadPC()

    def CALLfunction(self):
        self.setMessage("CALLfunction: set address bus to next 16 bits & PC => XY")
        # CALLfunction is like GOTOfunction except that the address of the next instruction 
        # after CALLfunction is saved in XY.
        self.addressbusToMemoryAddress()
        self.readMemoryToDatabus()
        self.loadJ1()
        self.loadINC()
        self.selectINC()
        self.addressbusToMemoryAddress()
        self.readMemoryToDatabus()
        self.loadJ2()
        self.loadINC()
        self.selectINC()
        self.loadXY()
        self.selectJ()
        self.loadPC()

    def BCfunction(self):
        self.setMessage("Branch Conditionally")
        C0 = (self.Inst[3] == 1) and (self.SIGN  == 1) 
        C1 = (self.Inst[4] == 1) and (self.CARRY == 0)
        C2 = (self.Inst[5] == 1) and (self.ZERO  == 1)
        C3 = (self.Inst[6] == 1) and (self.ZERO  == 0)

        c0 = " S1+ " if self.Inst[3] == 1 else " S1- "
        c1 = "Cy0+ " if self.Inst[4] == 1 else "Cy0- "
        c2 = " Z1+ " if self.Inst[5] == 1 else " Z1- "
        c3 = " Z0+ " if self.Inst[6] == 1 else " Z0- "

        a0 = "S=1" if self.SIGN  == 1 else  "S=0"
        a1 = "Cy=0" if self.CARRY  == 0 else "Cy=1"
        a2 = "Z=1" if self.ZERO  == 1 else  "Z=0"        
        a3 = "Z=0" if self.ZERO  == 0 else  "Z=1"        

        m0 = c0 + " " + a0 + "\n"
        m1 = c1 + " " + a1 + "\n"
        m2 = c2 + " " + a2 + "\n"
        m3 = c3 + " " + a3

        M = m0 + m1 + m2 + m3

        self.setMessage(M)

        if C0 or C1 or C2 or C3:
            self.setMessage("Branch")
            self.addressbusToMemoryAddress()
            self.readMemoryToDatabus()
            self.loadJ1()
            self.loadINC()
            self.selectINC()
            self.addressbusToMemoryAddress()
            self.readMemoryToDatabus()
            self.loadJ2()
            self.selectJ()
            self.loadPC()
        else:
            self.setMessage("No Branch")
            self.loadINC()
            self.selectINC()
            self.loadINC()
            self.selectINC()
            self.loadPC()

    def EXECUTE(self):
        self.setMessage("<<< EXECUTE >>>")
        RUN = True
        if self.Inst[0] == 0:
            if self.Inst[1] == 0:
                self.MOVfunction()
            else:
                self.SETABfunction()
        else:
            if self.Inst[1] == 0:
                if self.Inst[2] == 0:
                    if self.Inst[3] == 0:
                        self.ALUfunction()
                    else:
                        if self.Inst[4] == 0:
                            self.LOADfunction()
                        else:
                            self.STOREfunction()
                else:
                    if self.Inst[3] == 0:
                        RUN = self.RET_MOV16function()
                    else:
                        self.INCfunction()
            else:
                if self.Inst[2] == 0:
                    self.SETMfunction()
                else:
                    if self.Inst[5:7] == [1,1]:
                        if self.Inst[7] == 0:
                            self.GOTOfunction()
                        else:
                            self.CALLfunction()
                    else:
                        self.BCfunction()
        self.setMessage("*"*50)
        return RUN

# ===== RUN & CONTROLS =========================================================

    def step(self):
        self.PAUSE = False

    def pause(self):
        while self.PAUSE == True:
            pass
        self.PAUSE = True
        
    def noStep(self):
        self.NOSTEP = True if self.NOSTEP == False else False
        self.paintView()

    def FetchIncrementExecute(self):
        self.PAUSE = True
        self.RUN = True
        while self.RUN == True:
            self.FETCH()
            self.INCREMENT()
            self.RUN = self.EXECUTE()
            if self.RUN == True and self.NOSTEP == False:
                self.pause() # Make time to inspect the machine....

        self.setMessage("="*50)

    def run(self):
        start_new_thread( self.FetchIncrementExecute, () )
#         self.T = threading.Thread(target = self.FetchIncrementExecute )
#         TL = threading.Lock()
#         TL.acquire()
#         self.T.start()
#         TL.release()

# ===== Initialization =========================================================

    def __init__(self):

        self.DATABUS = [0,0,0,0,0,0,0,0]
        self.ADDRESSBUS    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.MEMORYADDRESS = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
        # Memory addresses are 15 bits, but the address
        # bus is 16 bits. So, the highest bit is dropped.

        self.MEMORY = self.mkMemory() 
        
        self.Inst = [0,0,0,0,0,0,0,0]
        self.PGM = []

        self.FUNCTION = [0,0,0]
        self.oldFUNCTION = [0,0,0]

        self.CARRY = 0
        self.ADDcarry = 0
        self.INCcarry = 0
        self.SIGN = 0
        self.ZERO = 0

        self.PAUSE = True
        self.NOSTEP = False
        self.RUN = True

        self.A = [0,0,0,0,0,0,0,0]
        self.B = [0,0,0,0,0,0,0,0]
        self.C = [0,0,0,0,0,0,0,0]        
        self.D = [0,0,0,0,0,0,0,0]    
        self.M1 = [0,0,0,0,0,0,0,0]
        self.M2 = [0,0,0,0,0,0,0,0]
        self.X = [0,0,0,0,0,0,0,0]
        self.Y = [0,0,0,0,0,0,0,0]
        self.J1 = [0,0,0,0,0,0,0,0]
        self.J2 = [0,0,0,0,0,0,0,0]

        # Program Counter
        self.PC1 = [0,0,0,0,0,0,0,0]
        self.PC2 = [0,0,0,0,0,0,0,0]

        # Increment Unit
        # This is always the address bus plus one.
        self.IncUnit1 = [0,0,0,0,0,0,0,0]
        self.IncUnit2 = [0,0,0,0,0,0,0,0]

        # IncUnit is loaded into Inc
        # Inc is selected onto the address bus
        self.Inc1 = [0,0,0,0,0,0,0,0]
        self.Inc2 = [0,0,0,0,0,0,0,0]

        self.ADD = [0,0,0,0,0,0,0,0]
        self.INC = [0,0,0,0,0,0,0,0]
        self.AND = [0,0,0,0,0,0,0,0]
        self.OR  = [0,0,0,0,0,0,0,0]
        self.XOR = [0,0,0,0,0,0,0,0]
        self.NOT = [0,0,0,0,0,0,0,0]
        self.SHL = [0,0,0,0,0,0,0,0]
        self.CLR = [0,0,0,0,0,0,0,0]

# ===== Dictionaries ===========================================================

        self.functionLabelsDictionary = { (0,0,0) : self.ADD, \
                                          (0,0,1) : self.INC, \
                                          (0,1,0) : self.AND, \
                                          (0,1,1) : self.OR, \
                                          (1,0,0) : self.XOR, \
                                          (1,0,1) : self.NOT, \
                                          (1,1,0) : self.SHL, \
                                          (1,1,1) : self.CLR \
                                          }

        self.regLoadMap = { (0,0,0) : self.loadA, \
                            (0,0,1) : self.loadB, \
                            (0,1,0) : self.loadC, \
                            (0,1,1) : self.loadD, \
                            (1,0,0) : self.loadM1, \
                            (1,0,1) : self.loadM2, \
                            (1,1,0) : self.loadX, \
                            (1,1,1) : self.loadY 
                            }

        self.regSelectMap = { (0,0,0) : self.selectA, \
                              (0,0,1) : self.selectB, \
                              (0,1,0) : self.selectC, \
                              (0,1,1) : self.selectD, \
                              (1,0,0) : self.selectM1, \
                              (1,0,1) : self.selectM2, \
                              (1,1,0) : self.selectX, \
                              (1,1,1) : self.selectY 
                              }

# ==============================================================================

        self.updateALU()
        self.updateIncrUnit()

# ===== END Initialization =====================================================




