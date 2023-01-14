// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(LOOP)
    @SCREEN
	D=A
	@i 
	M=D //i = screen

    @KBD
    D = M
    @BLACK_SCREEN
    D;JNE

    (WHITE_SCREEN)
		@i
		A=M
		M=0    //set white screen 
		@i     
		M=M+1
		@i
		D=M //increment i

    //  if i < 24575:
        @24576
        D = A
        @i
        D = D-M
        @WHITE_SCREEN
        D;JNE //iterate again
        @LOOP
        0;JMP

    (BLACK_SCREEN)    
		@i
		A=M
		M=-1 // set black screen
		@i     
		M=M+1
		@i
		D=M //increment i

    //  if i < 24575:
        @24576
        D = A
        @i
        D = D-M
        @BLACK_SCREEN
        D;JNE //iterate again
        @LOOP
        0;JMP
