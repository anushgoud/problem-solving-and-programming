#!/usr/bin/env python
# coding: utf-8

# ### Standard Libraries
# - File i/o
# - Regular expression
# - Datetime
# - Math(numerical and mathematical)

# ## Write, Read,Analysis -- Data Science and Analysis

# ### File HAndling in Python
# - File:- Document containing information resides on the permanent stprage
# - Different types of files :- txt,doc,pdf,csv and etc ..
# - Input --Keyboard
# - Output --File
# ### Modes of the File I/O
# - 'w' -- This mode is used to file writing
#      -- If the file is not present first it creates the file and write so me data to it
#      -- If the file is already present then it will rewrite the previous content

# In[1]:


# Function to create a file and write to the file
def createFile(filename):
    f= open(filename,'w')
    for i in range(10):
        f.write('This is %d Line ' % i)
    print("File is created and data has written")
    return
createFile('file1.txt')


# In[2]:


ls


# In[3]:


def createFile(filename):
    f= open(filename,'w')
    f.write('Testing--\n')
    print("File is created and data has written")
    return
createFile('file1.txt')
    


# In[4]:


def appendData(filename):
    f=open(filename,'a')
    for i in range(10):
        print("This is %d Line\n" %i)
    print("File created and successfully data written")
    return
appendData('file2.txt')


# In[5]:


def appendData(filename):
    f=open(filename,'a')
    for i in range(10):
        f.write("This is %d Line\n" %i)
    print("File created and successfully data written")
    return
appendData('file2.txt')


# In[7]:


def appendData(filename):
    f=open(filename,'a')
    f.write("New Line 1 \n")
    f.write("New Line 2 \n")
    print("File created and successfully data written")
    f.close()
    return
appendData('file2.txt')


# In[8]:


# Function to read of the file
def readFileData(filename):
    f=open(filename,'r')
    if f.mode == 'r':
        x = f.read()
        print(x)
    f.close()
    return
readFileData('file2.txt')


# In[11]:


# Function to read the file
def fileOperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode =='r' :
            data = f.read()
            print(data)
        elif f.mode == 'a':
            f.write('Data to the file')
            print('The data successfully written')
    f.close()
    return
filename = input('Enter the file name')
mode = input('Enter the mode of the file')
fileOperations(filename,mode)
            


# In[16]:


# Data Analysis
# Word Count Program
def wordCount(filename,word):
    with open(filename, 'r') as f:
        if f.mode == 'r':
            x= f.read()
            li= x.split()    #It splits the string with whitespace
    cnt= li.count(word)
    return cnt
filename = input('Enter the file name :')
word = input('Enter the word :')  #which word count you need
wordCount(filename,word)


# In[17]:


# Character count from the given file
def charCount(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x=f.read()
            li = list(x)
    return len(li)
filename = input('Enter the filename : ')
charCount(filename)


# In[19]:


# Function to find the no. of lines in the i/p file
# i/p -- filename(file2.txt)
# o/p -- No of lines (12)

def countOfLines(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = x.split("\n")
    return len(li)
filename = input('Enter the filename : ')
countOfLines(filename)


# In[22]:


# Function to print the Upper and Lower characters
def caseCount(filename):
    cntUpper = 0
    cntLower = 0
    with open(filename,'r') as f:
        if f.mode =='r':
            x = f.read()
            li = list(x)
    for i in li:
        if i.isupper():
            cntUpper += 1  #cntUpper = cntUpper+1
        elif i.islower():
            cntLower += 1   #cntLower = cntLower+1
    output = 'Upper Case = {0} , Lower Case = {1}'.format(cntUpper,cntLower)
    return output
filename = input('Enter the filename : ')
caseCount(filename)


# ### math, random, os
# - os package it contains certain methods which works with os

# In[23]:


ls


# In[27]:


cd Desktop/probsolvingprogramming/git


# In[28]:


ls


# In[47]:


cd ..


# In[48]:


import os
os.listdir('git/')  # Listdir()  --ls


# In[49]:


li = os.listdir('git/')
for i in li:
    print(i)


# - Older version Python -- os.listdir()
# - New version Python   -- os.scandir() and pathlib.Path()

# In[50]:


li = os.scandir('git/')
for i in li:
    print(i)


# In[51]:


from pathlib import Path
li = Path('git/')
for i in li.iterdir():
    print(i.name)


# ### Listing all files in a Directory

# In[52]:


import os
dirPath = "git/"
for i in os.listdir(dirPath):
    if os.path.isfile(os.path.join(dirPath,i)):
        print(i)


# In[53]:


pwd


# In[11]:


cd git


# In[12]:


pwd


# ### Listing Subdirectories

# In[54]:


dirPath = 'git/'
for i in os.listdir(dirPath):
    if os.path.isdir(os.path.join(dirPath,i)):
        print(i)


# In[55]:


from pathlib import Path
dirPath = Path('git/')
for i in dirPath.iterdir():
    if i.is_dir():
        print(i.name)


# In[56]:


dirPath = 'Git/'
with os.scandir(dirPath) as f:
    for i in f:
        if i.is_dir():
            print


# ### Creating a Single Directory

# In[57]:


os.mkdir('SingleDirectory')


# In[58]:


import pathlib
p = pathlib.Path('TestFolder')
p.mkdir()


# In[20]:


ls


# ### Creating multiple Directories

# In[28]:


import os
os.makedirs('2019/July/11')


# In[29]:


ls


# In[59]:


pwd


# In[64]:


cd probsolvingprogramming


# In[66]:


import os
dirPath = 'git/'
for f_name in os.listdir(dirPath):
    if f_name.endswith('.ipynb'):
        print(f_name)


# ### Deleting  Files and Directories

# In[ ]:


import os
data_file ='file1.txt'  #Give the path c:\\Users
os.remove(data_file)


# In[68]:


data_dir = 'TestFolder'
os.rmdir(data_dir)


# In[ ]:


import shutil
data_dir = '2019'
shutil.rmtree(data_dir)


# ### Regular Expressions

# - Used to specific Pattern matching
# - Symbolic notations of Pattern
#           - Patterns(RE) represents set of the values
# - [0-9] 

# In[ ]:




