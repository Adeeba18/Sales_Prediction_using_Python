#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


df=pd.read_csv("train.csv")
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()*100/len(df)


# In[8]:


df.isnull().sum()


# In[9]:


df['Postal Code'] = df['Postal Code'].fillna(0)
df


# In[10]:


df.info()


# 
# # Segment for values available

# In[11]:


seg=pd.DataFrame(df['Segment'].value_counts())
seg


# In[12]:


sns.barplot(seg, x=seg.index, y="Segment")


# # 10 state of us giving maximum sales count

# In[14]:


state=pd.DataFrame(df['State'].value_counts())[0:10]
state


# In[15]:


sns.barplot(state , y= state.index , x = 'State')


# # 10 Cities that give maximum sales count

# In[16]:


city=pd.DataFrame(df['City'].value_counts())[0:10]
city


# In[17]:


sns.barplot(city,y=city.index,x="City")


# # Region of USA gives maximum count

# In[18]:


region=pd.DataFrame(df['Region'].value_counts())
region


# In[19]:


sns.barplot(region,x=region.index,y='Region')


# # what kind of product they Are selling and their quantity through USA

# In[20]:


category=pd.DataFrame(df['Category'].value_counts())
category


# In[21]:


sns.barplot(category,x=category.index,y='Category')


# # Under Furniture supplies what kind of product they are selling

# In[22]:


fr_data = df[df['Category'] == 'Furniture']
fr_data = pd.DataFrame(fr_data['Sub-Category'].value_counts())
fr_data
sns.barplot(fr_data, y = fr_data.index , x = 'Sub-Category')


# # Under Technology what kind of product they are selling

# In[24]:


tc_data = df[df['Category'] == 'Technology']
tc_data = pd.DataFrame(tc_data['Sub-Category'].value_counts())
sns.barplot(tc_data, y = tc_data.index , x = 'Sub-Category')


# # Under Office what kind of product they are selling

# In[25]:


oc_data = df[df['Category'] == 'Office Supplies']
oc_data = pd.DataFrame(oc_data['Sub-Category'].value_counts())
sns.barplot(oc_data,y = oc_data.index,x = 'Sub-Category')



# # what is the companies preffrred mode of shipping

# In[26]:


ship_data=pd.DataFrame(df['Ship Mode'].value_counts())
ship_data
sns.barplot(ship_data,y='Ship Mode',x=ship_data.index)


# # what is the average shipping cost per ship mode

# In[27]:


sms_data = pd.DataFrame(df.groupby('Ship Mode')['Sales'].mean())
sms_data


# In[28]:


sms_data = sms_data.sort_values(by = 'Sales')
sns.barplot(sms_data , y = sms_data.index , x = 'Sales')


# # Top 10 highest buyer in their 4 years journey

# In[31]:


top10=pd.DataFrame(df['Customer Name'].value_counts())[0:10]
top10
sns.barplot(top10, y = top10.index , x = 'Customer Name')


# # Top 10 city, state and region gives maximum sales

# In[32]:


max_city = pd.DataFrame(df.groupby('City')['Sales'].mean().sort_values(ascending = False))[0:10]
max_city


# In[33]:


max_state = pd.DataFrame(df.groupby('State')['Sales'].mean().sort_values(ascending = False))[0:10]
max_state


# In[34]:


max_zone = pd.DataFrame(df.groupby('Region')['Sales'].mean().sort_values(ascending = False))
max_zone

