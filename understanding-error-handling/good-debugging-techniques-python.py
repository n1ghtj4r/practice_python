import pdb
import sys #im using this to full stop the functions, and proper manage it

def add(a, b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}')
    return result

add(1, 2)

#best way to get Quotient, with function;

def divide(a, b):
    result = a / b
    return result

print(divide(10, 2))
print(divide(15, 3))

print("\n") #pdb section, pdb section is an interactive debugging environment

def divide(a, b):
    sys.exit() #remove this to run the command section, follow in comment down below
    pdb.set_trace()
    return a / b

print(divide(10, 2))

# output type examples

"""
type:
> /Users/fcc/Desktop/debugging.py(5)divide()
-> return a / b
(Pdb)

the output:

(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) whatis a
<class 'int'>
(Pdb) whatis divide
Function divide

(Pdb) continue
5.0
"""