#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[24]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
plt.rcParams["figure.figsize"]=20,20


# In[3]:


df=pd.read_csv('D:\E-drvebkp\Covid\state_level_latest.csv')


# In[4]:


df.head()


# In[5]:


df.columns


# In[11]:


plt.pie(df['Recovered'],labels=df['State_code'],autopct='%1.1f%%')
plt.show()


# In[13]:


plt.hist(df['Confirmed'],label=df['State'])


# In[16]:


plt.plot(df['State_code'],df['Confirmed'],'g-',linestyle='dotted')


# In[17]:


sns.heatmap(df.corr())


# In[18]:


sns.pairplot(df,hue='State_code')


# In[43]:


df.columns


# In[25]:


plt.subplot(2,2,1)
plt.plot(df['State_code'],df['Confirmed'],'r')
plt.subplot(2,2,2)
plt.plot(df['State_code'],df['Deaths'],'b')
plt.subplot(2,2,3)
plt.plot(df['State_code'],df['Active'],'g')


# In[30]:


plt.savefig('C:\\Users\\LENOVO\\Documents\\viv.png',dpi=500)


# In[ ]:




