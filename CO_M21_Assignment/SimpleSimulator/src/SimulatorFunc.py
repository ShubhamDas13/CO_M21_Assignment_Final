import RegistorValues as RV
import Storeandprint as SP

FlagList = []
for i in range(256):
    FlagList.append(0)

def Addition(inp,linenumber):
    a = inp[7:10]
    b_val = RV.RegsVal[inp[10:13]]
    c_val = RV.RegsVal[inp[13:16]]
    sum = b_val + c_val
    RV.RegsVal[a] = sum
    if sum>65535:
        RV.RegsVal["111"] += 8
        bin_val = bin(sum)
        finalbinval = bin_val[-17:-1]
        int_val = int(finalbinval,2)
        RV.RegsVal[a] = int_val
        FlagList[linenumber] = 1
    SP.StoreOp(linenumber-1)
    RV.RegsVal["111"] = 0

def Subtraction(inp,linenumber):
    a = inp[7:10]
    b_val = RV.RegsVal[inp[10:13]]
    c_val = RV.RegsVal[inp[13:16]]
    sub = b_val - c_val
    RV.RegsVal[a] = sub
    if sub<0:
        RV.RegsVal["111"] += 8
        RV.RegsVal[a] = 0
        FlagList[linenumber] = 8
    SP.StoreOp(linenumber-1)
    RV.RegsVal["111"] = 0

def Move_Immediate(inp,linenumber):
    a = inp[5:8]
    imm_val = int(inp[8:],2)
    RV.RegsVal[a] = imm_val
    SP.StoreOp(linenumber-1)


def Move_Register(inp,linenumber):
    a = inp[10:13]
    b = inp[13:]
    b_val = RV.RegsVal[inp[13:]]
    RV.RegsVal[a] = b_val
    if b == "111":
        val = FlagList[linenumber-1]
        RV.RegsVal[a] = val
    SP.StoreOp(linenumber-1)


def Load(inp,linenumber): 
    a = inp[10:13]
    mem_addr = int(inp[8:],2)
    lin = 0
    f = open("maininput.txt", "r")
    Lines = f.readlines()
    for line in Lines:
        line +=1
        if line == mem_addr:
            bin_val = line
            RV.RegsVal[a] = bin_val
            break
    SP.StoreOp(linenumber-1)
        

def Store(inp,linenumber):
    a = inp[5:8]
    SP.StoreInDump(a)
    SP.StoreOp(linenumber-1)


def Multiply(inp,linenumber):
    a = inp[7:10]
    b_val = RV.RegsVal[inp[10:13]]
    c_val = RV.RegsVal[inp[13:16]]
    mul = b_val * c_val
    RV.RegsVal[a] = mul
    if mul>65535:
        RV.RegsVal["111"] += 8
        bin_val = bin(mul)
        finalbinval = bin_val[-17:-1]
        int_val = int(finalbinval,2)
        RV.RegsVal[a] = int_val
        FlagList[linenumber] = 1
    SP.StoreOp(linenumber-1)
    RV.RegsVal["111"] = 0


def Divide(inp,linenumber):
    a = inp[7:10]
    b_val = RV.RegsVal[inp[10:13]]
    c_val = RV.RegsVal[inp[13:16]]
    div = b_val // c_val
    RV.RegsVal[a] = div
    SP.StoreOp(linenumber-1)


def Right_Shift(inp,linenumber):
    a = inp[5:8]
    a_val = RV.RegsVal[a]
    imm_val = int(inp[8:],2)
    rs = a_val>>imm_val
    RV.RegsVal[a] = rs
    SP.StoreOp(linenumber-1)


def Left_Shift(inp,linenumber):
    a = inp[5:8]
    a_val = RV.RegsVal[a]
    imm_val = int(inp[8:],2)
    ls = a_val<<imm_val
    RV.RegsVal[a] = ls
    SP.StoreOp(linenumber-1)



def Exclusive_OR(inp,linenumber):
    a = inp[7:10]
    b_val = RV.RegsVal[inp[10:13]]
    c_val = RV.RegsVal[inp[13:16]]
    xor = b_val^c_val
    RV.RegsVal[a] = xor
    SP.StoreOp(linenumber-1)


def OR(inp,linenumber):
    a = inp[7:10]
    b_val = RV.RegsVal[inp[10:13]]
    c_val = RV.RegsVal[inp[13:16]]
    orop = b_val|c_val
    RV.RegsVal[a] = orop
    SP.StoreOp(linenumber-1)


def AND(inp,linenumber):
    a = inp[7:10]
    b_val = RV.RegsVal[inp[10:13]]
    c_val = RV.RegsVal[inp[13:16]]
    andop = b_val&c_val
    RV.RegsVal[a] = andop
    SP.StoreOp(linenumber-1)


def Invert(inp,linenumber):
    a = inp[10:13]
    b = RV.RegsVal[inp[13:]]
    inv = ~b
    if inv<0:
        inv = 0
        RV.RegsVal[a] = inv
    else:
        RV.RegsVal[a] = inv
    SP.StoreOp(linenumber-1)


def Compare(inp,linenumber):
    a = RV.RegsVal[inp[10:13]]
    b = RV.RegsVal[inp[13:]]
    if a==b:
        RV.RegsVal["111"] += 1
        FlagList[linenumber] = 1
    elif a>b:
        RV.RegsVal["111"] += 2
        FlagList[linenumber] = 2
    elif a<b:
        RV.RegsVal["111"] += 4
        FlagList[linenumber] = 4
    SP.StoreOp(linenumber-1)
    RV.RegsVal["111"] = 0

def Unconditional_Jump(inp,linenumber):
    mem_addr = inp[8:]
    SP.StoreOp(linenumber-1)
    val = int(mem_addr,2)
    return val



def Jump_if_less_than(inp,linenumber):
    mem_addr = inp[8:]
    SP.StoreOp(linenumber-1)
    if FlagList[linenumber-1] == 4:
        val = int(mem_addr,2)
        return val
    else:
        return linenumber


def Jump_if_greater_than(inp,linenumber):
    mem_addr = inp[8:]
    SP.StoreOp(linenumber-1)
    if FlagList[linenumber-1] == 2:
        val = int(mem_addr,2)
        return val
    else:
        return linenumber

def Jump_if_equal(inp,linenumber):
    mem_addr = inp[8:]
    SP.StoreOp(linenumber-1)
    if FlagList[linenumber-1] == 1:
        val = int(mem_addr,2)
        return val
    else:
        return linenumber

