from flask import Flask, request, jsonify, Response, send_file #annoying you have to import these files
import sys
from hopfield import *
import numpy as np
import json
import os

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
hop = Hopfield(100, []) #need to figure out a way to add new inputs to net

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

def train_hop(input_array):
    target = np.asarray(input_array)
    hop.add_target(target)

def run_hop(input_array):
    input = np.asarray(input_array)
    result = hop.test(input, 1) #bad values, just introduced, might ruin this
    return result
def translate(nump_array):
    arr = np.ndarray.tolist(nump_array)
    return json.dumps(arr)
def reset_hop():
    hop.reset()

@app.route('/')
def sendFiles():
    return send_file('index.html')

@app.route('/hop_train', methods= ['GET', 'POST'])
def post_response(): #runs all methods under route code?
    if request.method == 'POST':
        read = read_input_json(request.data) #converts to array
        train_hop(read)
        return 'Hop trained'
    else:
        return 'request not read'
@app.route('/hop_reset', methods= ['GET'])
def reset():

    if request.method == 'GET':
        reset_hop()
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
