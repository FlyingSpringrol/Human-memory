import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from urllib import urlretrieve
import cPickle as pickle
import os
import gzip

import numpy as np
import theano

import lasagne
from lasagne import layers
from lasagne.updates import nesterov_momentum

from nolearn.lasagne import NeuralNet
from nolearn.lasagne import visualize

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def unpickle(file):
    """
    data -- a 10000x3072 numpy array of uint8s. Each row of the array stores a 32x32 colour image.
    32 * 32 = 1024
    1024*3 = 3072
    [0-255]
    The first 1024 entries contain the red channel values, the next 1024 the green, and the final 1024 the blue.
     The image is stored in row-major order, so that the first 32 entries of the array are the red channel
     values of the first row of the image.
     [1024, 1024, 1024]

    labels -- a list of 10000 numbers in the range 0-9. The number at index i indicates the
    label of the ith image in the array data.

    10 classes
    X_train = np.reshape((-1,1,28,28)) -> all the values
    """
    fo = open(file, 'rb')
    dict = pickle.load(fo)
    fo.close()
    return dict

def format_grey(raw_data): #returns greyscale image
    #input = 3072 length ndarray
    red = dat[0:1024]
    green = dat[1024: 2048]
    blue = dat[2048: 3072]
    red = red.astype(float)
    green = green.astype(float)
    blue = blue.astype(float)
    for i in range(1024):
        red[i] = ((red[i] + blue[i] + green[i])/3)/255
        #red holds all the channels
    return red.astype(np.uint8)

def greyscale(cifar):
    grey = np.zeros(10000)
    for idx,x in enumerate(cifar['data']):
        grey[idx] = format_grey(x)
    return grey

def get_cifar(path): #returns (input, output), greyscaled
    cifar = unpickle(path)
    grey = greyscale(cifar)
    input = grey.reshape((-1,1,32,32))
    output = np.asarray(cifar['labels']).astype(np.uint8)
    return (input, output)


def format_multi(dat): #multiple channel data
    return dat.reshape((-1,1,32,32))

x_train, y_train = get_cifar()
x_test, y_test = get_cifar()


single_channel_net = NeuralNet(
    layers=[('input', layers.InputLayer),
            ('conv2d1', layers.Conv2DLayer),
            ('maxpool1', layers.MaxPool2DLayer),
            ('conv2d2', layers.Conv2DLayer),
            ('maxpool2', layers.MaxPool2DLayer),
            ('dropout1', layers.DropoutLayer),
            ('dense', layers.DenseLayer),
            ('dropout2', layers.DropoutLayer),
            ('output', layers.DenseLayer),
            ],
    # input layer
    input_shape=(None, 1, 32, 32),
    # layer conv2d1
    conv2d1_num_filters=32, #32 filters da fuq
    conv2d1_filter_size=(5, 5),
    conv2d1_nonlinearity=lasagne.nonlinearities.rectify,
    conv2d1_W=lasagne.init.GlorotUniform(),
    # layer maxpool1
    maxpool1_pool_size=(2, 2),
    # layer conv2d2
    conv2d2_num_filters=32,
    conv2d2_filter_size=(5, 5),
    conv2d2_nonlinearity=lasagne.nonlinearities.rectify,
    # layer maxpool2
    maxpool2_pool_size=(2, 2),
    # dropout1
    dropout1_p=0.5,
    # dense
    dense_num_units=256,
    dense_nonlinearity=lasagne.nonlinearities.rectify,
    # dropout2
    dropout2_p=0.5,
    # output
    output_nonlinearity=lasagne.nonlinearities.softmax,
    output_num_units=10,
    # optimization method params
    update=nesterov_momentum,
    update_learning_rate=0.01,
    update_momentum=0.9,
    max_epochs=10,
    verbose=1,
    )

# Train the network
nn = single_channel_net.fit(x_train, y_train)
