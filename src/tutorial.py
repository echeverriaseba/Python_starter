# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 1. Defining a function ####

def hello():
    """Print "Hello World" and return None."""
    print("Hello World")


hello()

dir() # Inspecting objects defined in the Console

help(hello) # Returns the additional information included as documentation string in the function

# 1. Automatic Symbolic Python ####
# after installing SymPy Python package with:
# conda install SymPy
# import SymPy

# e.g. 1:
expr = (x + y) ** 3
expr # returns the previous expression in LaTex math syntax

expr.expand() # opens the polynome    
    
# e.g. 2:   
expr2 = (x + y + z) ** 3
expr2 # returns the previous expression in LaTex math syntax

expr2.expand() # opens the polynome

