import numpy as np
import random
import pdb

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
        self.rate = 1/self.num_nodes
        self.targets = targets
        self.remembered = []

    def train(self, target, max_iterations = 10):
        iterations = 0
        self.current_states = np.copy(target)
        while iterations < max_iterations:
            #pdb.set_trace()
            iterations += 1
            self.sync_update() #updates the new_states
            if self.is_stable(): #compares new_states and current_states
                print "Stable pattern"
                self.remembered.append((self.current_states, target))
                return True #stops the update
            self.current_states = np.copy(self.new_states)
            self.update_weights()
        print 'No stable pattern established'
        return False

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
        self.weights = self.weights + (pNew)

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

    def is_stable(self):
        #if values are equal
        if np.array_equal(self.current_states, self.new_states):
            return True
        return False


    def run(self):
        for target in self.targets:
            self.train(target)
        print self.weights
    def max_patterns(self):
        #return the maximum amount of patterns
        return .144 * self.num_nodes

    """
    Test methods
    """
    def test(self, input):
        self.current_states = np.copy(input)
        stable = 0
        for i in range(100): #runs 1000 times before returning false
            self.sync_update()
            self.current_states = np.copy(self.new_states)
            if self.is_stable():
                stable +=1
            if stable >= 1:
                """
                Just offline test stuff
                print '\n found pattern'
                print 'current pattern', self.current_states
                for memory in self.remembered:
                    print 'saved state', memory[1]
                    print 'original target', memory[0]
                """
                print 'pattern found'
                return self.find()
        print 'no pattern found'
        return self.current_states
    def find(self): #iterate through the memories looking for the match
        for memory in self.remembered:
            if np.array_equal(memory[0], self.current_states):
                return memory[1]
        else: return self.current_states
    def print_states(self):
        print 'current states ', self.current_states
        print 'new states, ', self.new_states



#testing stuff
a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
b = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1]
a = np.asarray(a)
b = np.asarray(b)
test1 = np.asarray([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
test2 = np.asarray([-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
test3 = np.asarray([1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1])
def main():
    hop = Hopfield(15,[a,b])
    hop.max_patterns()
    hop.run()
    hop.test(test1)
    hop.test(test2)
    hop.test(test3)

if __name__ == '__main__':
    main()
