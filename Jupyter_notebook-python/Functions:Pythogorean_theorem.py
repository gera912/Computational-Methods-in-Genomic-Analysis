#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[1]:


NAME = "Gera Perez"
COLLABORATORS = ""


# # ICA7 - Transitioning to Python: Functions

# ## Write a function to calculate the Pythagorean theorem
# $$a^2 + b^2 = c^2$$
# 1. The function should take 2 parameters (a and b), compute the value of c and return it
# 2. Call your function with several different values for a and b and print the results
# 3. Check your work with a calculator
# 4. After writing your function in Jupyter Notebook, convert it to a .py file and execute it from the command line
# 
# Turn in your completed Jupyter Notebook and your .py file to GitHub.

# In[2]:


# Imports a module.
import math

# Creates a method that takes two parameters.
def pythag(a,b):
    '''Computes the length of the hypotenuse of a right triangle given the lengths
    of the other two sides.'''
    
    # creates a variable that squares each parameter then computes an addition. 
    x = (a**2) + (b**2) 
    
    # creates a variable that stores the square root of a previous result.
    c = math.sqrt(x)
    
    # Returns a variable that has a result.
    return c


# In[3]:


# calls a method
pythag(1,2)


# In[4]:


'''Check function results, do not change this cell'''
assert pythag(3,4) == 5, "fails 3,5 test"
assert pythag(5,12) == 13, "fails 5,12 test"
assert pythag(9,40) == 41, "fails 9,40 test"


# Convert your Jupyter notebook to a script and be sure to upload the script to your repo. Include the name of your script file in the text box below.

# YOUR ANSWER HERE

# In[5]:


# ICA7.py


# In[ ]:




