"""
Going to rewrite the code I had. It was getting far too convoluted and becoming
an enormous time suck

Upper limit on patterns stored?
M/N ... .144

Oscillating between all 1s and all -1s... common neural net error?
Ooh, maybe that's where balance exists, avoiding deep convictions

Fuck, shit just doesn't work.
Will come back when I'm better at programming.
"""
import random
import numpy as np
import pdb

def binary(input): #return 0 or 1
    if (input >= 0):
        return 1
    else: return -1
vec_bin = np.vectorize(binary)

def tan_i(input):
    return 1

tan_i = np.vectorize(tan_i)


class Hopfield(object):
    def __init__(self, nodes, target_set):
        self.num_nodes = nodes
        self.nodes = np.zeros(self.num_nodes) #holds node activations
        self.weights = self.init_weights(self.num_nodes) #weights
        self.random_idxs = random.shuffle(np.arange(self.num_nodes)) #used in async updating
        self.target_set = target_set
        self.rate = 1/self.num_nodes
        self.new_states = np.zeros(self.num_nodes)
    def init_weights(self, node_num): #create symmetrical weight matrix
        weights = np.random.uniform(-1,1, self.num_nodes)
        weights = vec_bin(np.matrix(weights).transpose() * np.matrix(weights))
        np.fill_diagonal(weights,0)
        return weights

    def async_update(self): #nodes selected randomly
        node_idx = random.randint(0,self.num_nodes-1)
        self.calc_activation(node_idx)
        self.nodes = vec_bin(self.nodes)

    def calc_activation(self, node_idx): #calculates node activation
        sum = 0
        for i in range(self.nodes.size): #iterate down column
            if i == node_idx: #avoid self-connection, which is 0 anywat
                continue
            sum += self.weights[i, node_idx] * self.nodes[i]
        self.new_states[node_idx] = sum #store new states in array

    def sync_update(self): #first iteration = all -1's for the weights
        for node_idx, node in enumerate(self.nodes):
            self.calc_activation(node_idx)
        self.new_states = vec_bin(self.new_states)

    def update_weights(self):
        #change in weights == xi*xj (xi being neuron1, xj being neuron2)
        pNew = (np.matrix(self.nodes).transpose()*np.matrix(self.nodes)) - np.identity(self.num_nodes)
        self.weights = self.weights + pNew
        #np.fill_diagonal(self.weights,0) #fill self connections

    def run(self, max_iterations = 4):
        self.max_patterns() #prints the patterns that can be stored
        for target in self.target_set:
            iterations = 0
            stable = False
            while not stable and iterations < max_iterations:
                iterations+=1
                self.nodes[:] = target[:] #sets each number to target value
                self.sync_update()
                #stable = self.search_for_change() #checks to see if nodes == new_states
                self.nodes = self.new_states
                self.update_weights()
        print self.weights
        #pdb.set_trace()
    def test(self, input):
        self.nodes = np.copy(input)
        for i in range(2): #runs 1000 times before returning false
            self.sync_update()
            if self.check_all():
                print "Found! Sequence is " + str(self.nodes)
                return True
        return False

    def check_all(self):
        for target in self.target_set:
            if self.check(target):
                return True
        return False
    def check(self, target):
        for i in range(self.nodes.size):
            if (self.nodes[i] != target[i]):
                return False
        return True
    def search_for_change(self): #stop updating weights if stable state is reached
        return np.array_equal(self.new_states, self.nodes)

    def validate_weights(self): #weights must be symetrical, so should output a zero matrix
        #just compares the difference in the weight tranpose with a zero matrix
        zeroed_weights = (self.weights - self.weights.transpose())
        zero = np.matrix(np.zeros((self.num_nodes, self.num_nodes)))
        return np.array_equal(zero, zeroed_weights)
    def max_patterns(self):
        #return the maximum amount of patterns
        print 'Maximum patterns for this net: ' + str(.144 * self.num_nodes)

a = [1,1,1,1,1]
b = [1,1,1,1,1]
a = np.asarray(a)
b = np.asarray(b)
test1 = np.asarray([1,1,1,1,1])
test2 = np.asarray([1,1,1,1,1])

def main():
    hop = Hopfield(5,[a,b])
    hop.run()
    hop.test(test1)
    hop.test(test2)
main()
