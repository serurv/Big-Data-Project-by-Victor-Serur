#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This is a program that integrates SQL functionality into Python. This is following a lesson from Introduction to Python for Computer Science and 
# Data Science 

# Author: Victor Serur


# In[1]:


# We import all libraries involving pandas and sql 


# In[2]:


import sqlite3


# In[3]:


connection = sqlite3.connect('ch17/books.db')


# In[4]:


import pandas as pd


# In[5]:


# Displays max column number of ten 


# In[6]:


pd.options.display.max_columns = 10


# In[7]:


# Displays all authors 


# In[8]:


pd.read_sql('SELECT * FROM authors', connection, index_col = ['id'])


# In[9]:


# Displays all titles, editions, and copyright 


# In[10]:


pd.read_sql('SELECT * FROM titles', connection)


# In[11]:


# Creates dataframe variable 


# In[12]:


df = pd.read_sql('SELECT * FROM author_ISBN', connection)


# In[13]:


df.head() 


# In[14]:


# Selects first and last name from authors 


# In[15]:


pd.read_sql('SELECT first, last FROM authors', connection)


# In[16]:


# Displays information for titles 


# In[17]:


pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection)


# In[18]:


# Displays authors by specific information 


# In[19]:


pd.read_sql("""SELECT id, first, last FROM authors WHERE last LIKE 'D%'""", connection, index_col = ['id'])


# In[20]:


pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", connection, index_col = ['id'])


# In[21]:


# Displays titles by ascending order 


# In[22]:


pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)


# In[23]:


# Displays author by first and last names in varying order 


# In[24]:


pd.read_sql("""SELECT id, first, last FROM authors ORDER by last, first""", connection, index_col = ['id'])


# In[25]:


# Displays descending, then ascending order of authors 


# In[26]:


pd.read_sql("""SELECT id, first, last FROM authors ORDER by last DESC, first ASC""", connection, index_col = ['id'])


# In[27]:


# Displays detailed information about titles 


# In[28]:


pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to program' ORDER BY title""", connection)


# In[29]:


pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first""", connection).head()


# In[30]:


# Creates cursor variable and creates new author 


# In[31]:


cursor = connection.cursor()


# In[32]:


cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")


# In[33]:


pd.read_sql('SELECT id, first, last FROM authors ', connection, index_col = ['id'])


# In[34]:


cursor = cursor.execute("""UPDATE authors SET last = 'Black' WHERE last = 'Red' AND first = 'Sue'""")


# In[35]:


pd.read_sql('SELECT id, first, last FROM authors ', connection, index_col = ['id'])


# In[36]:


# Deletes author column where we created a new author 


# In[37]:


cursor = cursor.execute('DELETE FROM authors WHERE id = 6')


# In[38]:


cursor.rowcount


# In[39]:


pd.read_sql('SELECT id, first, last FROM authors ', connection, index_col = ['id'])


# In[40]:


# Displays titles by edition in descending order 


# In[41]:


pd.read_sql("""SELECT title, edition FROM titles ORDER BY edition DESC""", connection).head(3)


# In[42]:


# Displays authors with first name starts with an 'A'


# In[43]:


pd.read_sql("""SELECT * FROM authors WHERE first LIKE 'A%'""", connection)


# In[44]:


pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title NOT LIKE '%How to Program' ORDER BY title""", connection)


# In[45]:


# This is part 2 of the program. It is based on lesson 17.1 in the textbook. 


# In[46]:


# This is part a, it slects all authors last names from the authors table in descending order 


# In[47]:


pd.read_sql("""SELECT id, last FROM authors ORDER by id DESC""", connection, index_col = ['id'])


# In[48]:


# This is part b, it slects all book titles from the titles table in ascending order 


# In[49]:


pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)


# In[ ]:


# This is part c, we use inner join to select all the books for a specific author and order the information  


# In[130]:


pd.read_sql("""SELECT first, last, isbn, copyright, title 
FROM authors 
INNER JOIN titles WHERE first LIKE '%Paul'
ORDER BY title ASC""", connection)


# In[50]:


# This is part d, we insert a new author into the authors table. 


# In[51]:


cursor.execute("""INSERT INTO authors (first, last) VALUES ('John', 'Smith')""")


# In[52]:


pd.read_sql('SELECT id, first, last FROM authors ', connection, index_col = ['id'])


# In[53]:


# This is part e, we insert a new title for an author and ISBN 


# In[72]:


cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES ('8', 'Test')""")


# In[73]:


pd.read_sql('SELECT * FROM author_ISBN', connection)


# In[74]:


pd.read_sql('SELECT title FROM titles', connection)


# In[116]:


cursor.execute("""INSERT INTO titles VALUES ('Test', 'Test', 'test', 'test')""")


# In[117]:


pd.read_sql('SELECT * FROM titles', connection)

