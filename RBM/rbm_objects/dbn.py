import rbm
import mnist
import numpy as np
import pickle
'''
TODO:
-figure out hyperparameters
-visualize error over time
-Figure out non-fixed bias problem
-Softmax output layer
-Add minibatches to this shit
'''
def softmax(inputs, target):
    output = 0
    for i in inputs:
        output += np.exp(i)
    return target/output

def generate_dbn_weights(dimensions):
    zipped = zip(dimensions[1:], dimensions[:-1])
    w = []
    for pair in zipped:
        w.append(rbm.generate_weights(pair[0], pair[1]))
    w = np.array(w)
    return w

def train_dbn(dbn_weights, training_data, learning_rate = .1, max_epochs = 1):
    #train layer by layer
    #fully train one layer, then train the next, until all are trained
    for idx, weight in enumerate(dbn_weights):
        if idx == 0: #first layer training
            rbm.train(weight, training_data, learning_rate, max_epochs)
            continue

        else:
            training_data = rbm.get_states(rbm.construct(dbn_weights[idx-1], training_data))

        rbm.train(weight, training_data,learning_rate, max_epochs)
    return dbn_weights

def construct(weights, vis_states):
    for weight in weights:
        vis_states = rbm.construct(weight, vis_states)
    return vis_states

def reconstruct(weights, hid_states):
    for i in range(len(weights)+1)[1:]:
        hid_states = rbm.reconstruct(weights[-i], hid_states)
    return hid_states

def pickle_weights(weights, path):
    data = {'weights': weights}
    output = open(path, 'wb')
    pickle.dump(data, output)
    output.close()

def unpickle(path):
    pkl_file = open(path, 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    return data['weights']
if __name__ == "__main__":
    data = mnist.load_mnist('../../../mnist_test.csv')
    data = rbm.insert_biases(data)
    dims = [784, 200, 50, 10]
    dbn_weights = generate_dbn_weights(dims)
    dbn_weights = unpickle('../weights/300_dbn.pkl')
    #dbn_weights = train_dbn(dbn_weights, data, max_epochs = 2000)
