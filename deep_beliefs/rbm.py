import numpy as np
from numpy import random as rand


def sigmoid(x):
    return 1/(1+ np.power(np.e, -x))

def bin(state):
    if rand.random() > state:
        return 1
    else: return 0

vec_bin = np.vectorize(bin)


class Layer():
    """
    2 layer RBM class, Meant to be modular... recycle code to be part of Deep Belief Net.

    """
    def __init__(self, visibles, hiddens, learning_rate):
        self.weights = [rand.randn(visibles) for h in xrange(hiddens)] #weights = inputs to hiddens
        self.vis_biases = rand.randn(visibles)
        self.hid_biases = rand.randn(hiddens)
        self.vis_states = np.zeros(visibles)
        self.hid_states = np.zeros(hiddens)
        self.learning_rate = learning_rate

        self.visibles = visibles
        self.hiddens = hiddens

    def train(self,input):
        '''
        Contrastive divergence algorithm
        '''
        #step 1
        self.construct(input)
        v = np.copy(self.vis_states)
        h = np.copy(self.hid_states)
        #step 2
        self.reconstruct(h)
        self.construct(self.vis_states)
        v_p = self.vis_states
        h_p = self.hid_states
        #step 3
        changes = self.learning_rate * (np.outer(v,h) - np.outer(v_p, h_p))
        self.weights += changes.T

    def construct(self, vis):
        '''
        Construct hidden states from visibles
        '''
        #calculate activations
        self.vis_states = vis #set visibles
        for i in xrange(self.hiddens):
            for j in xrange(self.visibles):
                self.hid_states[i] +=  self.weights[i][j] * self.vis_states[j]
        #add biases
        for i in xrange(self.hiddens):
            self.hid_states[i] += self.hid_biases[i]
            self.hid_states[i] = sigmoid(self.hid_states[i])

        self.hid_states = vec_bin(self.hid_states)

    def reconstruct(self, hiddens):
        '''
        reconstruct visible states from hiddens
        '''
        self.hid_states = hiddens #set visibles
        for i in xrange(self.hiddens):
            for j in xrange(self.visibles):
                self.vis_states[j] +=  self.weights[i][j] * self.hid_states[i]
        #add biases
        for i in xrange(self.hiddens):
            self.vis_states[i] += self.vis_biases[i]
            self.vis_states[i] = sigmoid(self.vis_states[i])

        self.hid_states = vec_bin(self.hid_states)

    def test(self):
        print 'hiddens: ',self.hid_states
        print 'Visibles: ', self.vis_states
    def p_weights(self):
        print 'Weights', self.weights

def test():
    layer = Layer(10, 2, 1)
    layer.train(rand.randn(10))


test()
