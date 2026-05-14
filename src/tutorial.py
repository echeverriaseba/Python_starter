# -*- coding: utf-8 -*-
"""
This script goes through basic Python commands and synthax. ¡
"""

# %% 1. Defining functions 

def hello():
    """Print "Hello World" and return None.""" # note that indentation (number of spaces) replaces R's {}.
    print("Hello World")

hello()

dir() # Inspecting objects defined in the Console

help(hello) # Returns the additional information included as documentation string in the function

#%reset -f #resets the namespace (analogue to R's environment)...similar to rm() in R

def hello2(name):
    """Given an object 'name', print 'Hello ' and the object."""
    print("Hello {}".format(name))

i = 42
if __name__ == "__main__": # this is used to run the function only if this cell is not imported from another module. Scripts in Python have as default __name__ == "__main__", when imported then __name__ = "name of the imported script".
    hello2(i)

# %% 2. Automatic Symbolic Python 

# after installing SymPy Python package with:
# conda install SymPy
# import SymPy

# e.g. 1:
#expr = (x + y) ** 3
#expr # returns the previous expression in LaTex math syntax

#expr.expand() # opens the polynome    
    
# e.g. 2:   
#expr2 = (x + y + z) ** 3
#expr2 # returns the previous expression in LaTex math syntax

#expr2.expand() # opens the polynome

# %% 3. Documentation string formatting 

# Documenting the code using reStructuredText (reST) format
# run this cell (Ctrl+Enter) and then use (Ctrl+I) on top of average() to access its information

def average(a, b):
    """
    Return the average value (arithmetic mean) of two numbers.

    Parameters
    ----------
    a : numeric
        A number to average.
    b : numeric
        Another number to average.

    Returns
    -------
    result : numeric
        The average of a and b, computed using ``0.5 * (a + b)``.

    Example
    -------
    >>> average(5, 10)
    7.5

    """

    return (a + b) * 0.5

result = average(100,50) # note here that this is not part of the function any more because the 4 spaces indentation is missing. In R this would be defined within a {} block as in: name <- function(arguments){workflow}
print(result)

globals()

# %% 4. Debugging

# When running a cell (Ctrl+Enter) the console shows only the final result of all lines within a cell. In order to look for mistakes("bugs") we open the debugging mode with Ctrl+F5. Let's say we have:
    
def average(a,b):
    result = a + b / 2 # the mistake is here due to a lack of parentheses.
    return result

a = 4
b = 6

avg = average(a, b)
print(avg) # prints 7.0 intead of 5.0

# Here we enter the debugging mode with Ctrl+F5. Spyder will:
# - highlight the first executable line
# - open the debugger console (ipdb>)
# use debug commands n, s, c, and p to identify the error and correct the function
 
type(avg) #  A float in Python is a data type used to represent numbers that have a decimal point
type(a) # Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# %% 5. The math library

import math # the math library contains basic math equations like sin() and sqrt(), and values such as pi().
math.sin(3)
math.sqrt(25)
math.sqrt(math.pi)

# %% 6. Creating and using lists

station_names = [
    "Helsinki Harmaja",
    "Helsinki Kaisaniemi",
    "Helsinki Kaivopuisto",
    "Helsinki Kumpula",
]

print(station_names) # use from now on to check the current state of the list

len(station_names) # analogue to R's lenght()

station_names[1] # just as in R, list elements can be accessed with their index values. Note here again that, as Python starts values stored in collections with the index value 0, this returns the second value.
type(station_names[1])

station_names[3] = "modified value" # edit a value within the list

station_names.append("new value") # add a new value to the list

del station_names[2] # removing a list value by its index

station_names.remove("new value") # removing a list value by its name

station_names.count("Helsinki Harmaja") # checking how many times a value is contained in a list

station_names.index("Helsinki Harmaja") # checkin a value's index within a list

station_names.reverse() # to reverse the order of items in a list

# %% 7. Working with text and numbers
# Station information
station_name = "Helsinki Kaivopuisto" # type(station_name) = str
station_id = 132310 # type(station_id) = int
temp = 18.56789876 # type(temp) = float

# The f-string approach
# Here the f character activates the f-string functionality
# The .2f is the Format specifier (precision and type), without it then the entire temp value is printed.
info_text = (
    f"The temperature at {station_name} (ID: {station_id}) is {temp:.2f} Celsius."
)
print(info_text)

text = "Stations: Helsinki Kumpula, Helsinki Kaisaniemi, Helsinki Harmaja"

# %% 8. Manipulating character strings 
# %% 9. Working with data using NumPy package 
import numpy as np # imports the NumPy package (similar to R's library()) and assigns it the "np" label

a = np.arange(15).reshape(3, 5) 
a # note that in Python vectors and matrixes start from 0, not 1 as in R.

help(np)




















