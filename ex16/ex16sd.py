# (1) Write a script similar to the last exercise that uses read and argv to read the file you just created.

from sys import argv

script, filename = argv

txt = open(filename, 'r')

print txt.read()


# (2) Thre's too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, line3
# with juse one target.write() command instead of six.

print "Opening the file..."
target = open(filename, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target_new = line1 + "\n" + line2 + "\n" + line3 + "\n"

target.write(target_new)

print "And finally, we close it."
target.close()