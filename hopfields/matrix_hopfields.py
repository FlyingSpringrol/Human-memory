"""
Going to rewrite the code I had. It was getting far too convoluted and becoming
an enormous time suck

"""
import random
import numpy as np
def binary(input): #return 0 or 1
    if (input > 0):
        return 1
    else: return -1
vec_bin = np.vectorize(binary)

class Hopfield(object):
    def __init__(self, nodes, target_set):
        self.num_nodes = nodes
        self.nodes = np.zeros(self.num_nodes) #holds node activations
        self.weights = np.random.random((nodes, nodes)) #weights
        #self.random_idxs = np.arange(nodes).shuffle() #used in async updating
        self.target_set = target_set
        self.rate = 1/self.num_nodes

    def async_update(self, input): #nodes selected randomly
        #would it be useful to have a stored, random array of node indices to be used?
        self.nodes = input
        node_idx = random.randint(0,self.num_nodes-1)
    def calc_activation(self, node_idx): #to make code more modular
        sum = 0
        for i in range(self.nodes.size):
            if i == node_idx:
                continue
            sum += self.weights[i,node_idx]
        self.nodes[node_idx] = sum

    def sync_update(self):
        for node_idx, node in enumerate(self.nodes):
            self.calc_activation(node_idx)

    def update_weights(self):
        pNew = (np.matrix(self.nodes) * np.matrix(self.nodes).transpose() - np.identity(self.num_nodes))
        pNew = vec_bin(pNew)
        self.weights = vec_bin(self.weights) #apply binary flip to all weights
        self.weights = self.weights + pNew
    def run(self):
        for target in self.target_set:
            self.nodes = target
            for i in range(100):
                self.sync_update()
                self.update_weights()
        print self.weights

a = [1,1,1,1,1]
b = [-1,-1,-1,-1,-1]
c = [1,1,1,-1,-1]
a = np.asarray(a)
b = np.asarray(b)
c = np.asarray(c)

def main():
    hop = Hopfield(5,[a,b,c])
    hop.run()
main()
