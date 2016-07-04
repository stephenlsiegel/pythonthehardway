# Is-A, Has-A, Objects, and Classes

# Animal is-a object (yes, sort of confusing, look at the extra credit)
class Animal(object):
	pass
	
# Dog is-a Animal and has-a __init__ function that takes parameters self, name
class Dog(Animal):

	def __init__(self, name):
		# Dog has-a attribute name
		self.name = name

# 
class Cat(Animal):
	
	def __init__(self, name):
		#
		self.name = name

# Person is-a object and has-a __init__ function that takes parameters self, name
class Person(object):
	
	def __init__(self, name):
		# Person has-a attribute name
		self.name = name
		
		# Person has-a pet of some kind
		self.pet = None

# Employee is a Person and has-a __init__ function that takes parameters self, name, salary
class Employee(Person):

	def __init__(self, name, salary):
		# 
		super(Employee, self).__init__(name)
		# Employee has-a attribute salary
		self.salary = salary

# Fish is-a object
class Fish(object):
	pass
	
# Salmon is-a Fish
class Salmon(Fish):
	pass
	
# Halibut is-a Fish
class Halibut(Fish):
	pass

# rover is-a Dog
rover = Dog("Rover")

# satan is a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet satan who is-a Cat
mary.pet = satan

#
frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
