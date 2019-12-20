from flask import Flask, request, jsonify, Response, send_file #annoying you have to import these files
import sys
from hop import *
import numpy as np
import json
import os
import csv

app = Flask(__name__)
hop = Hopfield(num_nodes = 784) #need to figure out a way to add new inputs to net
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


def binary(val, threshold):
    if (val > threshold):
        return 1
    else: return -1
vec_bin = np.vectorize(binary)

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
    inputs.clear()
    hop.reset_hop()
    return 'Reset Net'

@app.route('/hop_run', methods= ['GET', 'POST'])
def run_response():
    if request.method == 'POST':
        read = read_input_json(request.data)
        result = run_hop(read)
        json = translate(result)
        return json
    else:
        print('not read')
        return 'request not read'

if __name__ == "__main__":
    app.run()
