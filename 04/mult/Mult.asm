// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

    @0
    D = A
    @R2
    M = D //set sum to 0
    @CONDITIONAL
    0;JMP
(LOOP)   
    @R2
    D = M 
    @R0 
    D = D+M //Add R0 to sum
    @R2
    M = D   //Set R2 to the new value

(CONDITIONAL)
    @R1
    D = M
    @END
    D = D-1;JLT //R1-1 and check equality
    @R1
    M = D
    @LOOP
    0;JMP

(END)
    @END
    0;JMP



