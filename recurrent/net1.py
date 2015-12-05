import numpy as np

"""
Shit to understand:
    1. Data loading, inputs and outputs, in the input and output vectors are actually representations, only holding the indices to words.
    2.

    Input formats:
        'vocab' = 8000 words
        input: np.array(8000)
        output: np.array(8000)
        hidden state: np.array(100)

        U = input to hidden (8000 -> 100) Weights
        V = hidden to output (100 -> 8000) Weights
        W = hidden to hidden [passed] (100 -> 100) Weights

"""
def softmax(x):
    xt = np.exp(x - np.max(x))
    return xt / np.sum(xt)

class Recurrent(object):
    def __init__(self, word_dim, hidden_dim = 100, bptt_truncate = 4):
        self.word_dim = word_dim
        self.hidden_dim = hidden_dim
        self.bptt_truncate = bptt_truncate
        # Randomly initialize the network parameters
        self.U = np.random.uniform(-np.sqrt(1./word_dim), np.sqrt(1./word_dim), (hidden_dim, word_dim))
        self.V = np.random.uniform(-np.sqrt(1./hidden_dim), np.sqrt(1./hidden_dim), (word_dim, hidden_dim))
        self.W = np.random.uniform(-np.sqrt(1./hidden_dim), np.sqrt(1./hidden_dim), (hidden_dim, hidden_dim))

    def propagate(self, x): #x is the input array of words
        # The total number of time steps
        T = len(x)
        # During forward propagation we save all hidden states in s because need them later.
        # We add one additional element for the initial hidden, which we set to 0
        s = np.zeros((T + 1, self.hidden_dim))
        s[-1] = np.zeros(self.hidden_dim)
        # The outputs at each time step. Again, we save them for later.
        o = np.zeros((T, self.word_dim)) #outputs
        # For each time step...
        for t in np.arange(T):
            #what is the difference between range, arange, xrange?
            # Note that we are indxing U by x[t]. This is the same as multiplying U with a one-hot vector.
            s[t] = np.tanh(self.U[:,x[t]] + self.W.dot(s[t-1]))
            o[t] = softmax(self.V.dot(s[t]))
        return [o, s]

    def predict(self, x):
        # Perform forward propagation and return index of the highest score
        o, s = self.propagate(x)
        return np.argmax(o, axis=1)

    def bptt(self, x, y):
        return x

def main():
    re = Recurrent(8000)
    print re.predict(np.zeros(1))

if __name__== '__main__':
    main()
