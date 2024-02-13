'''
CS-370 lab activity for Jan. 30, 2024
This file includes a sample example of how you can use sys.argv to parse command line arguments.
sys.argv is a list containing all the items that have been typed on the command line for a particular invocation of a program.

For example, you might type into the command line, to execute your python program:
>> python myprogram.py --dostuff arguments

sys.argv[0] is the name used to invoke the program (myprogram.py).
Optionally, additional arguments may come after the name of the program, those are sys.argv[1], etc.
'''

import sys
import os
import simpleaudio as sa
from simpleaudio_test import play_sound
argvlen = len(sys.argv)

'''
This is a debugging statement that prints out the list of command line arguments that were included when you 
invoked this program from the command line.
'''
print("sys.argv: ", sys.argv)

'''
# HELP: This is a command line argument that is invoked by typing --help or -h
(Note that it is a command line convention to offer full name and first letter options.
The full name options have two preceding dashes -- and the one-letter options have just one -)
For example:
>> python cli_example.py --help
>> python cli_example.py --h

Right now, this help command is not very useful.
Take a look at some other helps commands, like
>> python --help
>> pip -h
>> conda --help
To see what they include.
'''

# This if statement checks to see what argument comes right after the program name
# Note that it also runs if you have no arguments after the program name
if argvlen<=1 or sys.argv[1]=='--help' or sys.argv[1]=='-h':

    # This prints out a sample of how you might use this command
    print("usage:",sys.argv[0], '--help')
    print('-h     : print this help message and exit (also --help)')
    print('-p     : plays one or more .wav files (also --play)')

    # Note that it is proper hygiene to have this at the end of each
    sys.exit(0);

'''
# HELP: This is another command line argument, invoked by typing --count or -c.
For example:
>> python cli_example.py --count
>> python cli_example.py -c *
>> python3 cli_example.py -c ../sounds/*.wav
    we use this command to count the number of wav files in sounds dir
'''
# Count is pretty basic: It just counts the command line arguments that come after it
if sys.argv[1] == '-c' or sys.argv[1] == '--count' :
    print("counted ", argvlen-2, " argument"+"s" if argvlen-2>1 else "")
    sys.exit(0)

'''
To add additional command line arguments, that have more capabilities, you need create more if statements.
For example, if we want to play a file, we should construct a new if statement to parse the following that you might 
enter into the command line:
>> python cli_example.py --play sounds/toaster.wav
>> python cli_example.py -p sounds/coffee.wav
'''

# TODO: Add in the play command by writing a new if statement
'''
You can use count as a template/example.
For now, it doesn't have to actually play a file, but it should take in a filepath as an additional argument
that comes after play (see the examples above).

For now, just have it print out the statement:
"I am now playing <filepath>."

(You'll add in the ability to actually play in the next step.)
'''

# ADD YOUR CODE FOR PLAY HERE
if (sys.argv[1] == '-p' or sys.argv[1] == '--play') and argvlen >= 3:
    for sound in sys.argv[2:]:
        play_sound(sound)
    sys.exit(0)

# Code for listing all available sounds with the command "-all"
if (sys.argv[1] == '--all'):
    directory = "sounds"
    files = os.listdir(directory)
    for file in files:
        print(file) 
    sys.exit(0)

'''
This goes at the end of all of your if statements and it lets you know if you have 
unknown or unaddressed command line arguments.
'''
print(sys.argv[0], "error, unexpected arguments ", sys.argv[1:],file=sys.stderr)

sys.exit(1)