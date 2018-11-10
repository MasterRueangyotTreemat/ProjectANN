#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np


# In[36]:


url = 'https://github.com/prasertcbs/basic-dataset/raw/master/msleep.csv'
#df = pd.read_csv(url, nrows=10)
df = pd.read_csv(url) 
df


# In[13]:


df.shape


# In[19]:


np.iinfo(np.int32).max


# In[21]:


np.random.randint(np.iinfo(np.int32).min, np.iinfo(np.int32).max)


# In[22]:


np.random.randint(np.iinfo(np.int32).min, np.iinfo(np.int32).max, 5)


# In[37]:


df['uid'] = np.random.randint(np.iinfo(np.int32).min, np.iinfo(np.int32).max, df.shape[0])
df


# In[38]:


df.sort_values(['uid'],inplace=True)
df


# In[39]:


train_ratio = .7
df_train = df[:int(df.shape[0] * train_ratio)]
df_train


# In[42]:


df_train.shape


# In[43]:


df_test = df[int(df.shape[0] * train_ratio):]
df_test


# In[41]:


df_test.shape


# In[ ]:




