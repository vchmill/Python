Python
#1 
print("Hello, world! My name is Vitor Pereviazko")

#2
print("Hello!")  # this is my first comment

#3
greetings = "greetings"
print("greetings = " + str(greetings))
great_things = "from Lviv!"
print(str(greetings)+" "+ str(great_things))

#4
variable = 1
print(varibable)

#5
number = 9
print(type(number))   # print type of variable "number"

float_number = 9.0
print(type(float_number))

#6
number = 9
print(type(number))   # print type of variable "number"

float_number = 9.0
print(float_number)
print(int(float_number))

#7
number = 9.0        # float number

result = number/2

remainder = number % 2

print("result = " + str(result))
print("remainder = " + str(remainder))

#8
number = 9.0
print("number = " + str(number))

number -= 2
print("number = " + str(number))

number += 5

print("number = " + str(number))

#9
number = 9.0
print("number = " + str(number))

number -= 2
print("number = " + str(number))

number += 5

print("number = " + str(number))

#10
one = 1
two = 2
three = 3

print(one < two < three)  # This chained comparison means that the (one < two) and (two < three) comparisons are performed at the same time.

is_greater = three > two
print(is_greater)

#11
hello = "Hello"
world = 'World'

hello_world = hello+' '+world
print(hello_world)      # Note: you should print "Hello World"

#12
hello = "Hello"
world = 'World'

hello_world = hello+' '+world
print(hello_world)      # Note: you should print "Hello World"

#13
python = "Python"
print("h " + python[3])     # Note: string indexing starts with 0

p_letter = python[0]
print(p_letter)

#14
long_string = "This is a very long string!"
exclamation = long_string[-1]
print(exclamation)

#15
monty_python = "Monty Python"
monty = monty_python[:5]      # one or both index could be dropped. monty_python[:5] is equal to monty_python[0:5]
print(monty)
python = monty_python[6:]
print(python)

#16
ice_cream = "ice cream"
print("cream" in ice_cream)    # print boolean result directly

contains = "ice" in ice_cream
print(contains)

#17
phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
first_half = phrase[:int(len(phrase)/2)]
print(first_half)

#18
dont_worry = "Don't worry about apostrophes"
print(dont_worry)
print("\"Sweet\" is an ice-cream")
print('The name of this ice-cream is "Sweet\'n\'Tasty"')

#19
monty_python = "Monty Python"
print(monty_python)

print(monty_python.lower())    # print lower-cased version of the string

print(monty_python.upper())

#20
name = "John"
print("Hello, PyCharm! My name is %s!" % name)     # Note: %s is inside the string, % is after the string
years =28
print("I'm %d years old" % years)
