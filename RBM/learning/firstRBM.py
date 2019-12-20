import numpy as np
from numpy import random as rand
import sys


def sigmoid(x):
    return 1.0/(1+ np.power(np.e, -x))

vec_sig = np.vectorize(sigmoid)

def bin(state):
    if rand.random() < state:
        return 1.0
    else: return 0.0

vec_bin = np.vectorize(bin)


class Layer():
    """
    2 layer RBM class, Meant to be modular... recycle code to be part of Deep Belief Net.

    """
    def __init__(self, visibles, hiddens, learning_rate = 0):
        self.weights = [rand.randn(visibles) for h in xrange(hiddens)] #weights = inputs to hiddens
        self.vis_biases = rand.randn(visibles) #weights for bias to visuals
        self.hid_biases = np.zeros(hiddens) #weights for bias to hiddens

        self.vis_states = np.zeros(visibles) #container for current states
        self.hid_states = np.zeros(hiddens) #container for current states
        #learning rate assignment
        if learning_rate== 0:
            self.learning_rate = visibles * hiddens * .001
        else: self.learning_rate = learning_rate
        #number of visibles and hiddens
        self.visibles = visibles
        self.hiddens = hiddens

    def train(self,inputs):
        '''
        Contrastive divergence algorithm
        '''
        #step 1
        self.construct(inputs, False)
        v = np.copy(self.vis_states)
        h = np.copy(self.hid_states)
        #step 2
        self.reconstruct(h, False)
        self.construct(self.vis_states, False)
        v_p = self.vis_states
        h_p = self.hid_states
        #insert the bias activations into the activation vectors
        v = np.insert(v, 0, 1.0)
        h = np.insert(h, 0, 1.0)
        v_p = np.insert(v_p, 0, 1.0)
        h_p = np.insert(h_p, 0, 1.0)
        #get gradients
        changes = (np.outer(h, v) - np.outer(h_p, v_p))
        #get MSE
        err = np.sum(changes)**2
        ax1 = changes[:,0][1:].flatten() #get pad column
        ax2 = changes[:1].flatten()[1:] #get pad row
        #remove bias padding
        changes = np.delete(changes, 0, axis = 0)
        changes = np.delete(changes, 0, axis = 1)
        print changes.shape

        self.hid_biases += self.learning_rate * ax1
        self.vis_biases += self.learning_rate * ax2
        self.weights += self.learning_rate * changes

        return err

    def construct(self, vis, prob = False):
        '''
        Construct hidden states from visibles
        '''
        #calculate activations
        self.vis_states = np.copy(vis) #set visibles
        self.hid_states[:] = 0
        for i in xrange(self.hiddens):
            for j in xrange(self.visibles):
                self.hid_states[i] +=  self.weights[i][j] * self.vis_states[j]
        #add biases
        for i in xrange(self.hiddens):
            self.hid_states[i] += self.hid_biases[i]
            self.hid_states[i] = sigmoid(self.hid_states[i])
        if prob:
            self.hid_states = vec_bin(self.hid_states)

    def reconstruct(self, hiddens, prob = False):
        '''
        reconstruct visible states from hiddens
        '''
        self.hid_states = np.copy(hiddens) #set visibles
        self.vis_states[:] = 0
        for i in xrange(self.hiddens):
            for j in xrange(self.visibles):
                self.vis_states[j] +=  self.weights[i][j] * self.hid_states[i]
        #add biases
        for i in xrange(self.visibles):
            self.vis_states[i] += self.vis_biases[i]
            self.vis_states[i] = sigmoid(self.vis_states[i])
        if prob:
            self.vis_states = vec_bin(self.vis_states)

    def test(self):
        print 'hiddens: ',self.hid_states
        print 'Visibles: ', self.vis_states
    def p_weights(self):
        print 'Weights', self.weights
        print 'Vis_biases', self.vis_biases
        print 'Hid_biases', self.hid_biases

key_vis = ["Theory of General Relativity", "Tobacco", "Drinking Heavily", "Molly", "Leo Tolstoy", "Higher Education"]
key_hid = ["Smart", "Not Smart"]
data = {"data0": [1, 0, 0, 0, 1, 1], "data1": [1, 0, 0, 0, 1, 1], "data2": [0, 0, 1, 1, 1, 0], "data3": [0, 1, 1, 1, 0, 0], "data4": [1, 1, 0, 0, 1, 1]}

def test(x):
    layer = Layer(6, 2, 1)
    layer.reconstruct([1,0], True)
    layer.test()
    layer.construct([1, 0, 0, 0, 1, 1], True)
    layer.test()
    for j in range(x):
        for i in xrange(5):
            keyed = data["data" + str(i)]
    layer.reconstruct([1,0], True)
    layer.test()
    layer.construct([1, 0, 0, 0, 1, 1], True)
    layer.test()
    layer.p_weights()
    return layer

x = 1
for arg in sys.argv[1:]:
    if (arg):
        x = int(arg)
layer = test(x)
