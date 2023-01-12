import argparse    
import os
from Parser import *
from codeWriter import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Generates a hack binary file from assembly"
    )
    parser.add_argument("vm_file", help="name of a HACK assembly file, i.e input.asm")
    args = parser.parse_args()
    Parser(args.vm_file)
                                    






        

         
         

    
    
    
    
    
    
