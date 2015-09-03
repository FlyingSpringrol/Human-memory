from neuron import Neuron

class Layer(object):
    def __init__(self, number, size, learning_rate):
        self.neurons = []
        #assorted variables
        self.size = size
        self.learning_rate = learning_rate
        self.id = 'layer' + str(number)
        self.create_neurons()
    def create_neurons(self):
        for i in range(self.size):
            neuron = Neuron(self.id, i+1, self.learning_rate)
            self.neurons.append(neuron)
    def connect_layer(self, output_layer):
        for this_neuron in self.neurons:
            for other_neuron in output_layer.neurons:
                this_neuron.connect_output(other_neuron)
    def propagate_layer(self):
        for neuron in self.neurons:
            neuron.calculate()
    def backprop(self):
        #deltas is the same length as
        for neuron in self.neurons:
            neuron.backprop() #neuron calculates its connections creates its deltas based on forward Layer
    def adjust(self): #changes biases and weights
        for neuron in self.neurons:
            neuron.adjust()
    def recover(self):
        for neuron in self.neurons:
            neuron.recover()
    def print_info(self):
        for neuron in self.neurons:
            neuron.print_info()
