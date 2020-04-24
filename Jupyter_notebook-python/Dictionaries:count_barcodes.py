#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[17]:


NAME = "Gera Perez"
COLLABORATORS = ""


# # ICA8 - Using a dictionary to count barcodes
# The goal of this assignment is to use a dictionary to count the number of times each barcode appears in a sequencing dataset. Be sure to follow the directions in the assignment, or the unit tests will fail. When you begin coding, remove the ```raise NotImplementedError()``` command.
# 
# Decompress s_1_sequence.txt.gz into your working directory on your own computer. Remember to start with a subset of the data to test your code. (Suggestion: `head -40 s_1_sequence.txt > test.txt` in your terminal) Be sure to change back to s_1_sequence.txt for your final submission.

# In[18]:


# create a dictionary called barcodes

barcodes = {}

        

        
        


# In[19]:


#Autograder tests, do not change
assert barcodes == {}, "barcodes not empty dictionary"


# # Populate your dictionary
# * Read each FASTQ record and pull the barcode off the sequence from each record.
# > [Hint](hint1.ipynb)
# * Each barcode will be a key for your dictionary. Increment the counter for each barcode in the dictionary when you encounter that barcode in a sequence.
# > [Hint](hint2.txt)
# 
# *Remember to test your code each step of the way.*

# In[20]:


# opens a text file to read and stores the text file as a variable.
with open("/Users/gerardoperez/Documents/shell/s_1_sequence.txt","r") as fh:   
    
    # Initiates a variable.
    count = 0
    
    # A for loop that goes through each line in the text file.
    for line in fh:
        
        # updates the variable by an addition of one after each loop.
        count = count + 1
        
        # If statemnt to get the second line from each record in text file.
        if count%4 == 2:
            
            # Intitates a variable.
            Num = 0
            
            # Slices the first 5 characters of the line.
            bcode = line[0:5]
            
            # if else statement that checks if 5 character slice is in dictionary.
            if bcode in barcodes:
                
                # if true then add a 1 to the value of the key.
                barcodes[bcode] = barcodes[bcode] + 1
            else:
                
                # if false, then store 1 as a value for the key.
                barcodes[bcode] = 1
            
# closes text file            
fh.close()


# In[21]:


#Autograder tests, do not change
assert len(barcodes) == 976, "Dictionary wrong length"
assert barcodes["ACTGC"] == 10659, "ACTGC count incorrect"


# # Write out your results
# * Write all the barcodes in your dictionary along with their counts to a file called `barcodes.tsv` in your repo. You should order the barcodes from highest counts to fewest counts. The format should be `barcode` [tab] `count`.

# In[22]:



# creates an empty dictionary
my_dict = {}

# A for loop that goes through the items in the dictionary.
for key, value in barcodes.items(): 
    
    # Reverses key to value and value to key in dictionary.
    my_dict[value] = key 



# opens a tsv file to write and stores the tsv file into a variable.
f = open("barcodes1.tsv", "w")

# A for loop that sorts the keys in a dictionary and reverses the order
# from highest to lowest.
for key in sorted(my_dict.keys(), reverse = True):

    # writes the formatted output to the tsv file.
    f.write("%s\t%s\n" % (my_dict[key],key))

# closes tsv file
f.close()


# In[23]:


#Autograder tests, do not change
import os
assert os.path.isfile("barcodes.tsv"), "Requested file not created"


# List (at least) three data types that can be used as dictionary keys.

# Integers, floats and strings.

# **CHALLENGE**: Determine how many reads fall below a specified quality score.
# * Translate the quality scores for each FASTQ record and determine the average quality score for that read (hint: what encoding?).
# * Tally the number of reads that fall below the threshold (you choose the threshold).
# * Print the number of sequences read, and the number and the percent of reads that fell below your chosen threshold.

# In[24]:


'''Report results for challenge here, including the threshold you chose'''
# YOUR CODE HERE


# In[ ]:





# In[ ]:





# In[ ]:




