import numpy
import math
import random
import numpy as np
from layer import Layer
""""
Testing neural nets:
    -propagation test
    -back-prop adjusting test (xor) -> (sine) -> (mnist)
        -look for a consistent pattern in trained outputs: training a function
            JUST THE WRONG ONE
        -Erroneous patterns of outputs?:
            -linear relationship between inputs and outputs
            (very evident in sine-training)
        -Watch changes in net: Algorithm for testing backprop:
            -Change learning rate and epoch sizes: see how output pattern changes
            -print weight_gradients
            -programs to check valid delta values?: and if it's decreasing?
    -Write explicit tests for:
        1.connection of layers (architecture)
        2.functional forwards propagation: (function)
        3.Functional backprop (algorithm)

    -Shit that you should hate:
        -Overfitting
        -Local minimums
        -convergence?
"""
def mean_squared(input, target): #the actual error: not the derivative
    return math.pow((target-input), 2)
def der_MSE(input, target):
    return (input-target)
def cross_entropy():
    return a
def sig(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))
def der_sig(z):
    """Derivative of the sigmoid function."""
    return sig(z)*(1-sig(z))

class Network(object):
    def __init__(self, layers, learning_rate, error_function):
        self.layers = []
        self.error_function = error_function #add check code to see
        self.learning_rate = learning_rate
        self.create_layers(layers)
        self.connect_layers()
    #initalization methods
    def create_layers(self, layers):
        for i in range(len(layers)):
            size = layers[i]
            layer = Layer(i, size, self.learning_rate)
            self.layers.append(layer)
    def connect_layers(self):
        for idx,layer in enumerate(self.layers):
            if (idx == len(self.layers)-1):
                #last layer does not connect to anything
                continue
            else: layer.connect_layer(self.layers[idx+1]) #connect layer after
    def propagate_net(self, inputs):
        #format of input? add in break code
        self.set_inputs(inputs)
        [layer.propagate_layer() for layer in self.layers]
    def set_inputs(self, inputs): #sets the activation of input neurons
        input_layer = self.layers[0]
        for i in range(len(inputs)):
            in_neuron = input_layer.neurons[i]
            in_neuron.activation = inputs[i]

    def recover(self): #used to reset all neuron and connection variables, called recursively
        for layer in self.layers:
            layer.recover()

    def backprop(self, error, target):
        #does not inclue propagation
        #error = error function
        start_idx = -1
        output_layer = self.layers[start_idx]
        length = len(self.layers)
        #store outputs
        for idx, neuron in enumerate(output_layer.neurons): #store output error
            delta = error(neuron.state,target[idx]) * der_sig(neuron.activation)
            neuron.delta = delta
        for i in range(length): #find algorithmic number not magic number (1 in this case)
            if (i == 0): #skip output layer
                continue
            else:
                idx = start_idx - i
            layer = self.layers[idx]
            layer.backprop()
            self.adjust()
        #adjust all weights and biases

    def adjust(self):
        for layer in self.layers:
            layer.adjust()
    def train(self, unit):
        for unit in set:
            self.propagate_net(unit[0])
            self.backprop(self.error_function, unit[1])
            self.recover()
    def train_sine(self, iterations):
        #easier to create a set?
        for i in range(iterations):
            ins = [random.random()*math.pi]
            output = [math.sin(ins[0])]
            #output = [.5]
            self.propagate_net(ins)
            self.backprop(self.error_function, output)
            self.recover()

        tests = [0, .2*math.pi, .5*math.pi, .7*math.pi]
        for test in tests:
            self.propagate_net([test])
            self.print_outputs()
            print 'target: ' + str(math.sin(test))
            self.recover()
    def train_xor(self, iters):
        inputs = [[0,1], [0,0], [1,0], [1,1]]
        outputs = [[1], [0], [1], [0]]
        tests = inputs
        print 'pre-training:'
        for test in tests:
            self.propagate_net(test)
            self.print_outputs()
            self.recover()
        #backprop logic
        for i in range(iters):
            idx = random.randint(0,len(inputs)-1)
            self.propagate_net(inputs[idx])
            self.backprop(self.error_function, outputs[idx])
            self.recover()
        print 'post-training:'
        for test in tests:
            self.propagate_net(test)
            self.print_outputs()
            self.recover()
        print outputs


    def batch_prop(self, mini_batch_size):
        a =2

    def read_file(self, filename):
        a = 2

    def test(self, test_set):
        a = 2
    def print_outputs(self):
        output = self.layers[-1]
        for neuron in output.neurons:
            print 'activation:' + str(neuron.state)
def test_xor():
    xor_net = Network([2,3,1], -2, der_MSE)
    xor_net.train_xor(100000)
def test_sine():
    sine_net = Network([1,20,1], -3, der_MSE)
    sine_net.train_sine(10000)
def test_feedforward():
    a = 2

def train_multiple_nets(number, net_parameters):
    nets = []
    for i in range(number):
        #net_parameters = array [layer1size, layer2size]
        net = Network(net_parameters, -3, der_MSE)
        nets.append(net)
    for net in nets:
        net.train_sine(1000)

test_xor()
