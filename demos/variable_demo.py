# 2022.03.11 This is a demonstration of declaring variables in python

# Variable statements (lines of code) start with an identifier.
# Identifiers are user-defined (i.e. the programmer, you) names we use for
# variables, functions, classes, and other things in python.

# You can name things pretty much however you wish, with a few exceptions.

# Valid characters in identifiers include:
#
# lower case letters
# upper case letters
# digits (0 to 9)
# underscore (_)

# Note that identifiers *cannot* start with a digit.

#------------------------------------------------------------------------------
# Example 1:

# Here is a complete variable assignment statement demonstrating an identifier.
# It demonstrates the common pattern:
# [identifier] [equals] [expression].
# (Don't worry about expressions, we will get to them later).

temperature = 12

# Here the identifier is 'temperature'.  It conforms to our rules above.

#------------------------------------------------------------------------------
# Example 2:
_my_name = 'Johannes Kepler'
print("My name is " + _my_name)

# Here we start a variable name with an underscore.  It's a little weird, but
# it is valid.  We use leading underscores by convention to denote private
# variables.  But don't worry about that for now.

# Also note we have an underscore within the name.

# Typically, we want to name our variables something descriptive and we can
# use multiple words like in a phrase.  For example we may want a variable
# referring to the temperature of the sun.  We may name it "sun_temperature".

# Generally when we name something with multiple words, instead of putting
# spaces in the variable name (this is disallowed), we put underscores to
# represent the space.  The practice of using underscores this way is called
# snake case.  (There are other styles like camel case).

sun_temperature = 5778

print("The temperature of the sun is " + str(sun_temperature) + "K")

# (Note the temperature of the sun is apparently 5778 K).


# That's it for now!  Here are some exercises:

# 1.) Create a new file in our repository under the exercises folder called variable-exercise.py

# 2.) Declare four variables and assign them some values as follows:
#     a.) declare an variable with an identifier without snakecase, assign it an integer
#     b.) declare an variable with an identifier without snakecase, assign it a string
#     c.) declare an variable with an identifier with snakecase, assign it an integer
#     d.) declare an variable with an identifier with snakecase, assign it a string

# Be creative about your variable names!
