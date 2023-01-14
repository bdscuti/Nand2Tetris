import argparse    
import os




command_types = {'add':'C_ARITHMETIC', 
                'sub':'C_ARITHMETIC',
                'neg':'C_ARITHMETIC', 
                'eq':'C_ARITHMETIC',
                'gt':'C_ARITHMETIC',
                'lt':'C_ARITHMETIC',
                'and':'C_ARITHMETIC',
                'or':'C_ARITHMETIC',
                'not':'C_ARITHMETIC',
                'push':'C_PUSH',
                'pop':'C_POP'
                #  don't know what to do here with the other types of commands.      
                }

segmentDictionary = {
        'local':'LCL',
        'argument':'ARG',
        'this':'THIS', 
        'that':'THAT',
        'temp':'5',
        'pointer':'3',
        'static': '16'}

DebugMode = True





def Parser(vm_file):
    if os.path.exists(vm_file):  # check if the asm_file exists at the specified path
        with open(vm_file, "r") as f:
            lines = f.readlines()  # calls translate_lines() function
            instructions = strip_whitespace_and_comments(lines)
            commands = instructions    
            current_command = commands[0]
            for _ in commands:
                if hasMoreCommands() == True:
                    current_command, commands = advance(commands)
                    words = current_command.split(' ')
                    type_of_current_command = command_types[words[0]]
                    if type_of_current_command != 'C_RETURN': 
                        arg1 = arg1(type_of_current_command, words)
                    if type_of_current_command in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
                        arg2 = arg2(words)
                    codeWriter(vm_file, type_of_current_command, arg1, arg2)
            else:
                print("File has no commands")
                
    def arg1(type_of_current_command, words):             
        if type_of_current_command == 'C_ARITHMETIC':
            return words[0]
        else:
            return words[1]
            
    def arg2(words):            
            return words[2]
                            
    def hasMoreCommands(commands):
        return bool(commands)
        
    def advance(commands):
        if hasMoreCommands() == True:
            current_command = commands[0]
            commands = commands[1:]
            return current_command, commands 
        else:
            return [], commands
        
    def strip_whitespace_and_comments(lines):
        instructions = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:
                if not stripped_line.startswith("//"):
                    if "//" in stripped_line:
                        instructions.append(stripped_line.split("//")[0].strip())
                    else:
                        instructions.append(stripped_line)
        return instructions           
    
 
 
 

def codeWriter(vm_file, type_of_current_command, arg1, arg2)
    init_SP()
    # if type_of_current_command == 'C_ARITHMETIC':
    #     writeArithmetic(arg1)

        
        

    def init_SP():
        write('@256\nD=A\n@SP\nM=D')
        
    # def writeArithmetic(arg1):
        # if arg1 == 'add':

        # elif arg1 == 'sub':
            
        # elif arg1 == 'neg':
            
        # elif arg1 == 'eq':
            
        # elif arg1 == 'gt':
            
        # elif arg1 == 'lt':
            
        # elif arg1 == 'and':
            
        # elif arg1 == 'or':
            
        # elif arg1 == 'not':



    def push(segment, index):
        write(f'//Push {segment} {index}\n')
        if segment == 'static': 
            static_label = vm_file.replace('.vm', index)  
            #hack machine automatically maps static labels to RAM registers
            write(f'@{static_label}.{index}\nD=M\n')
        
        else: 
            #store segment in D register
            # constant skips over rest of the code
            write(f'@{index}\n') 
            write(f'D=A\n')  
            
            if segment != 'constant':
                if segment == "pointer" or segment == "temp":
                    write(f'@{segmentDictionary[segment]}\n')
                    write(f'A=A+D\nD=M\n')
                # 
                else:
                    # ARG, LCL, THIS, THAT
                    write(f"@{segmentDictionary[segment]}\n")
                    write(f"A=M+D\nD=M\n")
                    
        #set stack value equal to D
        write(f'@SP\nA=M\nM=D\nD=SP+1\n@SP\nM=D\n') 
            
       

                    
    def pop(): 
        write('hello')
    
    
    
    
def write(code):
    if DebugMode = True:
        print(code)
    else:
        with open(args.vm_file.replace('.vm','.asm') ,'w'):
            print(code)
        
        
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Generates a hack binary file from assembly"
    )
    parser.add_argument("vm_file", help="name of a HACK assembly file, i.e input.asm")
    args = parser.parse_args()
    Parser(args.vm_file)