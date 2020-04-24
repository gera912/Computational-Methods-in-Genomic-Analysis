#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, restart the kernel (in the menubar, select Kernel→Restart) and then run all cells (in the menubar, select Cell→Run All).
# 
# Make sure you fill in any place that says YOUR CODE HERE or "YOUR ANSWER HERE", as well as your name and collaborators below:

# # Bi 621 – Problem Set 3
# ## Due before class, Monday, July 9
# 
# The goal of this problem set is to convert phred quality scores from their single letter encoding into integers and to calculate the average phred quality score for a single sequence. **Be sure to remove the ```raise NotImplementedError()``` from the code.**

# In[10]:


#initializing variables, do not change
id = "@GAAATG_1_1101_4446_2137_1"
seq = "TGCAGGTTGAGTTCTCGCTGTCCCGCCCCCATCTCTTCTCTTCCAGTCTGGCTCTGGAGCAGTTGAGCCCAGCTCAGGTCCGCCGGAGGAGACCG"
phred_score = "FFHHHHHJJJJIJIJJJIJJJJJJIIIJJJEHJJJJJJJIJIDGEHIJJFIGGGHFGHGFFF@EEDE@C??DDDDDDD@CDDDDBBDDDBDBDD@"


# # Part 1 – Convert_phred
# Write a function that takes a single character as it's parameter and converts that parameter into a phred score, and returns the phred score.
# >*Remember: Illumina 1.8+ phred scores are offset by a factor of 33 from 0. Review the lecture notes as well as the [Wikipedia FASTQ page](https://en.wikipedia.org/wiki/FASTQ_format) to see how to do the conversion.*
# 
# *HINT* – what does the ord() function do? Check the documentation

# In[11]:


# Creates a method that takes an instance variable.
def convert_phred(letter):
    """Converts a single character into a phred score"""
    
    # Creates a variable that stores a difference 
    # of -33 of the unicode point from the instance variable. 
    x=ord(letter) - 33
    
    # returns a variable with the result.
    return x
  


# Check to see that your code works.

# In[12]:


# Calls a method. 
convert_phred('A')


# In[13]:


#autograder tests, do not change
"""Check that convert_phred returns the correct value for several different inputs"""
assert convert_phred("I") == 40
assert convert_phred("C") == 34
assert convert_phred("2") == 17
assert convert_phred("@") == 31
assert convert_phred("$") == 3


# # Part 2 – Convert the entire phred string
# Write a loop print each letter in the `phred_score` string and its corresponding score in the following format:
# ```
# 0: F - 37
# 1: F - 37
# 2: H - 39
# 3: H - 39
# 4: H - 39
# 5: H - 39
# 6: H - 39
# 7: J - 41
# ...```
# Reminder, start simply.
# * Write a loop to iterate over each letter in the `phred_score` and print them out.
# * Modify your loop to print the letter and the corresponding score. *Be sure to use your `convert_phred` function*.
# * Alter the loop to print out an index: 0 for the first letter, 1 for the 2nd letter, etc.
# * Be sure your formatting matches the requested output.

# In[14]:


# Creates a variable
count = 0

# A for loop that goes through a string.
for letter in phred_score:
    
    # prints a statement in a specific format
    print("{0}: {1} - {2}".format(count, letter, convert_phred(letter) ))
    
    # Adds a count of 1 to the variable.
    count= count + 1


# Write a second function that takes the original, unmodified `phred_score` string as a parameter. This function should calculate the average quality score of the whole phred string.
# > Struggling? See some [hints](PS3_hints.ipynb)

# In[15]:


# Creates a method that takes an instance variable.
def qual_score(phred_score):
    """Calculates a quality score from a phred score"""
    
    # Creates a variable
    count = 0
    total = 0
    
    # A for loop that goes through a string.
    for letter in phred_score:
        
        # Creates a variable to store the total sum of the phred scores.
        total= convert_phred(letter) + total
        
        # Adds a count of 1 to the variable.
        count = count + 1
        
    # returns the average result for the quuality score.
    return (total/count)


# In[16]:


# Prints a statement.
print(qual_score(phred_score))


# In[17]:


#autograder tests, do not change
old_convert_phred = convert_phred
del convert_phred

try:
    qual_score(phred_score)
except NameError:
    pass
else:
    raise AssertionError("qual_score does not call convert_phred")
finally:
    convert_phred = old_convert_phred
    del old_convert_phred


# In[18]:


#autograder tests, do not change
assert qual_score(phred_score) == 37.62105263157895


# In[ ]:





# In[ ]:




