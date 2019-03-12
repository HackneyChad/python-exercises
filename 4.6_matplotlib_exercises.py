#!/usr/bin/env python
# coding: utf-8

# # 4.6_matplotlib_exercises.py
# ## Q's 1-5

# #### 4.6_matplotlib_exercises.py
# #### Hackney, Chad
# #### 11 Mar 19

# In[ ]:


# 1. Write the Python code necessary to write your name with matplotlib lines.
## skipped per instruction.


# In[ ]:


# import libs
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math


# In[2]:


print(plt)


# #### 2. Use matplotlib to plot the following equation:  y = x^2 − x + 2

# In[15]:


x = list(range(1, 50))
y = [((n ** 2) - n + 2) for n in x]
plt.plot(x, y, c='red')

plt.annotate('Origin', xy=(0, 0), xytext=(5, 500),
            arrowprops={'facecolor': 'blue'})
plt.show()

# Add an anotation for the point 0, 0, the origin.


# #### 3. Create and label 4 separate plots for the following equations (choose a range for x that makes sense):

# In[28]:


# 3.a. Plot for:  y = √x

x = list(range(1, 50))
y = [(math.sqrt(n)) for n in x]

plt.plot(x, y, c='orange')
plt.title("Plot for y = √x")
plt.xlabel('x')
plt.ylabel('y')

plt.annotate('Origin', xy=(0, 1), xytext=(10, 1.5),
             arrowprops={'facecolor': 'blue'})
plt.show()


# In[30]:


# 3.b. Plot for:  y = x^3

x = list(range(1, 50))
y = [(n ** 3) for n in x]

plt.plot(x, y, c='yellow')
plt.title("Plot for y = x^3")
plt.xlabel('x')
plt.ylabel('y')

plt.annotate('Origin', xy=(0, 0), xytext=(5, 20000),
             arrowprops={'facecolor': 'blue'})
plt.show()


# In[52]:


# 3.c. Plot for:  y = tan(x)

x = list(range(1, 50))
y = [(math.tan(n)) for n in x]

plt.plot(x, y, c='green')
plt.title("Plot for y = tan(x)")
plt.xlabel('x')
plt.ylabel('y')

plt.annotate('Origin', xy=(0, 0), xytext=(5, -75),
             arrowprops={'facecolor': 'blue'})
plt.show()


# In[49]:


# 3.d. Plot for:  y = 2^x

x = list(range(1, 50))
y = [(2 ** n) for n in x]

plt.plot(x, y, c='blue')
plt.title("Plot for y = 2^x")
plt.xlabel('x')
plt.ylabel('y')

plt.annotate('Origin', xy=(0, 0), xytext=(10, 10),
             arrowprops={'facecolor': 'red'})
plt.show()


# #### 4. Combine the figures you created in the last step into one large figure with 4 subplots.

# In[53]:


plt.figure(figsize=(12, 8))

x = list(range(1, 50))
y = [(math.sqrt(n)) for n in x]
z = [(n ** 3) for n in x]
a = [(math.tan(n)) for n in x]
b = [(2 ** n) for n in x]

# the first subplot
plt.subplot(221)
plt.plot(x, y)
plt.title('x ~ y')

# the second subplot
plt.subplot(222)
plt.plot(x, z)
plt.title('x ~ z')

# the third subplot
plt.subplot(223)
plt.plot(x, a)
plt.title('x ~ a')

# the fourth subplot
plt.subplot(224)
plt.plot(x, b)
plt.title('x ~ f')

plt.suptitle('Q4. - Subplots derived from Q3.')
plt.show()


# #### 5. Combine the figures you created in the last step into one figure where each of the 4 equations has a different color for the points.  Be sure to include a legend.

# In[73]:


x = list(range(1, 50))
y = [(math.sqrt(n)) for n in x]
z = [(n ** 3) for n in x]
a = [(math.tan(n)) for n in x]
b = [(2 ** n) for n in x]

plt.plot(x, y, c='red')
plt.plot(x, z, c='orange')
plt.xscale('linear') # the default
plt.yscale('log')
plt.plot(x, a, c='yellow')
plt.plot(x, b, c='green')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.zlabel('z')
# plt.alabel('a')
# plt.blabel('b')
plt.legend()
plt.show()


# In[ ]:




