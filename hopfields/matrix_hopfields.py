"""
Going to rewrite the code I had. It was getting far too convoluted and becoming
an enormous time suck

"""
import random
import numpy as np
import pdb

def binary(input): #return 0 or 1
    if (input > 0):
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
        print self.weights
        #self.random_idxs = np.arange(nodes).shuffle() #used in async updating
        self.target_set = target_set
        self.rate = 1/self.num_nodes
    def init_weights(self, node_num): #create symmetrical weight matrix
        weights = np.zeros((node_num, node_num))
        for i in range(node_num):
            weights[i][:i] = 2* random.random() -1
        weights = weights + weights.transpose()
        return weights


    def async_update(self): #nodes selected randomly
        #would it be useful to have a stored, random array of node indices to be used?
        node_idx = random.randint(0,self.num_nodes-1)
        self.calc_activation(node_idx)
        self.nodes = vec_bin(self.nodes)

    def calc_activation(self, node_idx): #calculates node activation
        sum = 0
        for i in range(self.nodes.size): #iterate down column
            if i == node_idx:
                continue
            sum += self.weights[i,node_idx] * self.nodes[i]
        self.nodes[node_idx] = sum

    def sync_update(self): #first iteration = all -1's for the weights
        for node_idx, node in enumerate(self.nodes):
            self.calc_activation(node_idx)
        self.nodes = vec_bin(self.nodes)

    def update_weights(self):
        self.weights = vec_bin(self.weights)
        pNew = (np.matrix(self.nodes).transpose()*np.matrix(self.nodes))
        self.weights = self.weights + pNew
        np.fill_diagonal(self.weights,0) #fill self connections
        print self.weights

    def run(self):
        for i in range(1000):
            for target in self.target_set:
                self.nodes = np.copy(target)
                self.async_update()
                self.update_weights()
        print self.weights
        #pdb.set_trace()
    def test(self, input):
        self.nodes = np.copy(input)
        for i in range(1000):
            self.async_update()
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

a = [1,1,1,1,1]
b = [1,1,1,1,1]
c = [-1,1,-1,-1,1]
d = [-1,-1,-1,-1,-1]
a = np.asarray(a)
b = np.asarray(b)
c = np.asarray(c)
d = np.asarray(d)
test1 = np.asarray([-1,-1,-1,-1,-1])
test2 = np.asarray([-1,1,-1,-1,1])
test3 = np.asarray([1,1,1,1,1])

def main():
    hop = Hopfield(5,[a,b,c,d])
    hop.run()
    hop.test(test1)
    hop.test(test2)
    hop.test(test3)
main()
