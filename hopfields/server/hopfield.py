import numpy as np
import random
import pdb

""""
NOTE:
    The random weight initialization makes classification accuracy extremely
    volatile!


"""

def bin(input):
    if input >= 0:
        return 1
    else:
        return -1
vec_bin = np.vectorize(bin)

class Hopfield(object):
    def __init__(self, nodes, targets):
        self.num_nodes = nodes
        self.targets = targets
        self.current_states = vec_bin(np.random.uniform(-1,1, self.num_nodes))
        self.weights = np.matrix(self.current_states).transpose() * np.matrix(self.current_states)
        np.fill_diagonal(self.weights, 0)
        self.new_states = np.zeros(self.num_nodes)
        self.rate = .01
        self.targets = targets
        self.remembered = []

    def train(self, target, max_iterations = 10000):
        iterations = 0
        self.current_states = np.copy(target)
        while iterations < max_iterations:
            iterations += 1
            self.async_update() #updates the new_states
            if np.array_equal(self.new_states, target):
                #if output = the target
                return
            self.current_states = np.copy(self.new_states)
            self.update_weights()

    def add_target(self, target): #used for server training
        if (target.size != self.num_nodes):
            print "Wrong size inputs"
            return False
        if len(self.targets) > self.max_patterns(): #or should it prevent it from updating?
            print 'targets reset'
            self.reset()
        self.targets.append(target)
        self.train(target)
        print len(self.targets)
    def reset(self):
        print 'reset net'
        self.targets = []
        self.current_states = vec_bin(np.random.uniform(-1,1, self.num_nodes))
        self.weights = np.matrix(self.current_states).transpose() * np.matrix(self.current_states)
        self.remembered = []
        np.fill_diagonal(self.weights, 0)
        self.new_states = np.zeros(self.num_nodes)

    def update_weights(self):
        pNew = np.matrix(self.current_states).transpose() * np.matrix(self.current_states) - np.matrix(np.identity(self.num_nodes))
        self.weights = self.weights + self.rate * pNew

    def sync_update(self):
        """
        Calculates new_states, but does not set current_states equal to new_states!
        """
        self.new_states[:] = 0
        self.current_states = vec_bin(self.current_states)
        for node_idx, cur_node in enumerate(self.current_states): #iterate through all states
            for i, node in enumerate(self.current_states):
                if i == node_idx:
                    continue
                else:
                    self.new_states[node_idx] += self.weights[node_idx, i] * self.current_states[i]
        self.new_states = vec_bin(self.new_states)
    def async_update(self):
        self.current_states = vec_bin(self.current_states)
        self.new_states = np.copy(self.current_states)
        node_idx = np.random.randint(0, self.current_states.size)
        for i, node in enumerate(self.current_states):
            if i == node_idx:
                continue
            else:
                self.new_states[node_idx] += self.weights[node_idx, i] * self.current_states[i]
        self.new_states = vec_bin(self.new_states)
    def is_stable(self):
        #if values are equal
        if np.array_equal(self.current_states, self.new_states):
            return True
        return False
    def run(self):
        print self.weights
        for target in self.targets:
            self.train(target)
        print self.weights
    def max_patterns(self):
        #return the maximum amount of patterns
        return .144 * self.num_nodes

    """
    Test methods
    """
    def test(self, input, testNum, max_iterations = 100):
        print "\nTest num: ", testNum
        self.current_states = np.copy(input)
        for i in range(max_iterations):
            self.async_update()
            self.current_states = np.copy(self.new_states)
        #how to fix the flipped bit problem?
        return self.current_states
    def print_states(self):
        print 'current states ', self.current_states
        print 'new states, ', self.new_states
    def print_memories(self):
        print '\n Saved states for test: '
        for memory in self.remembered:
            print 'Original Target', memory[1]
            print 'Corresponding Memory', memory[0], '\n'


#testing stuff
a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
b = [1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
a = np.asarray(a)
b = np.asarray(b)
test1 = np.asarray([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
test2 = np.asarray([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
test3 = np.asarray([1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1])
test4 = np.asarray([1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1])
def main():
    hop = Hopfield(15,[a,b])
    hop.max_patterns()
    hop.run()
    hop.print_memories()
    print hop.test(test1, 1)
    print hop.test(test2, 2)
    print hop.test(test3, 3)
    print hop.test(test4, 4)

if __name__ == '__main__':
    main()
