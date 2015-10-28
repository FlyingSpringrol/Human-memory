# Human-memory
A repository for computational models of human memory

I'm a beginner! Anyone who is at the similar level who wants to learn about
models for human memory is welcome to participate in this repo.
The goal is ultimately to just learn about the dynamics of connected neurons,
their learning rules, and how our minds work!

I'm also trying to focus on biologically feasible systems.

Projects are implemented in Javascript and Python.

Theory:
Most models of human memory involve categorization and classification, and the equations that achieve this simple traverse an error or fitness surface to find the respective max and min.


WIP(s):
###1) Self organizing map/ Kohonen net (implemented in Javascript):

I would like to explore how neurons could exhibit this kind of activity with
biological constraints. For example, the kohonen net is based on comparative
error, and I'm not sure if neurons would ever be able to do such precise
calculations by only summing dendrite inputs.

Basically a SOM works by creating a field of several different classification populations through competive training. (Note: by populations I mean blobs of similar weight vectors). They're very interesting, and I'm going to try to think of ways in which you could chain a bunch of SOM's and feature extractors together to compute a complex classification problem.
I've read in several places that these are the "ideal model for human memory", but I seriously doubt these nets are the entire story. They might be a PART of human memory, but I think the remarkable type diversity of memory circuits in the brain will surprise us. These nets at best probably just loosely model the classification and categorization modules of our minds.

Just writing this one down... Not sure how this idea is connected to any of these ideas but are a bunch of simple graded "yes/no" responses enough to  match the accuracy of a single backpropagated ideal solution?

###2) Hopfield net:
Buggy! Still occasionally converges to a single/two possible patterns.Which is just not right.  
How to run: 
   Dependencies:  
   1.Flask
   2.Numpy
Download, move to server directory, and run the command 'python hopfield.py'.  
Next, open http://127.0.0.1:5000/  
Next feel free to train and run all the mofocking patterns you want.  

Theory behind Hopfield Nets:
Minimization of an energy function to create content-adressable memory.
Hopfield nets are incredibly interesting as they illustrate a recursive feeding network, that is, its output feeds back into its inputs. I think the saved, incrementally changing states of the net might be a perfect model for biological memory.  
I might have implemented my net wrong, but they work in a different way that I expected. See, I thought if I trained an 'H' for example, the net output would be an 'H', but the net output is actually the stable state that the 'H' was trained to. Why this is a bit disappointing is because you have to directly reference the trained states to pull out an input.
I wonder if recurrent systems have been observed in the brain, and if this recurrence is what allows for memory recall.
http://www.scholarpedia.org/article/Hopfield_network
http://www.cs.toronto.edu/~mackay/itprnn/ps/506.522.pdf
https://www.youtube.com/watch?v=gfPUWwBkXZY

###3)Python Neural net:
Object oriented approach to implementing a neural net. (Python)
Shit is slooooow.

###4) Markov Chains:

While not immediately relevant to connected and synchronized systems, markov models are easy to implement, and demonstrate the power of MEMORY, that is, using past experiences for computing future possibilities.

These generate text based on the book you feed it. You could potentially feed it information from any text source and it would generate a unique output. If I have time I'd love to add some features that would make the outputs more accurate/ comprehensible.
1)Dual-directional reading?
2)Part of speech identifier?

Project idea:
Webcrawl some sites to obtain current residential candidates speeches and run it through the markov model. It would be cool to see how the output differs in regard to rhetoric and topics.

###5) Deep Belief Networks:
Generative models:
Probabilistic inference networks: infer the relationship between the hidden units that could creates the visible effect.  

Related Concepts:
 :*RBMS (restricted boltzmann machines)
 *Sigmoid Belief Networks
 *Bayesian Networks
 *Autoencoders


deeplearning.net/tutorial/DBN.html
https://www.youtube.com/watch?v=vkb6AWYXZ5I
https://www.cs.toronto.edu/~hinton/nipstutorial/nipstut3.pdf

###6) Other shit to learn:
     Convolutional networks
     Auto-encoder, (standard, variational)
     Recurrent neural nets

###Links to models of biological systems:

MIT initial object recognition in the visual cortex: (full model and implementation details)
http://cbcl.mit.edu/projects/cbcl/publications/ai-publications/2005/AIM-2005-036.pdf

MIT Texture + object recognition:
http://cbcl.mit.edu/cbcl/publications/ps/unifiedC2.pdf

Orientation maps of the visual cortex:
http://www.scholarpedia.org/article/Visual_map#Orientation_Maps

Lateral occipital cortex and its role in object recognition:
http://math.bu.edu/people/horacio/tutorials/jascha_2.pdf

Visual perception of texture: (Something that I think will be incredibly important in the future of effective object segregation and recognition)
http://www.cns.nyu.edu/~msl/papers/landygraham02.pdf

Large scale model of the functioning brain (only the abstract)
http://www.sciencemag.org/content/338/6111/1202.short
