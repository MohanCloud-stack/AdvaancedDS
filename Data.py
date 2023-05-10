import numpy as np
#to check the data type of the array
arr=np.array([12,13,14,15])
print(arr.dtype)
#to create the array with defined data type 
arr=np.array([1,2,3,4,5],dtype='S')
print(arr)
# to create the array with data type 4 bytes integer
arr=np.array([1,2,3,4],dtype='i4')
print(arr)
print(arr.dtype)
#to covert the data type of an existing array
arr=np.array([1.1,2.2,3.3,4.4])
newarr=arr.astype('i')
print(newarr)
arr1=np.array([1,0,3])
newarr=arr1.astype(bool)
print(newarr)
