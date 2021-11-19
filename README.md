# Computer
Computer made using Digital (Made by Neeman)

## ALU
Arithmetic Logic Unit, does basic math and logic.  

**ID - Op Name**  
0 - Add  
1 - Subtract  
2 - Multiply  
3 - And  
4 - Or  
5 - Xor  
6 - Negate

## Computer Structure
ROM - Holds instructions to execute. 10 bit address  
RAM - RAM, random access memory. 10 bit address  
MAR - Memory Address Register, saves the address at which we want to access the ram. (Only takes in the first 10 bits of the data bus)  
Register A, B - Generic and General registers for program execution  
Program Counter - Saves the current address we are in the ROM  
Instruction Register - Holds the current instruction to execute.

## Control Logic

We use a ROM to appropriately get what microinstructions to execute.  

Address are 9 bits:  
000000 000   

First 3 bits are for the step that we are on.   
The last 6, are to represent what instruction this is.

The output on each address is a 18 bit value.
Each bit represents a microinstruction.
Example instruction:  
0b00000000000001110  
This is the fetch instruction, it fetches a new instruction from the ROM into the IR.

### Instruction Byte 
0000000000 **000000**

First 6 bits are reserved for instruction, allowing for 64 instructions  
10 bits are left over for other information

### Microinstructions
RAre - Register A read, if high, outputs data onto bus.  
RAwr - Register A write, if high, writes data from bus.  
RBre - Register B read, if high, outputs data onto bus.   
RBwr - Register B write, if high, writes data from bus.

ALUop - Operation for ALU to carry out.  
ALUo - Flag for overflow on the alu.   
ALUz - Flag for zero on the alu.   
ALUn - Flag for N on the alu.    
ALUre - ALU read, if high, outputs data onto bus.  

RAMwr - Write to RAM from the data bus  
RAMre - Read from RAM into the data bus  

MARwr - Write to ram from the data bus  
(The MAR always outputs its current data into the RAM, so a read microinstruction is not needed.)  

PCwr - Write to the Program Counter. Basically a jump instruction.
PCin - Increment current address in the program counter.

ROMre - Output data from address onto data bus

IRwr - Instruction Register write from data bus

SCclr - Step Counter clear signal

HLT - Halt the clock. Manual operation still possible.

### Instructions

#### No Op
000000  
NOP  
No operation, do nothing for 1 clock cycle.

#### Load A
000001   
LDA {memory address}
Loads a memory address from ram into the A register

#### Store/Stash A
000010
STA {memory address}
Store the value of the A register into the RAM in the specified address

#### Load Literal A
000011
LLA {value}
Loads a literal value (Max 10 bits) into the A Register

#### Load B
000100   
LDB {memory address}
Loads a memory address from ram into the B register

#### Store/Stash A
000101
STB {memory address}
Store the value of the B register into the RAM in the specified address

#### Load Literal A
000110
LLB {value}
Loads a literal value (Max 10 bits) into the B Register
