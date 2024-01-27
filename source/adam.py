# importing libraries
import numpy as np
import matplotlib.pyplot as plt

# creating the input array
X=np.array([[1,0,1,0], [1,0,1,1], [0,1,0,1]])

# converting the input in matrix form
X = X.T
print ('\n Input:')
print(X)

# shape of input array
print('\n Shape of Input:', X.shape)