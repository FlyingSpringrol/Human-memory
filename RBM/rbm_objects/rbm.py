import numpy as np
from numpy import random as rand


'''
TODO:
-fix biases for training process
-make the inputs prescribe to a set of rules

Done:
XXX-Optimize: make training multi-data matrix multiplication (nlog(n)) time: versus current
(n = matrix size?)
XXX-For mnist, performance gain is 10000*(1*log(1)) / 10000*log(10000) times faster
XXX-Add in load_data and save_data methods
'''
def validate(states):
    #validate vector to see if valid bias: activation ratio
    if (state[0]):
        return False

def activate(prob):
    if rand.random() < prob:
        return 1.0
    else: return 0.0

get_states = np.vectorize(activate)

def sigmoid(x):
    return 1/ (1 + np.power(np.e, -x))

vec_sig = np.vectorize(sigmoid)

def construct(weights, vis_states):
    #returns the hidden probabilities
    hid_states =  np.dot(vis_states, weights)
    return vec_sig(hid_states)

def reconstruct(weights, hid_states):
    #returns the visible probabilities
    vis_states =  np.dot(hid_states, weights.T)
    return vec_sig(vis_states)

def train(weights, train_data, learning_rate = .1, max_epochs = 3000):
    #return trained weight matrix
    num_examples = len(train_data)
    vis_inputs = train_data
    vis_inputs[:,0] = 1 #fix vis_input bias unit
    errors = []

    for i in xrange(max_epochs):
        #for vis_inputs in train_data:

        pos_hid_probs = construct(weights, vis_inputs)
        pos_hid_states = get_states(pos_hid_probs)
        neg_vis_probs = reconstruct(weights, pos_hid_states)
        neg_vis_states = get_states(neg_vis_probs)
        neg_hid_probs = construct(weights, neg_vis_states)
        neg_vis_probs[:,0] = 1 # Fix the bias unit.

        pos_associations = np.dot(np.matrix(vis_inputs).T, np.matrix(pos_hid_probs))
        neg_associations = np.dot(np.matrix(neg_vis_probs).T, np.matrix(neg_hid_probs))


        weights += (learning_rate * (pos_associations - neg_associations))/num_examples
        #print reconstruction error
        error = np.sum((vis_inputs  - neg_vis_probs) ** 2) / num_examples
        print "Epoch number ", i, ": Average Error is ", error
        errors.append((i, error))
    return (weights, errors)

def daydream(iterations, vis_states):
    #day dream gibbs iterations
    vis = np.copy(vis_states)
    hid = construct(vis_states)
    for i in xrange(iterations):
        vis = reconstruct(hid)
        hid = construct(vis)
    return (vis, hid)

def generate_weights(num_hid, num_vis):
    w = rand.randn(num_vis + 1, num_hid + 1)
    return w

def insert_biases(training_data):
    #if the beginnings don't have bias activations, add them in
    return np.insert(training_data, 0, 1, axis = 1)

def translate(inputs, translations):
    inputs = inputs[0][1:]
    for idx, i in enumerate(inputs):#sequential iteration right?
        if i == 1:
            return translations[idx]
    return "No translation found"

def run(weights, visibles, hiddens, vis_trans, hid_trans):
    for visible in visibles:
        print translate(get_states(construct(weights, visibles)), hid_trans)
    for hidden in hiddens:
        print translate(get_states(reconstruct(weights, hiddens)), vis_trans)
def save_weights(weights, path):
    np.savetxt(path, weights, delimiter= ',')

def load_weights(path):
    weights = np.loadtxt(open(path,"rb"),delimiter=",",skiprows=1)
    return weights
