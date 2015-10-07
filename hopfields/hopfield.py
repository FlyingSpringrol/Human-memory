import numpy as np
""""
Hopfield nets: single layers, fully connected NN
-Symmetric weights
-Network of oscillators


Store patterns: infer nearby solution when presented with corrupted input
Core idea: minimizing energy by correlating nodes

Recurrent network that iterates through itself until a local minima is reached.
Eg: The memory is returned


Variables that affect ability to infer: (range of off values)
Limit on stored memories
Absolute minimums (screw up net)

Dales law

QUESTION:

--WHAT IS LOCAL CORRELATION!--
Inputs have information about other inputs

"""
def random_seq(list_size):
    return 1# array of random indices

class Hopfield(object):
    def __init__(self, node_num, target_states):
        self.nodes = node_num #self.nodes = # of nodes
        self.target_states = target_states
        self.weights = (2) * np.random.random((self.nodes, self.nodes)) -1 #random range from -1 to 1
        self.rate = 1/self.nodes
        self.states = np.random.random(self.nodes)
        self.biases = np.zeros(self.nodes)
        print self.weights
    def sync_update(self):
        #has to find the node activation * the weight + bias
        sums = np.zeros(self.nodes)
        for nodeIdx, node in enumerate(self.states):
            for idx, node in enumerate(self.states):
                if idx == nodeIdx: continue
                sums[nodeIdx] += self.weights[idx][nodeIdx] * self.states[idx] #weight* activation
        self.states = sums
        self.binary_sums() #states = 0 or -1

    def binary_sums(self):
        self.states = [self.flip(input) for input in self.states]

    def flip(self, input):
        if (input > 0):
            return 1
        else: return -1

    def async_update(self):
        #come back and make sure, self-connections are 0?
        nodeIdx = random.randInt((0, self.nodes))
        sum = 0
        for idx, node in enumerate(self.states):
            if idx == nodeIdx: continue
            sum += self.weights[idx][nodeIdx] * self.states[idx] #weight* activation
        self.states[nodeIdx] = sum
    def update_weights(self):
        for node_idx, node1 in enumerate(self.states):
            for idx, node2 in enumerate(self.states):
                self.weights[node_idx][idx] = self.rate * node1 * node2
                self.weights[idx][node_idx] = self.rate * node1 * node2

    def iterate(self, inputs, iterations):
        for i in range(iterations):
            for input in inputs:
                self.states = input
                self.sync_update()
                self.update_weights()
                print self.states

    def output(self):
        answer = ""
        for node, idx in enumerate(self.nodes):
            answer += 'output' + idx + ': ' + node + ' '
        print answer

    def calculate(self, input, type):
        print a

a = [1,0,0,0,0]
b = [0,0,0,0,1]
a = np.asarray(a)
b = np.asarray(b)

def main():
    hop = Hopfield(5, [[0,1,1,0,1]])
    hop.iterate([a,b], 10)
if __name__ == "__main__":
    main()
