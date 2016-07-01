# Strings and Text

# A string is usually a bit of text you want to display or "export" out of the program. Python recognizes strings with either single or double quotes.

# You can use format characters inside strings, and then follow the string with % and the variable. If you use multiple format strings, you do % (list of variables in parentheses)

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e