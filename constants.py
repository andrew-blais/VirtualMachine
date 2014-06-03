#!/usr/bin/python3.2


# Copyright 2014 by Andrew L. Blais.
# This program is distributed under the terms of the 
# GNU General Public License version 3.


# This file contains a number of constants that are use in the three modules 
# that make up Virtual Machine. 


Range3 = range(3)
Range8 = range(8)
Egnar8 = range(7,-1,-1) # Egnar8 is Range8 backwards.

Range16 = range(16)
Egnar16 = range(15,-1,-1)

def listToList(source, destination):
    for j in range(len(source)):
        destination[j] = source[j]

def setSV(sv, v):
    for j in range(len(sv)):
        sv[j].set(str(v[j]))
# This supposes that the elements of sv have a set method. No bugs, yet. 
# Checks?

def listsToList(L1, L2, LIST):
    for j in Range16:
        if j < 8:
            LIST[j] = L1[j]
        else:
            LIST[j] = L2[j-8]
# This should make some checks. 
# len(L1) == len(L2) ?
# len(L1) + len(L2) == len(LIST)

def listToLists(L1, L2, LIST):
    for j in Range16:
        if j < 8:
            L1[j] = LIST[j]
        else:
            L2[j-8] = LIST[j]

MEMORYsize = pow(2,15)
RangeMEM = range(MEMORYsize)

