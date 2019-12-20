import dbn
import rbm
import mnist
import csv
import numpy as np
'''
Index with functional methods to run all the RBM and DBN code from.

TODO:

-Error printing
-Fix noise
-Read papers
-Amount of gibbs-sampling (CD1, CD2, ... CDx), stable markov 

'''
mnist_path = "../../../mnist_test.csv"

def convert(x):
    return int(x)/255.0
normalize = np.vectorize(convert)

def train_dbn(path, epochs, learning_rate, dims):
    #train dbn on mnist
    data = mnist.load_mnist('../../../mnist_test.csv')
    data = rbm.insert_biases(data)
    dims = [784, 100, 50, 10]
    dbn_weights = generate_dbn_weights(dims)
    dbn_weights = train_dbm(dbm_weights, data, learning_rate = learning_rate, max_epochs = 300)

def load_dbn(path):
    weights = dbn.unpickle(path)
    return weights

def train_rbn(epochs):
    data = load_mnist('../../../mnist_test.csv')
    data = insert_biases(data)
    vis = 784
    hid = 100
    weights = generate_weights(hid, vis)
    weights = train(weights, data, max_epochs = epochs)
    #train on mnist

def load_rbn(path):
    weights = rbm.load_weights(path)
    return weights

def load_small_mnist(path):
    #load a tiny part of mnist
    data = []
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        count = 0
        for line in reader:
            if count >= 100:
                return np.array(data)
            data.append(normalize((np.asarray(line[1:]))))
            count+=1
    return np.array(data)
