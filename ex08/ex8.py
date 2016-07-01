# Printing, Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four") # prints with single quotes around each
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# Question: why does the "But it didn't sing" line of the formatter print with double quotes while all the others print with single quotes?

# Answer: Because there is a single quote in the word didn't! This one confused me a bit at first


# Question: what is the difference between %s and %r?

# Answer: %s calls the str() function, %r calls the repr() function. From the Python documentation: The difference with repr(object) is that str(object) does not always attempt to return a string that is acceptable to eval(); its goal is to return a printable string.

# Answer 2 (from PtHW): %r is mostly used for getting debugging information, so you should prefer %s.
