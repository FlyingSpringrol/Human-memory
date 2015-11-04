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


def get_cifar(file):
    """
    data -- a 10000x3072 numpy array of uint8s. Each row of the array stores a 32x32 colour image.
    32 * 32 = 1024
    1024*3 = 3072
    [0-255]
    The first 1024 entries contain the red channel values, the next 1024 the green, and the final 1024 the blue.
     The image is stored in row-major order, so that the first 32 entries of the array are the red channel
     values of the first row of the image.
     
    labels -- a list of 10000 numbers in the range 0-9. The number at index i indicates the
    label of the ith image in the array data.

    10 classes
    X_train = np.reshape((-1,1,28,28)) -> all the values
    """
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

def squash(input1,input2,input3):
    #add the uints, divide the uints
    for idx, i in input1:
        input1[idx] = (i + input2[idx] + input3[idx])/3 #average of channels
    return input1


def get_labels(file):
    """
    label_names -- a 10-element list which gives meaningful names to the numeric labels in
    the labels array described above. For example, label_names[0] == "airplane", label_names[1] ==
    "automobile", etc.
    """
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

def format_input_multi(cifar_dict): #format to put through nolearn net
    """
    Output = 3, 32 * 32 arrays for each image
    """
    X_train = np.zeros(10000)
    Y_train = np.zeros(10000)
    for key in cifar_dict:
        X_train[key] = cifar_dict[key].reshape((-1,1,32,32))

def format_input_single(cifar_dict):
    """
    Output = 1 32 * 32 single channel array
    """
    #how to compress values together
    X_train = np.zeros(10000)
    Y_train = np.zeros(10000)
    X_test = np.zeros()
    Y_test = np.zeros()
    for key in cifar_dict:
        image = cifar_dict[key]
        X_train[key] = squash(image[0:1024], image[1024:2048], image[2048:3072]).reshape((32,32))
    return (X_train, y_train, x_test, y_test)


#load up the data
cifar_dict = load("./cifar")
x_Train, y_train, x_test, y_test = format_input_single(cifar_dict)

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
nn = single_channel_net.fit(X_train, y_train)
