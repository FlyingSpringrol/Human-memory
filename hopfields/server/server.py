from flask import Flask, request, jsonify, Response, send_file #annoying you have to import these files
import sys
from hop import *
import numpy as np
import json
import os
import csv

"""
Notes on flask: interesting that functions are declared below .route, and
appear to not be explicitly called
REST: representational state transfer
Things to learn:
    Template rendering
    HTTP methods
    Returning pages
    Returning objects
Request objects, context object
"""
app = Flask(__name__)
test = {'a': 1, 'b':2}
hop = Hopfield(num_nodes = 784, targets = []) #need to figure out a way to add new inputs to net
inputs = []

def serialize_hop(hop_output): #return as a matrix of states
    answer = dict()
    for idx, row in enumerate(hop_output):
        ref = 'row' + str(idx)
        answer[ref] = row
    return answer
def read_input_json(input): #converts input json to readable numpy array
    read = json.loads(input)
    answer = []
    for row in read:
        for unit in row:
            answer.append(translate_bools(unit['active']))
    return answer

def translate_bools(input):
    if input == True:
        return 1
    else: return -1

def train_hop(inputs):
    hop.reset_hop()
    hop.hebb_train(inputs)

def run_hop(input_array):
    inputs = np.asarray(input_array)
    result = hop.run(inputs) #bad values, just introduced, might ruin this
    return result[1] #return the array

def translate(nump_array):
    arr = np.ndarray.tolist(nump_array)
    return json.dumps(arr)

def reset_hop():
    hop.reset_hop()

def binary(val, threshold):
    if (val > threshold):
        return 1
    else: return -1
vec_bin = np.vectorize(binary)

def load_mnist(path):
    #load mnist data from csv, return the data in numpy arrays
    data = []
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            data.append(vec_bin((np.asarray(line[1:])), 255/2))
    return np.array(data)

def run_mnist(mnist_data):
    hop.reset_hop()
    hop.hebb_train(mnist_data)

def load_mnist():
    mnist = load_mnist('../mnist_exs.csv')
    run_mnist(mnist)

@app.route('/')
def sendFiles():
    return send_file('index.html')

@app.route('/hop_train', methods= ['GET', 'POST'])
def post_response(): #runs all methods under route code?
    if request.method == 'POST':
        read = read_input_json(request.data) #converts to array
        inputs.append(read)
        train_hop(inputs)
        return 'Hop trained'
    else:
        return 'request not read'
@app.route('/hop_reset', methods= ['GET'])
def reset():

    if request.method == 'GET':
        hop.reset_states()
        return 'Hopfield Reset'
    else:
        return 'request not read'

@app.route('/hop_run', methods= ['GET', 'POST'])
def run_response():
    if request.method == 'POST':
        read = read_input_json(request.data)
        result = run_hop(read)
        json = translate(result)
        return json
    else:
        print 'not read'
        return 'request not read'

if __name__ == "__main__":
    app.run()
