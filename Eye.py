import numpy as np
print(np.eye(5))
print(np.eye(2,3))
print(np.eye(4,3,1))#upper part of main diagonal
print(np.eye(4,k=-1))
# for the specific data type
print(np.eye(5,dtype=int))
print(np.identity(4,dtype=int))