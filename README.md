# Human-memory
A repository for computational models of human memory

I'm a beginner! Anyone who is at the similar level who wants to learn about
models for human memory is welcome to participate in this repo.
The goal is ultimately to just learn about the dynamics of connected neurons,
their learning rules, and how our minds work!

I'm also trying to focus on biologically feasible systems.


WIP(s):
###1) Self organizing map/ Kohonen net (implemented in Javascript):

I would like to explore how neurons could exhibit this kind of activity with
biological constraints. For example, the kohonen net is based on comparative
error, and I'm not sure if neurons would ever be able to do such precise
calculations by only summing dendrite inputs.

It would be cool to get some more data and explore the categorization power of SOMs.

###2) Hopfield net(implemented in python):
I've only just started working on this one, and am still reading about the network dynamics, inputs, outputs, and training. Honestly, I haven't found any good links yet.

###3)Python Neural net:
 Currently has a training problem (probably an indexing bug). Training a xor takes about 10000 iterations, which shouldn't happen.


###4) Markov Chains:

While not immediately relevant to connected and synchronized systems, markov models are easy to implement, and demonstrate the power of MEMORY, that is, using past experiences for computing future possibilities. (By storing words)

###Links to models of biological systems:

MIT initial object recognition: (full model and implementation details)
http://cbcl.mit.edu/projects/cbcl/publications/ai-publications/2005/AIM-2005-036.pdf

Orientation maps of the visual cortex:
http://www.scholarpedia.org/article/Visual_map#Orientation_Maps

Lateral occipital cortex and its role in object recognition:
http://math.bu.edu/people/horacio/tutorials/jascha_2.pdf

Visual perception of texture: (Something that I think will be incredibly important in the future of effective object segregation and recognition)
http://www.cns.nyu.edu/~msl/papers/landygraham02.pdf

Large scale model of the functioning brain (only the abstract)
http://www.sciencemag.org/content/338/6111/1202.short
