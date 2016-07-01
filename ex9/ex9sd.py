# Printing, Printing, Printing

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:", days
print "Here are the months:", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

# STUDY DRILLS

# (1) Why do the \n newlines not work when I use %r?

print "Here are the months: %r" % months
# result: Here are the months: 'Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug'
# This occurs because %r uses the repr() function, or as Zed says, it prints the "raw programmer's" version of the variable.

# (2) Why do I get an error when I put spaces between the three double quotes?

# This code will give an error, you have to type the double quotes without spaces """
# print " " "
# This is a test
# " " "" 