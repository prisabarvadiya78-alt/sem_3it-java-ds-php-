import sys
import numpy as np
#uniersal function
arr=np.array([1,5,9,16])
print("sqrt:",np.sqrt(arr))
print("square:",np.square(arr))
print("sin:",np.sin(arr))
print("cos:",np.cos(arr))

#aggregate function
arr1=np.array([1,5,9,16])
print("sum:",np.sum(arr1))
print("mean:",np.mean(arr1))
print("max:",np.max(arr1))
print("min:",np.min(arr1))
print("std:",np.std(arr1))


#array sorting
print("sort:",np.sort(arr1))


#boolean indexing
arr2=np.array([5,10,15,20,25])
print("boolean:",arr2[arr2>15])

#array indexing
arr3=np.array([[1,2,3],[4,5,6]])
print(arr3[0,1])
print(arr3[1,2])

# array slicing
print(arr3[1:4])


#one dimensional array indexing
arr4=np.array([10,20,30,40,50])
print(arr4[0])
print(arr4[2])
print(arr4[-1])

#array properties
arr5=np.array([[1,2,3],[4,5,6]])
print(arr5.ndim)
print(arr5.shape)
print(arr5.size)
print(arr5.dtype)

#one-dimensional array
arr6=np.array([10,20,30,40])
print(arr6)

#two-dimensional array
arr7=np.array([[1,2,3],[4,5,6]])
print(arr7)
