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
                    codewriter(vm_file, type_of_current_command,  arg1, arg2)
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