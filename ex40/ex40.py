# Modules, CLasses, and Objects

# There is a construct in Python called a class that lets you structure your software in a particular way.

# Object-Oriented Programming is just weird. You have to struggle through it. Here we go.


# A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator.

class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"
	
	def apple(self):
		print "I AM CLASSY APPLES!"

# Objects are Like Import

# You can instantiate (create) a class by calling the class like it's a function, eg:
thing = MyStuff()
thing.apple()
print thing.tangerine

# 1. Python looks for MyStuff() and sees that it's a class you've defined.
# 2. Python crafts an empty object with all the functions you've specified in the class using def.
# 3. Python then looks to see if you made a "magic" __init__ function, and if you have it calls that function to initialize your newly created empty object.
# 4. In the MyStuff function __init__ I then get this extra variable self, which is that empty object Python made for me, and I can set variables on it just like you would with a module, dictionary, or other object.
# 5. In this case, I set self.tangerine to a song lyrics and then I've initialized this object.
# 6. Now Python can take this newly minted object and assign it to the thing variable for me to work with.

# I now have three ways to ge things from things:
	# dict style
	# mystuff['apples']
	
	# module style
	# mystuff.apples()
	# print mystuff.tangerine
	
	# class style
	# thing = MyStuff()
	# thing.apples()
	# print thing.tangerine

print ""
print "-" * 10
print ""

class Song(object):
	
	def __init__(self, lyrics):
		# Note: the lyrics are a list of strings.
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

print ""
print "-" * 10
print ""

bulls_on_parade.sing_me_a_song()

### STUDY DRILLS ###

print ""
print "-" * 10, "STUDY DRILLS", "-" * 10
print ""

midnight = Song(["In the midnight", "My arms were shaking", "While we were apart"])
midnight.sing_me_a_song()
print ""

wemove_lyrics = ["Here we are", "Extending into shooting stars", "In our houses", "In our cars"]
wemove = Song(wemove_lyrics)
wemove.sing_me_a_song()

