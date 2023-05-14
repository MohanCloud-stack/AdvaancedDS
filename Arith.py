import numpy as np
a=np.arange(1,5)
print(a)
print(a+2)
print(a**2)
print(a%2)
#for 2-d array
c=np.array([[1,2],[3,4]])
print(c+2)
#add 1-d and 2-d 
e=np.arange(1,5)
f=np.array([10,20,30,40])
print(e+f)
g=np.array([[1,2,3],[4,5,6]])
h=np.array([[1,2,1],[2,1,1]])
print(g+h)
print(g%h)
print(g-h)
#inbuilt function
print(np.add(g,h))