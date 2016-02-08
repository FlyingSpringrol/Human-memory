import numpy as np
from numpy import random as rand

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
    for i in xrange(max_epochs):
        for vis_inputs in train_data:

            pos_hid_probs = construct(weights, vis_inputs)
            pos_hid_states = get_states(pos_hid_probs)
            neg_vis_probs = reconstruct(weights, pos_hid_states)
            neg_vis_states = get_states(neg_vis_probs)
            neg_hid_probs = construct(weights, neg_vis_states)

            pos_associations = np.dot(np.matrix(vis_inputs).T, np.matrix(pos_hid_probs))
            neg_associations = np.dot(np.matrix(neg_vis_probs).T, np.matrix(neg_hid_probs))


            weights += (learning_rate * (pos_associations - neg_associations))/num_examples
            #print reconstruction error
            error = np.sum((vis_inputs  - neg_vis_probs) ** 2)
            print "Epoch number ", i, ": Error is ", error
    return weights

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
    for train in training_data:
        np.insert(train, 1, 0)
    return training_data


if __name__ == "__main__":
    #reference data
    input_vars = ["Tolstoy", "Relativity", "Calculus", " Acid", "Drinking Heavily", "Reggae on the River"]
    hidden_vars = ["smart", "not smart"]
    p1 = np.array([1,0,0,0,1,1,0])
    p2 = np.array([1,1,1,1,0,0,0])
    #run
    hids = 2
    vis = 6
    #training data = arrays with fixed biases in the first column
    training_data = np.array([[1,1,1,1,0,0,0],[1,1,0,1,0,0,0],[1,1,1,1,0,0,0],[1,0,0,1,1,1,1], [1,0,0,1,1,0,0],[1,0,0,1,1,1,1]])

    weights = generate_weights(hids, vis)
    weights = train(weights, training_data)
    print weights
    print(construct(weights, p1))
    print(construct(weights, p2))
