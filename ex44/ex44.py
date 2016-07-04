# Inheritance vs. Composition

# Inheritance is something to use carefully. Most uses of inheritance can be simplified or replaced with composition, and multiple inheritance should be avoided at all costs.

### What is Inheritance? ###

# Inheritance is used to indicate that one class will get most or all of its features from a parent class. There are three ways the parent and child classes can interact.
	
	# 1. Actions on the child imply an action on the parent.
	# 2. Actions on the child override the action on the parent.
	# 3. Actions on the child alter the action on the parent.
	
### Implicit Inheritance ###

# Implicit actions that happen when you define a function in the parent, but not in the child.

class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

class Child(Parent):
	pass
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# Notice that we call son.implicit(), but the Child class does not have an implicit() function defined. If you put functions in a base class, then all subclasses will automatically get those features.
print '-' * 10

### Override Explicitly ###

# To override the implicit function, we can define it in the subclass as well.

class Parent(object):
	
	def override(self):
		print "PARENT override()"
		
class Child(Parent):
	
	def override(self):
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override()
son.override()

# In this example, we've overridden the Parent override function in Child, so son.override() will call the override function from Child.
print '-' * 10

### Alter Before or After ###

class Parent(object):
	
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.altered()
son.altered()

print '-' * 10

### All Three Combined ###

class Parent(object):
	
	def override(self):
		print "PARENT override()"
		
	def implicit(self):
		print "PARENT implicit()"
		
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	
	def override(self):
		print "CHILD override()"
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered() # This calls the Parent.altered() method inside the Child.altered() method.
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

print '-' * 5

dad.override()
son.override()

print '-' * 5

dad.altered()
son.altered()

### Using super() with __init ###

# The most common use of super() is actually in __init__ function in base classes. This is usually the only place where you need to do some things in a child, then complete the initialization in the parent. Example:

class Child(Parent):
	
	def __init__(self, stuff):
		self.stuff = stuff
		super(Child, self).__init__()

print '-' * 10

### Composition ###

# Inheritance is useful, but another way to do the exact same thing is just to use other classes and modules rather than rely on implicit inheritance.

class Other(object):
	
	def override(self):
		print "OTHER override()"
	
	def implicit(self):
		print "OTHER implicit()"
		
	def altered(self):
		print "OTHER altered()"
		
class Child(object):
	
	def __init__(self):
		self.other = Other()
		
	def implicit(self):
		self.other.implicit()
		
	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"
		
son = Child()

son.implicit()
son.override()
son.altered()

### When to Use Inheritance or Composition ###

# Both solve the problem of reusable code -- you don't want to have duplicated code all over your program. Here are three guidelines:

	# 1. Avoid multiple inheritance at all costs (that's something like class Child(Parent, Grandparent)
	# 2. Use composition to package code into modules that are used in many different unrelated places and siutations.
	# 3. Use inheritance only where there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.
	
### STUDY DRILLS ###

# Read PEP 8 - Style Guide for Python Code - https://www.python.org/dev/peps/pep-0008/