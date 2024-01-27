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

# creating the output array
y=np.array([[1],[1],[0]])

# output in matrix form
y = y.T

print ('\n Actual Output:')
print(y)

# shape of output array
print('\n Shape of Output:', y.shape)

# defining the Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

# defining the hyperparameters of the model
lr=0.001 # learning rate
inputlayer_neurons = X.shape[0] # number of features in data set
hiddenlayer_neurons = 3 # number of hidden layers neurons
output_neurons = 1 # number of neurons at output layer

epochs = 10000 # number of epochs

# initializing weight
w_ih=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
w_ho=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))

error_adam = []
# parameters for Adam
beta_1 = 0.9
beta_2 = 0.9
u_ih = 0
u_ho = 0
v_ih = 0
v_ho = 0

for i in range(epochs):
    # Forward Propogation
    
    # hidden layer activations
    hidden_layer_input=np.dot(w_ih.T,X)
    hiddenlayer_activations = sigmoid(hidden_layer_input)    
    # calculating the output
    output_layer_input=np.dot(w_ho.T,hiddenlayer_activations)
    output = sigmoid(output_layer_input)
    
    
    # Backward Propagation
    
    # calculating error
    error = np.square(y-output)/2
    error_wrt_output = -(y-output)
    output_wrt_Z2 = np.multiply(output,(1-output))
    Z2_wrt_who = hiddenlayer_activations
    # rate of change of error w.r.t weight between output and hidden layer
    error_wrt_who = np.dot(Z2_wrt_who,(error_wrt_output*output_wrt_Z2).T)
    Z2_wrt_h1 = w_ho
    h1_wrt_Z1 = np.multiply(hiddenlayer_activations,(1-hiddenlayer_activations))
    Z1_wrt_wih = X
    # rate of change of error w.r.t weights between input and hidden layer
    error_wrt_wih = np.dot(Z1_wrt_wih,(h1_wrt_Z1*np.dot(Z2_wrt_h1,(error_wrt_output*output_wrt_Z2))).T)
    
    # weighted squared gradients
    u_ho = beta_1 * u_ho + (1-beta_1) * np.square(error_wrt_who)
    u_ih = beta_1 * u_ih + (1-beta_1) * np.square(error_wrt_wih)
    
    # weighted gradients
    v_ho = beta_2 * v_ho + (1-beta_2)*error_wrt_who
    v_ih = beta_2 * v_ih + (1-beta_2)*error_wrt_wih
    
    # updating the learning rate
    new_lr_o = lr / np.sqrt(u_ho.sum())
    new_lr_h = lr / np.sqrt(u_ih.sum())

    # updating the weights
    w_ho = w_ho - new_lr_o * v_ho
    w_ih = w_ih - new_lr_h * v_ih
    error_adam.append(np.average(error))


    # visualizing the error after each epoch
plt.plot(np.arange(1,epochs+1), np.array(error_adam))
plt.show()
