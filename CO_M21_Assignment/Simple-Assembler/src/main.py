#This is where the program starts running
import OPCodes
import Registers
import ErrorToPrint
import AssemblerFunc as AF

erDict = {} #{line_number:[errors]}
line = 0
codeline = 0
VarDict = {} #{Variable_name:memory_address or total line -1}
LabelDict = {} #{label_name: (memory_address line-1, data)}
hltlist = [] #stores the codeline of hlt

def checkLabel(instruc):
    l = len(instruc[0])
    if instruc[0][l-1] == ':' and 'label' in instruc[0]:
        return True
    else:
        return False

def checkRegs(reg):
    if reg in Registers.Regs:
        return True
    else:
        return False

def checkErrors(instruc, previnst):
    
    if previnst[0] == "hlt":
        if instruc != []:
            return "-9"
    if len(hltlist) > 1:
        return "-9"
    if len(hltlist) == 0:
        return "-8"


    if instruc[0] == "var":
        if codeline > temptotalvar:
            return "-7"
        if len(instruc) != 2:
            return "-10"
        if instruc[1].isnumeric():
            return "-10"
        if instruc[1] == "FLAGS":
            return "-4"
        else:
            return None

    if instruc[0] not in OPCodes.Opcode:
        return "-1"
    
    if instruc[0] == "add":
        if len(instruc) != 4:
            return "-10"
        for i in range(1,4):
            reg = instruc[i]
            if reg == "FLAGS":
                return "-4"
            if checkRegs(reg) == False:
                return "-10"
        
        
    if instruc[0] == "sub":
        if len(instruc) != 4:
            return "-10"
        for i in range(1,4):
            reg = instruc[i]
            if reg == "FLAGS":
                return "-4"
            if checkRegs(reg) == False:
                return "-10"


    if instruc[0] == "mov":
        if len(instruc) != 3:
            return "-10"
        for i in range(1,3):
            r = instruc[i]
            if r[0].isalnum() == False:
                if int(r[1:])<0 or int(r[1:])>255:
                    return "-5"
                else:
                    return None
            if i ==1 and checkRegs(r) == False:
                return "-10"
            if r.isalnum and checkRegs(r) == False:
                return "-10"
    

    if instruc[0] == "ld":
        if len(instruc) != 3:
            return "-10"
        if checkRegs(instruc[1])==False:
            return "-10"
        mem = instruc[2]
        if mem not in VarDict:
            if mem in LabelDict:
                return "-6"
            return "-10"

    if instruc[0] == "st":
        if len(instruc) != 3:
            return "-10"
        if checkRegs(instruc[1])==False:
            return "-10"
        mem = instruc[2]
        if mem not in VarDict:
            if mem in LabelDict:
                return "-6"
            return "-10"
    
    if instruc[0] == "mul":
        if len(instruc) != 4:
            return "-10"
        for i in range(1,4):
            reg = instruc[i]
            if reg == "FLAGS":
                return "-4"
            if checkRegs(reg) == False:
                return "-10"
    
    if instruc[0] == "div":
        if len(instruc)!=3:
            return "-10"
        for i in range(1,3):
            r = instruc[i]
            if checkRegs(r) == False:
                return "-10"
    
    if instruc[0] == "rs":
        if len(instruc) != 3:
            return "-10"
        if checkRegs(instruc[1]):
            return "-10"
        r = instruc[2]
        if r.isnumeric() or r.isalpha():
            return "-10"
        if r[0].isalnum() == False:
            if int(r[1:])<0 or int(r[1:])>255:
                return "-5"
    
    if instruc[0] == "ls":
        if len(instruc) != 3:
            return "-10"
        if instruc[1] not in Registers.Regs:
            return "-10"
        r = instruc[2]
        if r.isnumeric() or r.isalpha():
            return "-10"
        if r[0].isalnum() == False:
            if int(r[1:])<0 or int(r[1:])>255:
                return "-5"
    
    if instruc[0] == "xor":
        if len(instruc) != 4:
            return "-10"
        for i in range(1,4):
            reg = instruc[i]
            if reg == "FLAGS":
                return "-4"
            if checkRegs(reg) == False:
                return "-10"
    
    if instruc[0] == "or":
        if len(instruc) != 4:
            return "-10"
        for i in range(1,4):
            reg = instruc[i]
            if reg == "FLAGS":
                return "-4"
            if checkRegs(reg) == False:
                return "-10"
    
    if instruc[0] == "and":
        if len(instruc) != 4:
            return "-10"
        for i in range(1,4):
            reg = instruc[i]
            if reg == "FLAGS":
                return "-4"
            if checkRegs(reg) == False:
                return "-10"

    if instruc[0] == "not":
        if len(instruc)!=3:
            return "-10"
        for i in range(1,3):
            r = instruc[i]
            if checkRegs(r) == False:
                return "-10"
    
    if instruc[0] == "cmp":
        if len(instruc)!=3:
            return "-10"
        for i in range(1,3):
            r = instruc[i]
            if checkRegs(r) == False:
                return "-10"

    if instruc[0] == "jmp":
        if len(instruc)!=2:
            return "-10"
        if (instruc[1] + ":") not in LabelDict:
            if instruc[1] in VarDict:
                return "-6"
            return "-3"

    if instruc[0] == "jlt":
        if len(instruc)!=2:
            return "-10"
        if (instruc[1] + ":") not in LabelDict:
            if instruc[1] in VarDict:
                return "-6"
            return "-3"

    if instruc[0] == "jgt":
        if len(instruc)!=2:
            return "-10"
        if (instruc[1] + ":") not in LabelDict:
            if instruc[1] in VarDict:
                return "-6"
            return "-3"
    
    if instruc[0] == "je":
        if len(instruc)!=2:
            return "-10"
        if (instruc[1] + ":") not in LabelDict:
            if instruc[1] in VarDict:
                return "-6"
            return "-3"

        









