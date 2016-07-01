# Numbers and math

# + plus | addition
# - minus | subtraction
# / slash | division
# * asterisk | multiplication
# % percent | modulus arithmetic (X % Y = X divided by Y with J remaining, returns J)
# < less-than (returns True/False boolean)
# > greater-than
# <= less-than-equal
# >= greater-than-equal

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6 # 30
print "Roosters", 100 - 25 * 3 % 4 # 97

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 # 6.75...no, 7 (because integers)

print "Is it true that 3 + 2 < 5 - 7?"

print 3+2 < 5 - 7 # false

print "What is 3 + 2?", 3 + 2 # 5
print "What is 5-7?", 5 - 7 # -2

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2 # True
print "Is it greater or equal?", 5 >= -2 # True
print "Is it less or equal?", 5 <= -2 # False


# Study drill - rewrite the eggs as floating point numbers
# You should now get 6.75

print 3.0 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6 # 6.75

# Note that without floating point numbers, Python drops the fractional part (it's technically not rounding down). So 3/4 = 0, 3.0/4.0 = 0.75