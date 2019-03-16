#!/usr/bin/env python
# coding: utf-8

# # 4.7_numpy_exercises.py
# ## Q's 1-7
# 
# #### Hackney, Chad
# #### 12 Mar 19

# In[ ]:





# In[2]:


# Exercises
# Create a file named 4.7_numpy_exercises.py for this exercise.

# Use the following code for the questions below:
#       a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


#  #  

# #### ** Setting up environment:

# In[6]:


import numpy as np
import math


# In[7]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
type(a)


# In[8]:


a


# #### 1. How many negative numbers are there?

# In[20]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
less_than_zero = a < 0
less_than_zero


# In[93]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a[a < 0]


# In[236]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
less_than_zero = a < 0
less_than_zero.sum()


# #### 2. How many positive numbers are there?

# In[19]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

greater_than_zero = a > 0
greater_than_zero


# In[25]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

a[a > 0]


# In[26]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

greater_than_zero = a > 0
greater_than_zero.sum()


# #### 3. How many EVEN and POSITIVE numbers are there?

# In[52]:


# array divisible by zero, ie "even number", AND is even number
## create a new array 'b', to preserve 'a' intact.
b = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

c = b[(b % 2) == 0]
c = c > 0
c.sum()


# #### 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[58]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

d = a + 3
d = d > 0
d.sum()


# #### 5. If you squared each number, what would the new mean and standard deviation be?

# In[66]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

e = a ** 2  # when printing out just 'e', this works so far to square each... now get the mean and std for 'e'
print(e)
print(e.mean())
print(e.std())


# #### 6.  A common statistical operation on a dataset is centering.  This means to adjust the data such that the center of the data is at 0.  This is done by subtracting the mean from each data point.  Center the data set.

# In[71]:


# This is the 'x' or "array of values", minus the mean of those values.

f = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
g = f.mean()
h = f - g
h


# #### 7.  Calculate the z-score for each data point. Recall that the z-score is given by: 
# Z = x−μ / σ

# In[76]:


# The problem above at #6 is literally the top half of this equation in #7.
# Now, simply divide #6 above, by the standard deviation of that array of data.

i = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
j = i.mean()
k = i.std()
l = (i - j) / k
l


# ## Setup 1:
# #### 8.  Copy the setup and exercise directions from More_Numpy_Practice  /missing weblink/   into your 4.7_numpy_exercises.py and add your solutions.
# #### ** Setting up environment:

# In[ ]:


import numpy as np
import math


# In[ ]:


## Setup 1
#  a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#  Use python's built in functionality/operators to determine the following:


# In[78]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
type(a)


# In[110]:


a


# #### 8.1.1  Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# In[80]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

sum_of_a = a.sum()
sum_of_a


# #### 8.1.2. Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# In[81]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

min_of_a = a.min()
min_of_a


# #### 8.1.3. Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
# 

# In[82]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

max_of_a = a.max()
max_of_a


# #### 8.1.4. Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# In[83]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mean_of_a = a.mean()
mean_of_a


# #### 8.1.5. Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# In[92]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

product_of_a = a.prod()
product_of_a


# #### 8.1.6. Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# In[91]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

squares_of_a = a ** 2
squares_of_a


# #### 8.1.7. Exercise 7 - Make a variable named odds_in_a.  It should hold only the odd numbers.

# In[98]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

odds_in_a = a[a % 2 == 1]
odds_in_a


# #### 8.1.8. Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# In[99]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

evens_in_a = a[a % 2 == 0]
evens_in_a


# ## Setup 2:
# 
# #### What about life in two dimensions?  A list of lists is matrix, a table, a spreadsheet, a chessboard...
# #### Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

# In[100]:


b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[108]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

type(b)


# In[111]:


b


# #### 8.2.1. # Exercise 1 - refactor the following to use numpy.  Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

# In[113]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)

sum_of_b = b.sum()
sum_of_b


# #### 8.2.2. Exercise 2 - refactor the following to use numpy. 

# In[114]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

min_of_b = b.min()
min_of_b


# #### 8.2.3. Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

# In[116]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
max_of_b


# #### 8.2.4. Exercise 4 - refactor the following using numpy to find the mean of b

# In[118]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

# mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))

mean_of_b = b.mean()
mean_of_b


# #### 8.2.5. Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

# In[120]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

product_of_b = b.prod()
product_of_b


# #### 8.2.6. Exercise 6 - refactor the following to use numpy to find the list of squares

# In[121]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

