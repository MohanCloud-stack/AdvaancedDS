import numpy as np 
a=np.arange(1,10)
print(a)
#advanced indexing
#create an array of index
index=np.array([1,4,5])
#use the index array as index
print(a[index])

# for 2-d/Multi dimensional Array
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b[[0,2],[2,0]])
#        row and column
print(b[[1,1,2],[0,2,1]])
#Boolean Indexing
c=np.array([[1,-2,3],[4,-2,3]])
print(c[c<0])
print(c[c>0])
#multiply all the -ve values by 2
print(c[c<0]*2)