def StartAssemblingData(instruction):
    isa = instruction[0]
    
    if isa == "add":
        bin_is = OPCodes.Opcode[isa]
        reg_bin = AF.Addition(instruction[1], instruction[2], instruction[3])
        num_freebit = 2
        AF.giveOutput(bin_is,num_freebit,reg_bin)   #print 


    elif isa == "sub":
        bin_is = OPCodes.Opcode[isa]
        reg_bin = AF.Subtraction(instruction[1], instruction[2], instruction[3])
        num_freebit = 2
        AF.giveOutput(bin_is,num_freebit,reg_bin)


    elif isa == "mov":
        bin_is = OPCodes.Opcode[isa]
        val = instruction[2]
        if val in Registers.Regs:
            bin_is = OPCodes.Opcode[isa]["reg"]
            binary = AF.Move_Register(instruction[1], val)
            num_freebit = 5
        else:
            bin_is = OPCodes.Opcode[isa]["imm"]
            binary = AF.Move_Immediate(instruction[1], val)
            num_freebit = 0
        AF.giveOutput(bin_is,num_freebit,binary)


    elif isa == "ld":
        bin_is = OPCodes.Opcode[isa]
        mem_ad = VarDict[instruction[2]]
        binary = AF.Load(instruction[1], mem_ad)
        num_freebit = 0
        AF.giveOutput(bin_is,num_freebit,binary)


    elif isa == "st":
        bin_is = OPCodes.Opcode[isa]
        mem_addr = VarDict[instruction[2]]
        binary = AF.Store(instruction[1], mem_addr)
        num_freebit = 0
        AF.giveOutput(bin_is,num_freebit,binary)


    elif isa == "mul":
        bin_is = OPCodes.Opcode[isa]
        reg_bin = AF.Multiply(instruction[1], instruction[2], instruction[3])
        num_freebit = 2
        AF.giveOutput(bin_is,num_freebit,reg_bin)


    elif isa == "div":
        bin_is = OPCodes.Opcode[isa]
        reg_bin = AF.Divide(instruction[1], instruction[2])
        num_freebit = 5
        AF.giveOutput(bin_is,num_freebit,reg_bin)


    elif isa == "rs":
        bin_is = OPCodes.Opcode[isa]
        val = instruction[2][1:]
        binary = AF.Right_Shift(instruction[1], val)
        num_freebit = 0
        AF.giveOutput(bin_is,num_freebit,binary)


    elif isa == "ls":
        bin_is = OPCodes.Opcode[isa]
        val = instruction[2][1:]
        binary = AF.Left_Shift(instruction[1], val)
        num_freebit = 0
        AF.giveOutput(bin_is,num_freebit,binary)


    elif isa == "xor":
        bin_is = OPCodes.Opcode[isa]
        reg_bin = AF.Exclusive_OR(instruction[1], instruction[2], instruction[3])
        num_freebit = 2
        AF.giveOutput(bin_is,num_freebit,reg_bin)


    elif isa == "or":
        bin_is = OPCodes.Opcode[isa]
        reg_bin = AF.OR(instruction[1], instruction[2], instruction[3])
        num_freebit = 2
        AF.giveOutput(bin_is,num_freebit,reg_bin)
    

    elif isa == "and":
        bin_is = OPCodes.Opcode[isa]
        reg_bin = AF.AND(instruction[1], instruction[2], instruction[3])
        num_freebit = 2
        AF.giveOutput(bin_is,num_freebit,reg_bin)


    elif isa == "not":
        bin_is = OPCodes.Opcode[isa]
        reg_bin = AF.Invert(instruction[1], instruction[2])
        num_freebit = 5
        AF.giveOutput(bin_is,num_freebit,reg_bin)


    elif isa == "cmp":
        bin_is = OPCodes.Opcode[isa]
        reg_bin = AF.Compare(instruction[1], instruction[2])
        num_freebit = 5
        AF.giveOutput(bin_is,num_freebit,reg_bin)


    elif isa == "jmp":
        bin_is = OPCodes.Opcode[isa]
        val = LabelDict[instruction[1] + ":"]
        binary = AF.Unconditional_Jump(val)
        num_freebit = 3
        AF.giveOutput(bin_is,num_freebit,binary)


    elif isa == "jlt":
        bin_is = OPCodes.Opcode[isa]
        val = LabelDict[instruction[1] + ":"]
        binary = AF.Jump_if_less_than(val)
        num_freebit = 3
        AF.giveOutput(bin_is,num_freebit,binary)


    elif isa == "jgt":
        bin_is = OPCodes.Opcode[isa]
        val = LabelDict[instruction[1] + ":"]
        binary = AF.Jump_if_greater_than(val)
        num_freebit = 3
        AF.giveOutput(bin_is,num_freebit,binary)


    elif isa == "je":
        bin_is = OPCodes.Opcode[isa]
        val = LabelDict[instruction[1] + ":"]
        binary = AF.Jump_if_equal(val)
        num_freebit = 3
        AF.giveOutput(bin_is,num_freebit,binary)


    elif isa == "hlt":
        bin_is = OPCodes.Opcode[isa]
        binary = AF.Halt()
        num_freebit = 0
        AF.giveOutput(bin_is,num_freebit,binary)

