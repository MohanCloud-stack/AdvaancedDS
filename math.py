#this is a one Dimensional array
import numpy as np
arr1=np.array([12,13,14,15])
print(arr1)
for i in range(len(arr1)):
    if arr1[i]%2 == 0:
        print(arr1[i])
# 2-D array
import numpy as np
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
# 3-D array
import numpy as np
arr3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3)
#checking the dimenisions that each array can have
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)