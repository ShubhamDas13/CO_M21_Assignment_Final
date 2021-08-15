#OPCODES for the Assembler
MRI = 1
NonMRI = 0

# {"command":("Binary Opcode value", MRI or not, Number of operands)}
Opcode = {"add":"00000",
"sub":"00001",
"mov":{"imm":"00010","reg":"00011"},
"ld":"00100",
"st":"00101",
"mul":"00110",
"div":"00111",
"rs":"01000",
"ls":"01001",
"xor":"01010",
"or":"01011",
"and":"01100",
"not":"01101",
"cmp":"01110",
"jmp":"01111",
"jlt":"10000",
"jgt":"10001",
"je":"10010",
"hlt":"10011"
}