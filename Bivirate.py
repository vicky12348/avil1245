#!/usr/bin/env python
# coding: utf-8

# # Bivariate Data: Examples, Definition and Analysis

# #In statistics, many bivariate data examples can be given to help you understand the relationship between two variables and to grasp the idea behind the bivariate data analysis definition and meaning.

# What is bivariate ?
# We have bivariate data when we studying two variables. These variables are changing and are compared to find the relationships between them.

# For example, if you are studying a group of students to find out their average math score and their age, you have two variables (math score and age).

# In[ ]:


Look at the following bivariate data table. It represents the age and average height of a group of babies and kids.


# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


data = [['3 months', 7], ['6 months', 8], ['9 months', 9],['1 Years', 10], ['2 Years', 11], ['3 Years', 12],['4 Years', 13], ['5 Years', 14]] 


# In[7]:


df = pd.DataFrame(data, columns = ['Age', 'Height in Cms']) 


# In[8]:


df


# There are 2 types of relationship between the dependent and independent variable:
# 
# A positive relationship (also called positive correlation) – that means if the independent variable increases, then the dependent variable would also increase and vice versa. The above example about the kids’ age and height is a classical positive relationship.
# A negative relationship (negative correlation) – when the independent variable increases and the dependent variable decrease and vice versa. Example: when the car age increases, the car price decreases.
# So, we use bivariate data to compare two sets of data and to discover any relationships between them.
# 
# Bivariate Data Analysis

# In[9]:


plt.scatter(df['Age'], df["Height in Cms"])


# In[10]:


df1=pd.read_csv('D:\E-drvebkp\Covid\state_level_latest.csv')


# In[11]:


df1.head()


# In[13]:


df1.columns


# In[16]:


plt.scatter(df1['Recovered'], df1["Deaths"])


# In[20]:


data1 = [['3 months', 10], ['6 months', 8], ['9 months', 7],['1 Years', 6], ['2 Years', 6], ['3 Years', 4],['4 Years', 3], ['5 Years', 2]] 


# In[21]:


df2 = pd.DataFrame(data1, columns = ['tenure', 'ROI']) 


# In[22]:


df2


# In[24]:


plt.scatter(df2['tenure'], df2["ROI"])


# In[ ]:




