# Lesson 2: More Variables

# Description:
#
# In this exercise we will learn more about variables.  Here are the goals for
# this exercise:
#
#   1.) Learn more data types
#   2.) Combine variables with operators to form expressions


# 2.1 More Data Types
#
# Previously we have learned about two types of variables:#
#
#   integers - which store integer numbers
#   strings - which store character data
#
# It turns out there are even more data types than that in Python.
#
#   float - stores decimal values (i.e. 2.5, 0.1, -1.2)
#   list - stores a list of items (i.e. [1, 2, 3])
#   dict - stores a dictionary of items (i.e. {"a": 1, "b": 2})

# Example 1: Our Name and Height

# Let's store our name and height into some variables

# store our name into a string
my_name = "Dr. Ray Mendoza"
print("Hello!  I'm " + my_name)

# store our height into a float
height = 5.66
print("My height is " + str(height))

# Some details:
#
# Notice we are combining our my_name and height variables with some string
# using the plus symbol '+' *inside* the print statements.

# let's be sneaky and increase our height by 1 foot!
height = height + 1

print("My new height is " + str(height))

# An important distinction:
# in the line where we increased height by 1 the left-hand side is the variable
# we are assigning the evaluation of the right hand side expression.

# So even though we are using the same variable, it is being assigned the
# evaluation of the right hand side.

# Do not confuse 'assignment' with 'equality'.

# So, we have used '+' in a few contexts now.
# What about subtraction '-', multiplication '*', or division '/'?

# We will conver that in section 2.2

# 2.2 Complex Data Types

# We have more complex data types which combine the more fundamental data types.

# The first is a list.

# A list represents a list of things.  These things can be things like ints,
# floats, or strings, or generally any other objects.

# We define lists just like we define variables.

# Example 2: Our Grocery List

# Lists
# standard indentation is 4 spaces
my_grocery_list = [
    "bananas",
    "fruit smoothie",
    "spaghetti"
    ]

print(my_grocery_list)

# Aside: '\n' escape characters
print("this line\nthat line")

length = len(my_grocery_list)

# write a print statement that will say
# "my grocery list has _ items"

print("my grocery list has " + str(length) + " items")

print("My grocery list is " + str(my_grocery_list))

# 2.3 Operators
#
# Operators allow us to alter one or more data types in way defined by the
# operator.
#
# Some common ones are those for the basic arithmetic:
#
#   + : addition
#   - : subtraction
#   * : multiplication
#   / : division
#
# These are called binary datatypes because they act on two data types.

# Example 3: Adding Two Numbers

# Let's add two numbers
x = 1
y = 5

# here we're assigning 'z' to the value of the expression 'x + y'
z = x + y

# Let's display the values
print("x is " + str(x))
print("y is " + str(y))
print("z is " + str(z))

# Let's investigate the types of each of these.
# We can know the type of a given variable using the 'type' built-in function.
type_of_x = type(x)
type_of_y = type(y)
type_of_z = type(z)

print("the type of x is " + str(type_of_x))
print("the type of y is " + str(type_of_y))
print("the type of z is " + str(type_of_z))

# Example 4: More Complex Expressions

# Today's temperature in degrees Fahrenheit
f_temperature = 70
c_temperature = (f_temperature - 32) * 5 / 9

print("The temperature in Fahrenheit is " + str(f_temperature))
print("The temperature in Celsius is " + str(c_temperature))

# And let's in turn check their types
# But this type let's put it all in the print statements
print("the type of f_temperature is " + str(type(f_temperature)))
print("the type of c_temperature is " + str(type(c_temperature)))

# Observe that one is an int, and the other is a float!
# When we divide things, there is a possibility that the result is a decimal, so
# the resulting type of a division is a float.

# We also have been using examples where we combine strings with other strings
# using the '+' operator inside our print statements.

# Some caveats about operators:

# Notice that inside our print statements we use the 'str' keyword a lot to
# convert the datatype to a string.  The reason we do is is to allow the '+'
# operator to correct combine a string with another string.

# If you try to run 'my string' + 1.5 you will get a TypeError telling you you
# only concatenate a string to another string.


# In general for binary operators we have a left-hand side and a right-hand
# side.

# The lhs and rhs have their own data types.
# The combined expression has it's own data type.

# There are rules for which data types we can combine.  Some combinations work.
# Some do not.  Arithmetic works pretty much like we think it should, but things
# can get weird when we use arithmetic operators with strings.

# Example 5: Adding strings

# This are OK

new_string = "The quick brown fox" + " jumped over the lazy dog"
print(new_string)

# This is not OK
# print("This string " + 12)

# We cannot use the '+' operator in a <str> and an <int>.

# This is OK.  It is defined semantics and will duplicate the string 10 times
print("A string " * 10)

# In addition to binary operators which operate on two things, we also have
# unary operators which operate on one thing.

# https://www.educba.com/unary-operators-in-python/