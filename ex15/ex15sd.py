# Reading Files

# imports the argv function from the sys module
from sys import argv

# declares that calling python at the command line will take two arguments, the script name and a filename
script, filename = argv

# saves a variable txt the opens/stores the file given by the second argument (filename)
txt = open(filename)

# prints out "Here's your file " and the name of the file
print "Here's your file %r:" % filename

# First runs the .read() function on the txt object, then prints the result to the console
print txt.read()

# print a text string to the console
print "Type the filename again:"

# stores a string input in the file_again variable and prompts the user with >
file_again = raw_input("> ")

# stores a file object to txt_again variable that is the file_again user input
txt_again = open(file_again)

# reads and prints out the txt_again file
print txt_again.read()


# STUDY DRILLS

# (1) Above each line, write a comment about what it does. Done

# (2) Note: the .read() function can be called a "function", "command", or "method". We will learn about this later.

# (3) Have your script also call close() on the txt and txt_again variables. It's important to close files when you're done with them.

txt.close()
txt_again.close()