# Human-memory
A repository for computational models of human memory

Projects are implemented in Javascript and Python.


### 1) Self organizing map/ Kohonen net (implemented in Javascript)

About SOMS: 
A self organizing map works by creating a field of several different classification populations through competive training. 

Run instructions: Open `index.html`


### 2) Hopfield net

About Hopfield Nets:
Finds the local minimums in a global energy function through activity-correlation. When fully trained, this allows for content-adressable memory.

Run Instructions:
Move to server directory, and run the command `python server.py`.  
Next, open `http://127.0.0.1:5000/`

### 3) Restricted Boltzman Machines
Includes the RBM:
Most of the credit for this code goes to Edwin Chen, I simply extended it to work in a 2D visual environment.

[Edwin Chen Tutorial link] (https://github.com/echen/restricted-boltzmann-machines)


### 4) Models to implement
* Spiking neuron models
* Sparse encoding (see Numenta)
* Reinforcement learning models
* Neural networks with backprop
* Convolutional neural networks
