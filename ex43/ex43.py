# Basic Object-Oriented Analysis and Design

# Process to build something using Python:
	# 1. Write or draw about the problem.
	# 2. Extract key concepts from (1) and research them.
	# 3. Create a class hierarchy and object map for the concepts.
	# 4. Code the classes and a test to run them.
	# 5. Repeat and refine
	
# The Analysis of a Simple Game Engine

### Write or Draw About the Problem ###

# Game is called Gothons from Planet Percal #25

# "Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below. The game will be more like a Zork or Adventure type game with text outputs and funny ways to die. The game will involve an engine that runs a map full of rooms or scenes. Ech room will print its own description when the player enters it and then tell the engine what room to run next out of the map."

# At this point I want to describe each scene:

# Death
	# This is when the player dies and should be something funny.
# Central Corridor
	# This is the starting point and has a Gothon already standing there they have to defeat with a joke before continuing.
# Laser Weapon Armory
	# This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad the hero has to guess the number for.
# The Bridge
	# Another battle scene with a Gothon where the hero places the bomb.
# Escape Pod
	# Where ther hero escapes but only after guessing the right escape pod.
	
### Create a CLass Hierarchy and Object Map for the Concepts ###

# * Map
	# - next_scene
	# - opening_scene
# * Engine
	# - play
# * Scene
	# - enter
	# * Death
	# * Central Corridor
	# * Laser Weapon Armory
	# * The Bridge
	# * Escape Pod
	
from sys import exit
from random import randint
	
### Code the Classes and a Test to Run Them ###
class Scene(object):
	
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		# be sure to print out the last scene
		current_scene.enter()

class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a loser.",
		"I have a small puppy that's better at this."
		]
	
	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		exit(1)

class CentralCorridor(Scene):
	
	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew."
		raw_input("...")
		print "You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod."
		raw_input("...")
		print "You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown clostume flowing around his hate-filled body."
		raw_input("...")
		print "He's blocking the door to the Armory and about to pull a weapon to blast you."
		
		action = raw_input("(shoot!, dodge!, tell a joke) > ")
		
		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			raw_input("...")
			print "His clown costume is flowing and moving around his body, which throws off your aim."
			raw_input("...")
			print "Your laser hits his costume but misses him entirely."
			raw_input("...")
			print "This completely ruins his brand new costume his mother bought him, which makes him fly into an insane rage and blast you repeatedly in the face until you are dead. Then he eats you."
			return "death"
			
		elif action == "dodge!":
			print "Like a world-class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head."
			raw_input("...")
			print "In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out."
			raw_input("...")
			print "You wake up shortly after only to die as the Gothon stomps on your head and eats you."
			return "death"
			
		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			raw_input("...")
			print "You tell the one Gothon joke you know:"
			raw_input("...")
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			raw_input("...")
			print "The Gothon stops, tries not to laugh, then bursts out laughing and can't move."
			raw_input("...")
			print "While he's laughing you run up to him and shoot him square in the head then jump through the Weapon Armory door."
			raw_input("...")
			return "laser_weapon_armory"
		
		else:
			print "DOES NOT COMPUTE!"
			return "central_corridor"
			
class LaserWeaponArmory(Scene):
	
	def enter(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding."
		raw_input("...")
		print "It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container."
		raw_input("...")
		print "There's a keypad lock on the box and you need the code to get the bomb out. The code is 3 digits. Guess a number between 0 and 999. You get 10 guesses."
		code = "%d%d%d" % (randint(0,9), randint(0,9), randint(0,9))
		guesses = 1
		guess = raw_input("My guess is > ")
		
		while guess != code and guesses < 10:
			print "BZZZZEDDD!"
			
			if int(guess) > int(code):
				print "Your guess was too high!"
			else:
				print "Your guess was too low!"
			
			print "You've used %d of 10 guesses." % (guesses)
			guesses += 1
			guess = raw_input("[keypad] > ")
			
		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			raw_input("...")
			print "You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot."
			raw_input("...")
			return "the_bridge"
		else:
			print "The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together. The code was %s." % (code)
			raw_input("...")
			print "You decide to sit there, and finally the Gothons blow up the ship from their ship and you die."
			return "death"

class TheBridge(Scene):

	def enter(self):
		print "You burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship."
		raw_input("...")
		print "Each of them has an even uglier clown costume than the last. They haven't pulled their weapons out yet, as they see the active bomb under your arm and don't want to set it off."
		
		action = raw_input("(throw the bomb, slowly place the bomb) > ")
		
		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons and make a leap for the door."
			raw_input("...")
			print "Right as you drop it a Gothon shoots you right in the back, killing you."
			raw_input("...")
			print "As you die you see another Gothon frantically trying to disarm the bomb."
			raw_input("...")
			print "You die knowing they will probably blow up when it goes off."
			return "death"
		
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat."
			raw_input("...")
			print "You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing your blaster at it."
			raw_input("...")
			print "You then jump back through the door, punch the close button, and blast the lock so the Gothons can't get out."
			raw_input("...")
			print "Now that the bomb is placed you run to the escape pod to get off this tin can."
			return "escape_pod"
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"
		
class EscapePod(Scene):
	
	def enter(self):
		print "You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes."
		raw_input("...")
		print "It seems like hardly any Gothons are on the ship, so your run is clear of interference."
		raw_input("...")
		print "You get to the chamber of escape pods, and now need to pick one to take."
		raw_input("...")
		print "Some of them could be damaged but you don't have time to look."
		raw_input("...")
		print "There's 5 pods, which one do you take?"
		
		good_pod = randint(1,5)
		guess = raw_input("[pod #] > ")
		
		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			raw_input("...")
			print "The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly."
			return "death"
		else:
			print "You jump into pod %s and hit the eject button." % guess
			raw_input("...")
			print "The pod easily slides out into space heading to the planet below."
			raw_input("...")
			print "As it flies to the planet, you look back and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time. You won!"
			
			return "finished"

class Finished(Scene):
	
	def enter(self):
		print "You Won! Good job."
		return "finished"
		
class Map(object):

	scenes = {
		"central_corridor": CentralCorridor(),
		"laser_weapon_armory": LaserWeaponArmory(),
		"the_bridge": TheBridge(),
		"escape_pod": EscapePod(),
		"death": Death(),
		"finished": Finished()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()