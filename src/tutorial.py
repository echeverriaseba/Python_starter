# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
 

# %% 5. Working with data using NumPy package 
import numpy as np # imports the NumPy package (similar to R's library()) and assigns it the "np" labell

a = np.arange(15).reshape(3, 5) 
a 





















