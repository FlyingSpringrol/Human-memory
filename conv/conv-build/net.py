import numpy as np
import numpy.random as rand
'''
CONVOLUTIONAL NET:
Matrix based approach to a simple convolutional net:
    Need to conceptually understand,
    Sections:
        1. Data input/output
        2. Activation functions
        3. Error Functions
        4. Convolution
        5. Backprop

'''

class Net(object):
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.weights = []
        self.score = 0

    def create_containers(self):
        self.biases = [rand.randn(-1,1,x) for layer in self.dimensions] #create biases
        self.weights = self.createWeights()

    def score(self, target):
        #how should you evaluate the target? Generative or convergent solution?

    def create_weights(self):
        weights = []
        for idx in range(len(self.dimensions) - 1): #iterate from first layer up to last
            weights[idx] = [np.zeros(self.dimensions[idx+1]) for i in range(self.dimensions[idx])]
        self.weights = weights
    def propagate(self, input):
        #activations * biases = input layer activations



class ConvLayer(object):
    def __init__(self):

    def

class Softmax(object):
    def __init__(self):

class FullConnected(object):
    def __init__(self):