squares_of_b = b ** 2
squares_of_b


# #### 8.2.7. Exercise 7 - refactor using numpy to determine the odds_in_b

# In[123]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

odds_in_b = b[b % 2 == 1]
odds_in_b


# #### 8.2.8. Exercise 8 - refactor the following to use numpy to filter only the even numbers

# In[124]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
evens_in_b


# #### 8.2.9. Exercise 9 - print out the shape of the array b.

# In[128]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

b.shape


# #### 8.2.10. Exercise 10 - transpose the array b.

# In[130]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

b.transpose()


# #### 8.2.11. Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# In[131]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

b.reshape(1, 6)


# #### 8.2.12. Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

# In[132]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
]
)

b.reshape(6, 1)


# ## Setup 3
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.

# In[ ]:


c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# In[133]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
)
type(c)


# In[134]:


c


# #### 8.3.1 Exercise 1 - Find the min, max, sum, and product of c.

# In[140]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
)

min_of_c = c.min()
print(f'min_of_c: {min_of_c}')

max_of_c = c.max()
print(f'max_of_c: {max_of_c}')

sum_of_c = c.sum()
print(f'sum_of_c: {sum_of_c}')

product_of_c = c.prod()
print(f'product_of_c: {product_of_c}')


# #### 8.3.2. Exercise 2 - Determine the standard deviation of c.

# In[142]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
)

standard_deviation = c.std()
print(f'standard_deviation: {standard_deviation}')


# #### 8.3.3. Exercise 3 - Determine the variance of c.

# In[143]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
)

variance = c.var()
print(f'variance: {variance}')


# #### 8.3.4. Exercise 4 - Print out the shape of the array c

# In[144]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
)

c.shape


# #### 8.3.5. Exercise 5 - Transpose c and print out transposed result.

# In[162]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
)

transpose_c = c.transpose()
print(f'transpose_c:\n {transpose_c}')


# #### 8.3.6. Exercise 6 - Multiply c by the c-Transposed and print the result.

# In[164]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
)

c_by_t_posed_c = c * transpose_c
print(f'c_by_t_posed_c:\n {c_by_t_posed_c}')


# 
# #### 8.3.7. Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261.

# In[166]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
)

print(f'Sum of t_posed_c: {c_by_t_posed_c.sum()}')


# #### 8.3.8. Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

# In[178]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
)

prod_of_c = c.prod()
print(f'product of c: {prod_of_c}')

prod_of_c_t_pose = transpose_c.prod()
print(f'product of c-transposed: {prod_of_c_t_pose}')


prod_of_c_by_prod_of_c_t_pose = prod_of_c * prod_of_c_t_pose
print(f'product of c, multiplied the product of c-transposed: {prod_of_c_by_prod_of_c_t_pose}')
print('... so, transposing an array does not affect its product.')


# ## Setup 4:

# In[ ]:


d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]


# In[179]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)
type(d)


# In[180]:


d


# #### 8.4.1. Exercise 1 - Find the sine of all the numbers in d.

# In[185]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

np.sin(d)


# #### 8.4.2. Exercise 2 - Find the cosine of all the numbers in d

# In[186]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

np.cos(d)


# #### 8.4.3. Exercise 3 - Find the tangent of all the numbers in d

# In[187]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

np.tan(d)


# #### 8.4.4. Exercise 4 - Find all the negative numbers in d

# In[191]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

neg_nos_in_d = d[d < 0]
print(neg_nos_in_d)


# #### 8.4.5. Exercise 5 - Find all the positive numbers in d

# In[198]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

pos_nos_in_d = d[d > 0]
print(pos_nos_in_d)


# #### 8.4.6 Exercise 6 - Return an array of only the unique numbers in d.

# In[203]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

np.unique(d)


# #### 8.4.7. Exercise 7 - Determine how many unique numbers there are in d.

# In[218]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

np.unique(d).shape[0]


# #### 8.4.8 Exercise 8 - Print out the shape of d.

# In[225]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

d.shape


# #### 8.4.9 Exercise 9 - Transpose and then print out the shape of d.

# In[230]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

# immediately below works, but the latter one below is prefered, like numpy shorthand
# d_t_pose = d.transpose()
# d_t_pose.shape

# preferred code:
np.transpose(d).shape


# #### 8.4.10 Exercise 10 - Reshape d into an array of 9 x 2

# In[231]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

d.reshape(9, 2)


# #### end of 4.7_numpy_exercises

print('monkey')
