#import numpy
'''
import numpy as np
import sys
#print(len(dir(np)))
list1 = [1, 2, 3, 4]
print(list1)
print(type(list1))
print(sys.getsizeof(list1))

arr1 = np.array([1, 2, 3, 4])
print(arr1)
print(type(arr1))
print("array", sys.getsizeof(arr1))
'''



#attriutes of 1-D Array
'''
import numpy as np
import sys
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(arr1.dtype)   #data type of each element
print(arr1.ndim)   #number of dimension
print(arr1.itemsize)   #size of each item in bytes
print(arr1.nbytes)   #size of whole array in bytes
print(arr1.size)   #number of elements
print(arr1.shape)   #order of array
'''



#attriutes of 2-D Array
'''
import numpy as np
import sys
arr1 = np.array([[1,2,3,4], [5,6,7,8]])
print(arr1)
print(arr1.dtype)   #data type of each element
print(arr1.ndim)   #number of dimension
print(arr1.itemsize)   #size of each item in bytes
print(arr1.nbytes)   #size of whole array in bytes
print(arr1.size)   #number of elements
print(arr1.shape)   #order of array
'''




#attriutes of 3-D Array
'''
import numpy as np
import sys
arr1 = np.array([[[1,2,3], [4,5,6], [9,8,6]], [[4,6,8], [2,4,6], [1,7,8]]])
print(arr1)
print(arr1.dtype)   #data type of each element
print(arr1.ndim)   #number of dimension
print(arr1.itemsize)   #size of each item in bytes
print(arr1.nbytes)   #size of whole array in bytes
print(arr1.size)   #number of elements
print(arr1.shape)   #order of array
'''



#creating array with arange()
'''
import numpy as np
arr = np.arange(7)
print(arr)
arr1 = np.arange(4,12)
print(arr1)
arr2 = np.arange(2,15,3)
print(arr2)
arr3 = np.arange(10,1,-2)
print(arr3)
'''



#using reshape
'''
import numpy as np
arr1 = np.arange(12).reshape(3,4)
print(arr1)
#arr2 = arr1.reshape(3,4)
#print(arr2)
arr2 = np.arange(48)
arr3 = arr2.reshape((3,4,4))
print(arr3)
arr4 = np.reshape(arr3, (3,4,4))
print(arr4)
'''


#resize
'''
import numpy as np
ar1 = np.arange(12)
print(ar1)
ar1.resize(3,4)
print(ar1)
'''


#zeros()  #creates array with zero value
'''
import numpy as np
ar2 =  np.zeros((3,5))
print(ar2)
'''


#empty()   #creates array with random value
'''
import numpy as np
ar3 = np.empty((2,4))
print(ar3)
'''


#ones()   #creates value with value 1
'''
import numpy as np
ar4 = np.ones((3,4))
print(ar4)
'''


#identity()   #creates identity matrix
'''
import numpy as np
ar5 = np.identity(5)
print(ar5)
'''


#linspace()   #creates value between numbers dividing in equal parts
'''
import numpy as np
ar6 = np.linspace(1,5,6)
print(ar6)
ar7 = np.linspace(0,2*np.pi, 100)
print(ar7)
'''


#empty_like   #creates replica
'''
import numpy as np
a = np.arange(12)
print(a)
b = np.empty_like(a)   #b is the replica of a
print(b)
b[2] = 200
print(b)
print(a)
'''


#ravel()  #it makes changes in oringinal copy as well as the replica
'''
import numpy as np
a1 = np.arange(12).reshape(3,4)
print(a1)
a2 = np.ravel(a1)
print(a2)
a2[4] = 200
print(a2)
print(a1)
'''


#flatten    #does not change the original
'''
import numpy as np
a1 = np.arange(12).reshape(3,4)
print(a1)
a2 = a1.flatten()
print(a2)
a2[4] = 200
print(a2)
print(a1)
'''


#flat attribute   #it returns the flat iterator
'''
import numpy as np
a3 = np.arange(12).reshape(3,4)
print(a3)
for i in a3.flat:
    print(i)
'''


#diag()   #adds elements to diagonal position
'''
import numpy as np
a4 = np.diag([2,3,4,1])
print(a4)
'''


#random function   #gives random values between 0 and 1
'''
import numpy as np
x=np.random.default_rng()
a5 = x.random((3,4))
print(a5)

a6 = np.random.randint(2,10, size = (3,5,2))
print(a6)
'''


#joining--
# hstack()
# vstack()
'''
import numpy as np
a7 = np.arange(6,12).reshape(2,3)
print(a7)
a8 = np.arange(8).reshape(2,4)
print(a8)
a9 = np.hstack([a7,a8])
print(a9)

a7 = np.arange(6,12).reshape(3,2)
print(a7)
a8 = np.arange(4).reshape(2,2)
print(a8)
a9 = np.vstack([a7,a8])
print(a9)
'''


#operations in arrays
#sum(), max, min, sory, argmax, argmin, argsort, mean, std, var
'''
import numpy as np
arr1 = np.array([1,3,6,8,2,4,9])
print(arr1)  #array
print(arr1.sum())  #sum
print(arr1.max())  #max value
print(arr1.min())  #min value
sort_arr = np.sort(arr1)  #sort in ascending order
print(sort_arr)  #arr1.sort() modifies the original array 
print(arr1.argmax())  #index value of largest number
print(arr1.argmin())  #index value of smallest number
print(arr1.argsort())  #index value of sorted numbers
print(arr1.mean())  #mean
print(arr1.std())  #standard deviation
print(arr1.var())  #variance
'''


#use of axis
'''
import numpy as np
a1 = np.arange(12).reshape(3,4)
print(a1)
print(a1.max())
print(a1.max(axis=0))   #column wise 
print(a1.max(axis=1))   #row wise
'''


#arithmetic operations
'''
import numpy as np
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a2)
print(a2+5)
print(a2-3)
print(a2*3)
print(a2/2)
print(a2//2)
print(a2%3)
print(a2**2)
#transpose
print(a2.T)
a3 = np.array([[4,5,9],[1,3,7],[7,4,6]])
a4 = np.array([[6,4,2],[1,4,7],[8,2,9]])
print(a3)
print(a4)
print(np.add(a3,a4))
print(a3+a4)
print(a3-a4)
print(np.subtract(a3,a4))
print(a3*a4)   #multiplication
print(np.multiply(a3,a4))   #multiplication
print(np.dot(a3,a4))   #multiplication
print(a3@a4)   #multiplication
'''


#condition
'''
import numpy as np
a1 = np.array([[-2,3,-4], [9,0,-7],[-3,2,4]])
print(a1)
print(np.where((a1>0),2*a1, a1**2))    #(condition),operation if true, operation if false
'''


#file operations

import numpy as np
a1 = np.arange(20).reshape(4,5)
print(a1)
#np.savetxt(r"cse.txt", a1)  #store the file
print(np.loadtxt(r"cse.txt"))  #load file











