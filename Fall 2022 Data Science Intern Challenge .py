#!/usr/bin/env python
# coding: utf-8

# # Fall 2022 Data Science Intern Challenge 
# 
# #### Darren Ho

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# ## Question 1
# 
# Given some sample data, write a program to answer the following: [click here to access the required data set](https://docs.google.com/spreadsheets/d/16i38oonuX1y1g7C_UAmiK9GkY7cS-64DfiDMNiR41LM/edit#gid=0)
# 
# On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 
# 
# - Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 
# - What metric would you report for this dataset?
# - What is its value?

# In[2]:


df = pd.read_csv('2019 Winter Data Science Intern Challenge Data Set.csv')
df


# In[3]:


df.info()


# In[4]:


# descriptive stats of int type columns

df.select_dtypes(include=['int']).describe()


# In[5]:


df['order_amount'].describe()


# In[6]:


df['order_amount'].hist()
plt.show()


# In[7]:


sns.boxplot(x=df['order_amount'])


# In[8]:


print('Naively Calculated AOV: $',sum(df['order_amount']) / len(df['order_amount']))


# ## Question 1a 
# - Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.
# 
# Answering the first bullet point, we see that the "naively calculated AOV" of $3145.13 is actually the average amount per unique order, or the mean of the `order_amount` column. This column may not be the best way to evaluate this data because it is heavily skewed. 
# 
# The proper way of calculating the AOV (Average Order Value) is to divide revenue by number of orders, so lets explore that.   

# In[9]:


# Calculating AOV

aov = sum(df['order_amount']) / sum(df['total_items'])
print('Average Order Value: $',round(aov,2))


# We find that the `AOV` value should be \\$357.92. This value tells us that, on average, a customer spends \\$357.92 per order. Although we have greatly reduced the `AOV` value, it still seems to be a bit high in terms of what an average customer would spend per order.
# 
# Let's take a look at the median value of `order_amount` since medians are more resistant to outliers than means are. 

# In[10]:


# Median 

median = df['order_amount'].median()
print('Median Order Amount: $', median)


# ## Question 1b
# - What metric would you report for this dataset?
# 
# For this dataset, I would report the median of `order_amount` as the median is more resistant against outliers as our data is heavily skewed.

# ## Question 1c
# - What is its value?
# 
# The value of the median is $284.

# ## Question 2
# 
# For this question you’ll need to use SQL. Follow this [link](https://www.w3schools.com/SQL/TRYSQL.ASP?FILENAME=TRYSQL_SELECT_ALL) to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.

# ## How many orders were shipped by Speedy Express in total?
# 
# SELECT COUNT(*) <br>
#   FROM Orders o <br>
#  INNER JOIN Shippers s ON o.ShipperID = s.ShipperID <br>
#  WHERE s.ShipperName = 'Speedy Express'
#  
# ### Answer: 54

# ## What is the last name of the employee with the most orders?
# 
# SELECT e.LastName, COUNT(*) AS Num_Orders <br>
#   FROM Employees e <br>
#  INNER Join Orders o ON o.EmployeeID = e.EmployeeID <br>
#  GROUP BY LastName <br>
#  ORDER BY Num_Orders DESC
#  
# ### Answer: Peacock, 40 orders

# ## What product was ordered the most by customers in Germany?
# 
# SELECT ProductName, SUM(Quantity) AS Total_Sold <br>
#   FROM Customers c <br>
#  INNER JOIN Orders o ON o.CustomerID = c.CustomerID <br>
#  INNER JOIN OrderDetails od ON od.OrderID = o.OrderID <br>
#  INNER JOIN Products p ON p.ProductID = od.ProductID <br>
#  WHERE Country = 'Germany' <br> 
#  GROUP BY ProductName <br>
#  ORDER BY Total_Sold DESC <br>
#  LIMIT 1
#  
# ### Answer: Boston Crab Meat
