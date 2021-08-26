import RegistorValues as RV
import Data 

def StoreOp(linenum):
    R0 = converttobin(RV.RegsVal["000"])
    R1 = converttobin(RV.RegsVal["001"])
    R2 = converttobin(RV.RegsVal["010"])
    R3 = converttobin(RV.RegsVal["011"])
    R4 = converttobin(RV.RegsVal["100"])
    R5 = converttobin(RV.RegsVal["101"])
    R6 = converttobin(RV.RegsVal["110"])
    Flag = converttobin(RV.RegsVal["111"])
    bin_line = convertline(linenum)
    Data.D[linenum] = RV.RegsVal

    f = open("simout.txt", "a")
    f.write(bin_line + " " + R0 + " " + R1 + " " + R2 + " " + R3 +  " " + R4 + " " + R5 + " " + R6 +  " " + Flag)
    f.write('\n')
    f.close()

def StoreInDump(reg):
    f = open("maininput.txt", "a")
    reg_val = converttobin(RV.RegsVal[reg])
    a = reg_val[::-1]
    while len(a)<16:
        a+="0"
    reg_val = a[::-1]
    f.write(reg_val)
    f.write('\n')
    f.close()

def convertline(line):
    bin_num = bin(line).replace('0b','')
    a = bin_num[::-1]
    while len(a)<8:
        a+="0"
    bin_num = a[::-1]
    return bin_num

def converttobin(num):
    bin_num = bin(num).replace('0b','')
    a = bin_num[::-1]
    while len(a)<16:
        a+="0"
    bin_num = a[::-1]
    return bin_num

def printout():
    f = open("simout.txt", "r")
    Lines = f.readlines()
    for line in Lines:
        print(line.replace('\n',''))

def printMEMDump():
    f = open("maininput.txt", "r")
    Lines = f.readlines()
    for line in Lines:
        print(line.replace('\n',''))