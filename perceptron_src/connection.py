import random
import math
import numpy as np

def sig(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))
def der_sig(z):
    """Derivative of the sigmoid function."""
    return sig(z)*(1-sig(z))

class Connection(object):
     #mostly just holds data: probably an unecessary class
     #ideas for good methods to add?
    def __init__(self, input, output, learning_rate):
        self.input = input
        self.output = output
        self.learning_rate = learning_rate

        self.weight = random.uniform(-1,1)#np.random.randn(0,1)
        self.weight_gradient = 0
        self.momentum = 1
    def set_weights(self, net_size): #assuming algorithmic answer to net size and weight distribution
        self.weight = random.uniform(-1/net_size, 1/net_size)
    def recover(self):
        a =2
    def calculate(self):
        new_gradient = self.output.delta * self.input.state
        if (cmp(new_gradient, 0) == 1): #compare the signs
            self.momentum *= 1 #should change
        else: self.momentum = 1
        self.weight_gradient = new_gradient

    def adjust(self):
        if (self.weight_gradient == 0):
            return
        adjust = self.weight_gradient * self.learning_rate * self.momentum
        self.weight += adjust
        #print 'adjusted: ' + self.input.id + ' ' + str(adjust)
