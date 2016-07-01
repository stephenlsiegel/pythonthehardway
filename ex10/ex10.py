# What Was That?

# In the last exercise, we saw two ways to make a string that goes across multiple lines.
# The first way was to use the \n newline character

# The \ (backslash) character is used for "escape sequences".

# For example, how would you put a double quote inside a string that uses double-quotes?
# eg uncomment the following and see what happens
# "I want to print some dialogue: Stephen said, "What will happen here?" and oh boy."

# We need a way to tell Python that the dialogue double quotes aren't string double-quotes.

# Two ways to solve this problem:

# (1) Use an escape character

print "Stephen said, \"What will happen here?\" and it worked."

# (2) Use triple quotes
print """Stephen said, "What will happen here?" and it also worked."""

# You can put as many lines inside of the triple quotes as you want.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Escape sequences:

# \\
# \'
# \"
# \a
# \b
# \f
# \n
# \N
# \r
# \t
# \uxxxx
# \Uxxxxxxxx
# \v
# \ooo
# \xhh

print "Testing a \v vertical tab"

print "Testing a \aASCII bell."
print "\a\a\a\a\a\a" # This will cause your computer to make bell sounds

print '''Testing triple 
quotes'''