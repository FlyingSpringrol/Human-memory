"""
Algorithm:
1. Calc error = output layer delta
2. Multiply inputs by error * derivative of activation = neuron delta
3. adjust

"""
import random
import math
import numpy as np
from connection import Connection

def sig(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))
def der_sig(z):
    """Derivative of the sigmoid function."""
    return sig(z)*(1-sig(z))

class Neuron(object):
    def __init__(self, layerID, number, learning_rate):
        #connections
        self.outputs = []
        self.inputs = []
        #bias
        self.bias = random.uniform(-1,1)#np.random.randn(0,1)
        #state variables
        self.activation = 0
        self.state = 0
        self.delta = 0
        self.learning_rate = learning_rate
        #id information
        self.layerID = layerID
        self.number = number #just id information
        self.id = self.makeID()
    #initialzation code:
    def set_weights(self, net_size):
        self.bias = random.uniform(-1/net_size, 1/net_size)
    def connect_output(self, other_neuron):
        connect = Connection(self, other_neuron, self.learning_rate)
        self.outputs.append(connect)
        other_neuron.inputs.append(connect)
    def makeID(self):
        id = ''
        id = self.layerID + ':' + str(self.number)
        return id
    def backprop(self): #calculates delta, using information of layer before
        for connection in self.outputs:
            output_neuron = connection.output #collect the connection output
            self.delta += output_neuron.delta * self.state
            connection.calculate() #only needs forward deltas and input activation for weight_grad
        self.delta= self.delta * der_sig(self.activation)
    def adjust(self):
        self.bias += self.delta * self.learning_rate
        for connection in self.outputs:
            connection.adjust()
    def calculate(self):
        if self.layerID != 'layer0': #if not in input layer
            self.activation += self.bias
        for connection in self.inputs:
            input = connection.input.state * connection.weight #store old activation
            self.activation += input
        self.state = sig(self.activation)
    def recover(self):
        self.activation = 0
        self.state = 0
        self.delta = 0
        for connect in self.outputs:
            connect.recover()
    def print_info(self):
        print 'bias: ' + str(self.bias)
