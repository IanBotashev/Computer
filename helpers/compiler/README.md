# Compiler
The compiler is a helper tool to make it easier to code for this CPU.

The only thing you need to know is when referencing a line in the file itself, for example when jumping,
prefix the program address with &, this automatically adjusts later on to be the correct position in the program.

Certain commands like SLI take up 2 addresses, and & accounts for that.   
Of course though, you don't need to.

All commands can be found in the main readme at the bottom.  
Run main.py.