totalline = 0
totalvarline = 0
open("mainoutput.txt", 'w').close()
open("userinput.txt", 'w').close()
previnst = ["first"]


#reads all the input
while True:
    f = open("userinput.txt", 'a')
    try:
        inp = input()
        x = inp.split()
        totalline += 1
        if inp == '':
            break

        if x[0] == 'var':
            totalvarline+=1
        
        if "hlt" in x:
            hltlist.append(totalline)
        
        c = checkLabel(x)
        if c == True:
            label_name = x[0]
            newdata = []
            for data in range(1,len(x)):
                newdata.append(x[data])
            x = newdata
            mem_val = totalline - totalvarline
            value = str(mem_val-1)
            LabelDict[label_name] = value
            newl = len(x)
            s=""
            for y in range(0,newl):
                if y == newl-1:
                    s += x[y]
                else:
                    s = s + x[y]+" "
            inp = s

        inpnext = inp + "\n"
        f.write(inpnext)
    except EOFError:
        break;


#starts assembly
f = open("userinput.txt", 'r')
lines = f.readlines()
temptotalvar = totalvarline
prev = ['empty']
for i in lines:
    if codeline>=1:
        prev = ins
    ins = i.replace('\n', '').split()
    codeline += 1
    line +=1
    er = checkErrors(ins,prev)
        
    if er != None:                                            #checks Errors
        if er == "-8":
            print("[ERROR] "+ ErrorToPrint.Errors[er])
            break
        print("[ERROR] on line "+ str(codeline) + " " + ErrorToPrint.Errors[er])
        break

    if ins[0] != "var":                                       #starts assembly
        StartAssemblingData(ins)

    elif ins[0] == "var":                                     #stores var in varDict
        VarDict[ins[1]] = totalline - totalvarline
        totalvarline -=1
        line -= 1
