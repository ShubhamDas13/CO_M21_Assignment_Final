import RegistorValues as RV
import Storeandprint as SP
import SimulatorFunc as SF

open("maininput.txt", "w").close()
open("simout.txt", "w").close()

linenumber = 0
while True:
    try:
        f = open("maininput.txt", "a")
        inp = input()
        linenumber += 1
        finalinp = inp + "\n"
        f.write(finalinp)
        if inp == "1001100000000000":
            break

    except EOFError:
        break;

f.close()

f = open("maininput.txt", "r")
linenum = 0
checkline = 0
Lines = f.readlines()
for line in Lines:
    inp = line.replace('\n','')
    isa = inp[:5]
    if checkline == linenum:
        linenum += 1
        checkline += 1
        if isa == "00000": #add
            SF.Addition(inp,linenum)

        elif isa == "00001": #sub
            SF.Subtraction(inp,linenum)

        elif isa == "00010": #mov imm:
            SF.Move_Immediate(inp,linenum)

        elif isa == "00011": #mov reg
            SF.Move_Register(inp,linenum)

        elif isa == "00100": #ld
            SF.Load(inp,linenum)
        
        elif isa == "00101": #st
            SF.Store(inp,linenum)
            linenumber += 1

        elif isa == "00110": #mul
            SF.Multiply(inp,linenum)

        elif isa == "00111": #div
            SF.Divide(inp,linenum)

        elif isa == "01000": #rs
            SF.Right_Shift(inp,linenum)

        elif isa == "01001": #ls
            SF.Left_Shift(inp,linenum)

        elif isa == "01010": #xor
            SF.Exclusive_OR(inp,linenum)

        elif isa == "01011": #or
            SF.OR(inp,linenum)
    
        elif isa == "01100": #and
            SF.AND(inp,linenum)

        elif isa == "01101": #not
            SF.Invert(inp,linenum)

        elif isa == "01110": #cmp
            SF.Compare(inp,linenum)

        elif isa == "01111": #jmp
            linenum = SF.Unconditional_Jump(inp,linenum)

        elif isa == "10000": #jlt
            linenum = SF.Jump_if_less_than(inp,linenum)

        elif isa == "10001": #jgt
            linenum = SF.Jump_if_greater_than(inp,linenum)

        elif isa == "10010": #je
            linenum = SF.Jump_if_equal(inp,linenum)

        elif inp == "1001100000000000": #hlt
            SP.StoreOp(linenum-1)
            break
    elif checkline < linenum:
        checkline += 1

for i in range(linenumber,257):
    f = open("maininput.txt", "a")
    finalinp = "0000000000000000" + "\n"
    f.write(finalinp)

SP.printout()  
SP.printMEMDump()