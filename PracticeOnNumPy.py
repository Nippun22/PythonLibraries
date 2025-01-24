#Q1: Write a Python program to create a 3*3 NumPy array with random integers between 1 and 50
#Q2: Given a 1D NumPy array, write a function to calculate the mean, median and standard deviation
#Q3: WAP to reshape a given array of shape (6,) into a 2*3 matrix
#Q4: Create a NumPy array containing the squares of numbers from 1 to 10
#Q5: WAP to find the unique elements in a given NumPy array and their counts.
#Q1
import numpy as np
ranArray= np.random.randint(1,51,size=(3,3))
print(ranArray)
#Q3
L=[1,2,3,4,5,6]
arr=np.array(L)
arr=arr.reshape(2,3)
print(arr)
#Q4
arr1=np.array([x**2 for x in range(1,11)])
print(arr1)
#Q5
arr1=np.array([1,2,3,44,5,5,6,6,7])
arr1, counts=np.unique(arr1, return_counts=True)

print(arr1)
print(counts)
