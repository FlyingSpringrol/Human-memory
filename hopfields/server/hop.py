import numpy as np
from numpy import random as rand

def sigmoid(x):
    return 1 / (1 + (np.power(np.e, -x)))
def flip(x):
    return -x
flipped = np.vectorize(flip)

''''
Shit to add:
Visualization of nodes and asynch updates?


'''
class Hopfield(object):
    def __init__(self, targets, num_nodes, learning_rate = .01):
        self.targets = targets #targets must be array
        self.num_nodes = num_nodes
        self.weights = np.zeros((self.num_nodes, self.num_nodes))
        self.states = np.zeros(self.num_nodes)

        #self.hebb_train(targets)

    def calc_weight(self, i, j, patterns):
        weight_ij = 0.0
        num_pats = len(patterns)
        for pattern in patterns:
            weight_ij += pattern[i] * pattern[j]
        return (1.0 / float(num_pats)) * weight_ij

    def calc_weights(self, patterns):
        w = np.copy(self.weights)
        for i in xrange(self.num_nodes):
            for j in xrange(self.num_nodes):
                w[i][j] = self.calc_weight(i, j, patterns)
        return w

    def set_weights(self, weights):
        self.weights = weights

    def hebb_train(self, patterns):
        w = self.calc_weights(patterns)
        w = np.matrix(w)
        w = w - np.identity(self.num_nodes)
        self.set_weights(w)

    def async_update(self, node, pattern):
        #return new state for neuron
        state = 0.0
        for i, neuron in enumerate(self.states):
            if i == node:
                continue
            else:
                state += self.weights[node, i] * self.states[i]
        return 1.0 if state > 0 else -1.0

    def run(self, pattern, max_iterations = 15):
        self.states = np.copy(pattern)
        changed = False
        update_list = range(len(self.states))
        for i in xrange(max_iterations):
            rand.shuffle(update_list)
            changed = False
            for node in update_list:
                new_state = self.async_update(node, pattern)
                if new_state != self.states[node]:
                    print 'change'
                    changed = True
                self.states[node] = new_state
            if not changed:
                return (True, self.states)
        return (False, self.states)

    def sync_update(self, pattern):
        return 1
    def print_weights(self):
        toprint= self.weights.flatten()
        for i in toprint:
            print i
    def set_targets(self,targets):
        self.targets = targets

    def reset_hop(self):
        self.targets = []
        self.weights = np.zeros((self.num_nodes, self.num_nodes))
        self.states = np.zeros(self.num_nodes)
    def reset_states(self):
        self.states = np.zeros(self.num_nodes)

def test():
    #returning inverses? Why?
    a = [1,-1,-1,-1,1]
    b = [-1,-1,-1,-1,-1]
    d = [1,1,-1,-1,1]
    e = [-1,-1,-1,1,-1]
    hop = Hopfield([a,b])
    c = hop.run(e)
    f = hop.run(d)
    print c
    print f
    print hop.weights
