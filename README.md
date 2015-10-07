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

Basically a SOM works by creating a field of several different classification populations (by populations I mean the blobs of similar weight vectors). They're very interesting, and I'm going to try to think of ways in which you could chain a bunch of SOM's and feature extractors together to compute a complex classification problem.
I've read in several places that these are the "ideal model for human memory", but I seriously doubt these nets are the entire story. They might be a PART of human memory, but I think the remarkable type diversity of memory circuits in the brain will surprise us. These nets probably loosely model the classification and categorization modules of our minds.

Just writing this one down... Not sure how this idea is connected yet but are a bunch of simple graded "yes/no" responses enough to  match the accuracy of a single backpropagated ideal solution?

###2) Hopfield net:
I've only just started working on this one, and am still reading about the network dynamics, inputs, outputs, and training. Honestly, I haven't found any really good tutorial links yet.
From my understanding, they are ways of creating associative memory. They can store and retrieve information through an incredible amount of input noise.  
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

I have no idea what these are yet! Wooh! But I'll start writing them soon.
src:
https://www.cs.toronto.edu/~hinton/nipstutorial/nipstut3.pdf

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
