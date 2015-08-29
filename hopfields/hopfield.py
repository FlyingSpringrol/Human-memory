import numpy as np
""""
Hopfield nets: single layers, fully connected NN
-Symmetric weights
-Network of oscillators


Store patterns: infer nearby solution when presented with corrupted input
Core idea: minimizing energy by correlating nodes


Variables that affect ability to infer: (range of off values)
Limit on stored memories
Absolute minimums (screw up net)




QUESTION:

--WHAT IS LOCAL CORRELATION!--
Inputs have information about other inputs

"""
def random_seq(list_size):
    return 1# array of random indices

class Hopfield(object):
    def __init__(self, node_num, target_states, rate):
        self.node_num = node_num
        self.nodes = [0] * node_num # array of values
        self.target_states = target_states
        self.weights = []
        self.rate = rate

        self.make_weights()


    def make_weights(self):
        #create the weight matrix to be used
        #
        #weights = np.create_matrix(self.nodes, self.nodes)
        weights = []
        for i in range(self.node_num):
            row = []
            for j in range(self.node_num):
                row.append(0)
            weights.append(row)
        print weights
        #matrix = np.matrix(weights)
        self.weights = weights

    def init_weights(self):
        #weights are a nice square matrix
        weights = []
        width = len(self.weights)
        for input in self.target_states:
            #self.weights = []
            x_count = 0
            for i in range(width):
                y_count = 0
                for j in range(width):
                    if j == x_count and j == y_count:
                        self.weights[i][j] = 0
                    else: self.weights[i][j] = (2*input[x_count]-1)*(2*input[y_count]-1)
                    y_count+=1
                x_count+=1
            weights.append(self.weights)
        return weights


    def sync_update(self):
        self.a = 1

    def async_update(self):
        #come back and make sure, self-connections are 0?
        for row in self.weights:
            for column in self.weights[row]:
                self.nodes[row] += self.weights[row][column]
                #also update weights
    def hebb_train(self):
        for node in self.nodes:
            a = 1
            #try to
    def output(self):
        answer = ""
        for node, idx in enumerate(self.nodes):
            answer += 'output' + idx + ': ' + node + ' '
        print answer
    def print_weights(self):
        length = len(self.weights)
        for i in range(length):
            for j in range(length):
                print self.weights[i][j]



    def calculate(self, input, type):
        print a

def main():
    hop = Hopfield(5, [[0,1,1,0,1]], 1)
    hop.init_weights()
main()
