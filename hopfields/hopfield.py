import numpy as np
import random
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


    def sync_update(self):
        #has to find the node activation * the weight + bias
        sums = np.zeros(self.nodes)
        for nodeIdx, node1 in enumerate(self.states):
            for idx, node2 in enumerate(self.states):
                if idx == nodeIdx: continue
                sums[nodeIdx] += self.weights[idx,nodeIdx] * self.states[idx] #weight* activation
        self.states = sums
        self.binary_sums() #states = 1 or -1

    def binary_sums(self):
        self.states = [self.flip(input) for input in self.states]

    def flip(self, input):
        if (input > 0):
            return 1
        else: return -1
    def async_update(self):
        #come back and make sure, self-connections are 0?
        for i in range(self.nodes):
            nodeIdx = random.randint(0, self.nodes-1)
            sum = 0
            for idx, node in enumerate(self.states):
                if idx == nodeIdx: continue
                sum += self.weights[idx,nodeIdx] * self.states[idx] #weight* activation
            self.states[nodeIdx] = self.flip(sum)
    def update_weights(self):
        """
        newWeight matrix = old weight matrix  + learning rate * (nodes * nodesTransposed - identity)

        """
        pNew = (np.matrix(self.states) * np.matrix(self.states).transpose() - np.identity(len(self.states)))
        flip = np.vectorize(self.flip)
        self.weights = self.weights + self.rate * pNew
        self.weights = flip(self.weights)


    def iterate(self, inputs, iterations):
        for i in range(iterations):
            for input in inputs:
                self.states = input
                self.async_update()
                self.update_weights()
        print self.weights
    def check(self, target): #checks if target == current states
        if (self.states == target).all():
            print "found"
            print target
            return True
        return False

    def inject(self, inputs, targets):
        test = 0 #used for printing
        for input in inputs:
            actualFound = False
            possible = 1000 #max iterations of searching
            while actualFound == False and possible > 0:
                possible -=1
                self.states = input
                self.async_update()
                for target in targets:
                    found = self.check(target) #being reassigned by last call
                    if (found == True):
                        actualFound = True
            test += 1
            print "test" + str(test) + str(input)
            print self.states

    def output(self):
        answer = ""
        for node, idx in enumerate(self.nodes):
            answer += 'output' + idx + ': ' + node + ' '
        print answer

    def calculate(self, input, type):
        print a

a = [1,1,1,1,1]
b = [-1,-1,-1,-1,-1]
c = [1,1,1,-1,-1]
a = np.asarray(a)
b = np.asarray(b)
c = np.asarray(c)

test1 = np.asarray([-1,-1,1,1,1])
test2 = np.asarray([-1,1,-1,-1,1])


def makeT():
    a = 2

def main():
    hop = Hopfield(5, [[0,1,1,0,1]])
    hop.iterate([a,b,c], 1000)
    hop.inject([test1,test2, c], [a,b,c])
if __name__ == "__main__":
    main()
