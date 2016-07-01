# More variables and printing

# In this lesson we will learn how to put variables in strings using a "format string".

my_name = 'Stephen L. Siegel'
my_age = 24
my_height = 73 # inches
my_weight = 195 # lbs
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)