#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# <h3> 1. Data Collection </h3>

# In[2]:


data = pd.read_csv("/Users/dobaophuc/Downloads/world_internet_user.csv", encoding="latin1")


# <h3> 2. Data Cleaning </h3>

# In[3]:


data.info


# In[4]:


data.duplicated().any() #check if any data is duplicated


# In[5]:


data.isnull().values.any() #check if any values are null


# In[6]:


data.isnull().sum() #The data "World" does not have Region value.


# In[7]:


data.fillna(0) #fill missing value with number 0


# <h3> 3. Data preprocessing</h3>

# In[8]:


data['Region'].value_counts()


# In[9]:


data['Region'].value_counts().plot(kind="bar")
plt.title('Country Counts')
plt.xlabel('Region')
plt.ylabel('Count')


# In[10]:


Region = ('Africa','America','Europe','Asia','Oceania','Middle East')
counts = (58,55,53,35,27,14)
colors = ('#ADD8E6','#E3CF57','#FFF5EE', '#FFD51F', '#E67F0D', '#D53032')
plt.pie(
counts,
labels = Region,
colors= colors,
autopct = '%1.1f%%',
shadow = True)
plt.show()


# In[11]:


#Country with most Internet User Percentage
data.rename(columns ={'Internet Users':'Internet_Users', '% of Population':'IU_Percentage'}, inplace = True)
data.head()


# <h3>4. Data Analysis and Visualization</h3>
# <h4> Bar graph of IU percentage avarage by regions</h4>

# In[12]:


data.Region[data.Country == '_World'] = 'World'
data.head()


# In[13]:


IURegion = pd.pivot_table(data,values = ['Population','Internet_Users','IU_Percentage'], index='Region', aggfunc= 'mean')
IURegion.sort_values(by = 'IU_Percentage', ascending = True)
IURegion


# In[14]:


IURegion['IU_Percentage'].plot(kind = 'bar')
plt.title('Internet User Percentage by Regions')
plt.xlabel('Region')
plt.ylabel('Percentage')
plt.show()


# <h4> Boxplots of Internet User Distribution by Regions </h4>

# In[15]:


d = data.drop(0)


# In[16]:


b1 = ['IU_Percentage']

boxplot = d.boxplot(b1)  
plt.xticks(rotation=90)
plt.title("World's IU Distribution")
plt.show()


# In[17]:


boxplot = d[d['Region'] == 'Asia'].boxplot(b1)  
plt.xticks(rotation=90)
plt.title("Asia IU Distribution")
plt.show()


# <p> * The IU percentage in Asia nearly resembles that of the world's figure</p>

# In[18]:


boxplot = d[d['Region'] == 'Africa'].boxplot(b1)  
plt.xticks(rotation=90)
plt.title("Africa IU Distribution")
plt.show()


# <p> * The IU percentage in Africa is still far below the world's level, with <strong>more than 75%</strong> countries having less than <strong>60%</strong> of population using the Internet</p>

# In[19]:


boxplot = d[d['Region'] == 'America'].boxplot(b1)  
plt.xticks(rotation=90)
plt.title("America IU Distribution")
plt.show()


# In[20]:


boxplot = d[d['Region'] == 'Oceania'].boxplot(b1)  
plt.xticks(rotation=90)
plt.title("Oceania IU Distribution")
plt.show()


# In[21]:


boxplot = d[d['Region'] == 'Europe'].boxplot(b1)  
plt.xticks(rotation=90)
plt.title("Europe IU Distribution")
plt.show()


# In[22]:


boxplot = d[d['Region'] == 'Middle East'].boxplot(b1)  
plt.xticks(rotation=90)
plt.title("Middle East IU Distribution")
plt.show()


# <h4> What is the country with the least Internet User Percentage? </h4>

# In[23]:


maxUI = d.sort_values('IU_Percentage', ascending = True)
maxUI.head()


# <p> - North Korea is the only Asian country in top 5 countries with the least Internet User Percentage, along with other 4 African countries. </p>
# <p> - More than <strong>99.9 percent</strong> of the country's population remained offline at the start of 2022. </p>
# <p> - According to <em>"Digital 2022: North Korea"</em> report from <strong>datareportal.com</strong>, only a few people in the country are able to access international websites, and it seems likely that a sizeable proportion of this small group will be made up of foreign expatriates and the country's political elite </p>

# <h4> What is the country with the most Internet User Percentage? </h4>

# In[24]:


maxUI.tail()


# In[25]:


data


# <h3>Thank you for watching!</h3>

# In[ ]:




