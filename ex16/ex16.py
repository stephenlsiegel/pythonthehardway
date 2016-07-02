# Read and Writing Files

# Commands from the last lesson to remember:
	# close
	# read
	# readline (this reads just one line of a text file)
	# truncate (this empties the file, be careful)
	# write('stuff') (this writes "stuff") to the file
	
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you want to do that, hit RETURN."

# This pauses the script and allows the user to hit CTRL-C or RETURN
raw_input("?")

print "Opening the file..."
# Look up why the open command takes 'w' as its second argument.
# The first argument is the name of the file to open.
# The second argument is the "mode" of opening the file.
# Commonly used modes 'r' for reading, 'w' for writing (truncating the file if it exists), and 'a' for appending
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
