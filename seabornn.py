#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd


# In[2]:


df = sns.load_dataset('tips') 


# In[4]:


df.head(25)


# In[28]:


df


# In[29]:


df.corr()


# In[5]:


sns.heatmap(df.corr())


# In[10]:


sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')


# In[38]:


sns.pairplot(df)


# In[11]:


sns.pairplot(df,hue='smoker')


# In[40]:


sns.distplot(df['tip'])


# In[12]:


sns.countplot('smoker',data=df)


# In[43]:


sns.barplot(x='total_bill',y='sex',data=df)


# In[46]:


sns.boxplot('sex','total_bill',data=df)


# In[ ]:




