### Learning to Speak Object Oriented ###

### Word Drills ###

# class: tell Python to make a new type of thing.

# object: two meanings (1) the most basic type of thing and (2) any instance of some thing.

# instance: what you get when you tell Python to create a class.

# def: how you define a function inside a class.

# self: inside the functions in a class, self i sa variable for the instance/object being accessed.

# inheritance: the concept that one class can inherit traits from another class, much like you and your parents.

# composition: the concept that a class can be composed of other classes as parts, much like how a car has wheels.

# attribute: a property classes have that are from composition and are usually variables.

# is-a: a phrase to say that something inherits from another, as in a "salmon is-a fish".

# has-a: a phrase to say that something is composed of other things or has a trait, as in "a salmon has-a mouth".

### Phrase Drills ###

class X(Y) === "Make a class named X that is-a Y"

class X(object): def __init__(self, J) === "Make a class named X that has-a __init__ that takes self and J parameters"

class X(object): def M(self, J) === "Make class X that has-a function M that takes self and J parameters"

foo = X() === "Set foo to an instance of class X"

foo.M(J) === "From foo, get the M function and call it with parameters self, J"

foo.K = Q === "In foo, get the variable K and set it to Q"
