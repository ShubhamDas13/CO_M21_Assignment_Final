import Registers

def giveOutput(isa_opcode, freebits, regs):
    final_binary = isa_opcode + "0"*freebits + regs
    a = open("mainoutput.txt", "a")
    a.write(final_binary)
    a.write('\n')
    a.close()
    print(final_binary)


def Addition(r1,r2,r3):
    bin_r1 = Registers.Regs[r1]
    bin_r2 = Registers.Regs[r2]
    bin_r3 = Registers.Regs[r3]
    return (bin_r1 + bin_r2 + bin_r3)


def Subtraction(r1,r2,r3):
    bin_r1 = Registers.Regs[r1]
    bin_r2 = Registers.Regs[r2]
    bin_r3 = Registers.Regs[r3]
    return (bin_r1 + bin_r2 + bin_r3)


def Move_Immediate(r1,imm):
    bin_r1 = Registers.Regs[r1]
    immd_val = imm[1:]
    num = int(immd_val)
    bin_num = bin(num).replace('0b','')
    a = bin_num[::-1]
    while len(a)<8:
        a+="0"
    bin_num = a[::-1]
    return (bin_r1 + bin_num)


def Move_Register(r1,r2):
    bin_r1 = Registers.Regs[r1]
    bin_r2 = Registers.Regs[r2]
    return (bin_r1 + bin_r2)


def Load(r1,mem_addr):  #mem_addr = line number
    bin_r1 = Registers.Regs[r1]
    mem = int(mem_addr)
    bin_memaddr = bin(mem).replace('0b','')
    a = bin_memaddr[::-1]
    while len(a)<8:
        a+="0"
    bin_memaddr = a[::-1]
    return (bin_r1 + bin_memaddr)


def Store(r1,mem_addr):
    bin_r1 = Registers.Regs[r1]
    mem = int(mem_addr)
    bin_memaddr = bin(mem).replace('0b','')
    a = bin_memaddr[::-1]
    while len(a)<8:
        a+="0"
    bin_memaddr = a[::-1]
    return (bin_r1 + bin_memaddr)


def Multiply(r1,r2,r3):
    bin_r1 = Registers.Regs[r1]
    bin_r2 = Registers.Regs[r2]
    bin_r3 = Registers.Regs[r3]
    return (bin_r1 + bin_r2 + bin_r3)


def Divide(r3,r4):
    bin_r3 = Registers.Regs[r3]
    bin_r4 = Registers.Regs[r4]
    return (bin_r3 + bin_r4)


def Right_Shift(r1,imm):
    bin_r1 = Registers.Regs[r1]
    num = int(imm)
    bin_num = bin(num).replace('0b','')
    a = bin_num[::-1]
    while len(a)<8:
        a+="0"
    bin_num = a[::-1]
    return (bin_r1 + bin_num)


def Left_Shift(r1,imm):
    bin_r1 = Registers.Regs[r1]
    num = int(imm)
    bin_num = bin(num).replace('0b','')
    a = bin_num[::-1]
    while len(a)<8:
        a+="0"
    bin_num = a[::-1]
    return (bin_r1 + bin_num)


def Exclusive_OR(r1,r2,r3):
    bin_r1 = Registers.Regs[r1]
    bin_r2 = Registers.Regs[r2]
    bin_r3 = Registers.Regs[r3]
    return (bin_r1 + bin_r2 + bin_r3)


def OR(r1,r2,r3):
    bin_r1 = Registers.Regs[r1]
    bin_r2 = Registers.Regs[r2]
    bin_r3 = Registers.Regs[r3]
    return (bin_r1 + bin_r2 + bin_r3)


def AND(r1,r2,r3):
    bin_r1 = Registers.Regs[r1]
    bin_r2 = Registers.Regs[r2]
    bin_r3 = Registers.Regs[r3]
    return (bin_r1 + bin_r2 + bin_r3)


def Invert(r1,r2):
    bin_r1 = Registers.Regs[r1]
    bin_r2 = Registers.Regs[r2]
    return (bin_r1 + bin_r2)


def Compare(r1,r2):
    bin_r1 = Registers.Regs[r1]
    bin_r2 = Registers.Regs[r2]
    return (bin_r1 + bin_r2)


def Unconditional_Jump(mem_addr):
    mem = int(mem_addr)
    bin_memaddr = bin(mem).replace('0b','')
    a = bin_memaddr[::-1]
    while len(a)<8:
        a+="0"
    bin_memaddr = a[::-1]
    return (bin_memaddr)


def Jump_if_less_than(mem_addr):
    mem = int(mem_addr)
    bin_memaddr = bin(mem).replace('0b','')
    a = bin_memaddr[::-1]
    while len(a)<8:
        a+="0"
    bin_memaddr = a[::-1]
    return (bin_memaddr)


def Jump_if_greater_than(mem_addr):
    mem = int(mem_addr)
    bin_memaddr = bin(mem).replace('0b','')
    a = bin_memaddr[::-1]
    while len(a)<8:
        a+="0"
    bin_memaddr = a[::-1]
    return (bin_memaddr)


def Jump_if_equal(mem_addr):
    mem = int(mem_addr)
    bin_memaddr = bin(mem).replace('0b','')
    a = bin_memaddr[::-1]
    while len(a)<8:
        a+="0"
    bin_memaddr = a[::-1]
    return (bin_memaddr)


def Halt():
    return "00000000000"

