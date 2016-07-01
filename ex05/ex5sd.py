# More variables and printing

# In this lesson we will learn how to put variables in strings using a "format string".

name = 'Stephen L. Siegel'
age = 24
height = 73 # inches
height_cm = (height * 1.0) * 2.54 
weight = 195 # lbs
weight_kg = (weight * 1.0) / 2.20462
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That is %d centimeters." % height_cm
print "He's %d pounds heavy." % weight
print "That is %d kilograms." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Still getting integers for the height_cm and weight_kg calculations. Probably need to use something other than %?

# Yes, use %f, floating point decimal. %d is integer decimal.

print "He's %f centimeters tall." % height_cm
print "He's %f kilograms." % weight_kg

# You probably want to round to 1 or 2 decimals, but we can skip that for now.