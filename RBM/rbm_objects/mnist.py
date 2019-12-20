from rbm import *
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def load_mnist(path):
    #load mnist data from csv, return the data in numpy arrays
    data = []
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            data.append(normalize((np.asarray(line[1:]))))
    return np.array(data)


def convert(x):
    return int(x)/255.0
normalize = np.vectorize(convert)

def visualize(number):
    #input = size of square letter + 1 bias unit
    number = number[1:]
    number = number.reshape(28,28)
    fig = plt.figure()
    imgplot = plt.imshow(number)
    plt.show()


if __name__ == "__main__":
    data = load_mnist('../../mnist_test.csv')
    data = insert_biases(data)
    vis = 784
    hid = 100
    weights = generate_weights(hid, vis)
    weights = train(weights, data, max_epochs = 400)
    print data.shape
    visualize(data[0])
