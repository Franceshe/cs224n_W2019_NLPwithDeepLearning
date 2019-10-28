# Assignment 3:

## Part1

###


### Dropout:
* See DL:7.12 Dropout, a regularization technique.
* karpathy gives great explaination of dropout and regularization in general:
...[L1/L2 regularization and Dropout-Linear classification: Support Vector Machine, Softmax](https://cs231n.github.io/neural-networks-2/#reg)
* [Dropout paper](http://www.cs.toronto.edu/~rsalakhu/papers/srivastava14a.pdf)

## Other optimization method:
* SGD
* Momentum
* Adaboost
* Adagrad[DL Sec.8.5.1]
* batch/batchnorm [DL Sec.8.7.1]-> Batch Normalization
* Layer normalization

### Other reference:
* https://cs231n.github.io/
********************************************
# Allen NLP Advice - Coding NLP for research
* Better coding style for NLP and ML in general
## Write code quickly
* Shape comments on tensor
* Comments describing non-obvious logic

## Run experiments, keep track of what you tried
* Keep tracking of experiment: inlcude git SHA, model metric, accuracy and so on.
...Check Allen Institude's open data management tool:- https://github.com/allenai/beaker
* Running experiment under controlled variable setting.
* Use configuration files, or separate scripts to tell the details.

## Analyze model behavior - did it do what you wanted?
* Analyze results - Tensorboard
...Crucial tool for understanding model behavior during training
...There is no better visualizer. If you don’t use this, start now.
● Metrics
○ Loss
○ Accuracy etc.
● Gradients
○ Mean values
○ Std values
○ Actual update values
● Parameters
○ Mean values
○ Std values
● Activations
○ Log problematic activations


* How to design so that result is more understandable?
...Separate data processing that also works on JSON
...Model needs to run without labels / computing loss

#### More production advice
* source control
* code review
* Continuous Integration (+ Build Automation)
...CI: always be merging (into a branch)
...BA: always be running your tests (+ other checks) (this means you have to write tests)
* How to test?
...Prototyping: Test the basic, using 'assert'!
...Production level reusable code: test everything...
* What to test?
...Test your model can train, save, and load
...test that it's computing /backpropagating gradients

### Reusable Components
#### The Right Abstractions
* Things That We Use A Lot
● training a model
● mapping words (or
characters, or labels) to
indexes
● summarizing a sequence of
tensors with a single tensor

* Things That Require a Fair Amount of Code
● training a model
● (some ways of) summarizing a
sequence of tensors with a single
tensor
● some neural network modules

* Things That Have Many Variations
● turning a word (or a character, or a label) into a tensor
● summarizing a sequence of tensors with a single tensor
● transforming a sequence of tensors into a sequence of tensors

* Things that reflect our higher-level thinking
● we'll have some inputs:
○ text, almost certainly
○ tags/labels, often
○ spans, sometimes
● we need some ways of embedding them as
tensors
○ one hot encoding
○ low-dimensional embeddings
● we need some ways of dealing with
sequences of tensors
○ sequence in -> sequence out (e.g. all outputs of an
LSTM)
○ sequence in -> tensor out (e.g. last output of an
LSTM

* AllenNLP is built on PyTorch
...under the covers, every piece of
a model is a torch.nn.Module
and every number is part of a
torch.Tensor