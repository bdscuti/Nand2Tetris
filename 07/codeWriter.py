from Parser import *


def codewriter(vm_file, type_of_current_command, arg1, arg2):
    with open(vm_file.replace('.vm','asm') ,'w'):
        if type_of_current_command == 'C_ARITHMETIC':
            writeArithmetic(arg1)


def writeArithmetic(arg1):
    if arg1 == 'add':
        print('')
    # elif arg1 == 'sub':
        
    # elif arg1 == 'neg':
        
    # elif arg1 == 'eq':
        
    # elif arg1 == 'gt':
        
    # elif arg1 == 'lt':
        
    # elif arg1 == 'and':
        
    # elif arg1 == 'or':
        
    # elif arg1 == 'not':



class Stack:
    RAM = {'SP':256, 
        'LCL':None,
        'ARG':None,
        'STATIC':16, 
        'THIS':None, 
        'THAT':None}
    vm_file = args.vm_file
    
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        
    def push(self):
        if self.arg1 == 'constant':
            # pointer = Stack.RAM["SP"] 
            # Stack.RAM[pointer] = self.arg2
            print(f'@{self.arg2}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            # pointer+=1
            
        elif self.arg1 == 'static':
            # pointer = Stack.RAM["SP"]  
            static_label = Stack.vm_file.replace('.vm', self.arg2)  
            # Stack.RAM[pointer]=Stack.RAM[Stack.RAM['STATIC']]
            # Stack.RAM['STATIC'] += 1 
            # pointer += 1
            print(f'@{static_label}.{self.arg2}\nD=M\n@{self.arg2}\nD=D+M\n@{static_label}.{self.arg2}\nM=D\n')
            print(f'@{static_label}.{self.arg2}\nD=M\n@SP\nM=D\n@SP\nM=M+1\n')
        
            
        elif self.arg1 == 'local':
            # pointer = Stack.RAM["SP"]
            # LCL_i = Stack.RAM["LCL"] + self.arg2
            print(f'@LCL\nD=M\n@{self.arg2}\nD=D+M\n@LCL\nM=D\n')
            # Stack.RAM[pointer] = Stack.RAM[LCL_i]
            # pointer += 1
            print(f'@LCL\nD=M\n@SP\nM=D\n@SP\nM=M+1\n')
            
        elif self.arg1 == 'argument':
            # pointer = Stack.RAM["SP"]
            # ARG_i = Stack.RAM[""] + self.arg2
            print(f'@ARG\nD=M\n@{self.arg2}\nD=D+M\n@LCL\nM=D\n')
            # Stack.RAM[pointer] = Stack.RAM[ARG_i]
            # pointer += 1
            print(f'@ARG\nD=M\n@SP\nM=D\n@SP\nM=M+1\n') 
        elif  self.arg1 == 'this':
            
        elif  self.arg1 == 'that':

                     
    def pop(): 
         print('hello')