Useful points from NOTE1


-Different levels of problems
Easy
• Spell Checking
• Keyword Search
• Finding Synonyms

Medium
• Parsing information from websites, documents, etc.

Hard
• Machine Translation (e.g. Translate Chinese text to English)
• Semantic Analysis (What is the meaning of query statement?)
• Coreference (e.g. What does "he" or "it" refer to given a document?)
• Question Answering (e.g. Answering Jeopardy questions)

-------------
HOW TO Represent words:
1.encode words as vectors 
2.ability to find similarity and difference
3.edit distance algorithm related

Essential idea of word vector encoding:
Passibly there might exist N Space(N Dimension) to encode word meaning, what if we can have some way of fuction approximator etc to approximate the metric as close as possible.
Each dimention is a layer of understanding, or parameter encoding.
-------------------------------
Side DISCOVERY:
I did not learn tense to learn (future vs present).
I learn things for what it is, not what it is called.
But I can later mapping the called(reference) to what it is.
So the efficiency of human commnication would increase.
---------------------------------
One-hot vector representation:

-Denotational sematics: sparse-local representation?
-Distributional sematics: context based understanding of words, dense matrix and better capture of similarity.

Jargon:
word embedding = word vectors
sematic = understading of words
syntactic = sentence related naming, structure of the sentence
-----------------
SVD based method:

disadvantage:
	SVD based methods do not scale well for big matrices and it is hard to incorporate new words or documents. And word sizes frequently changes.
	Computational cost for a m × n matrix is O(mn^2)

----------------------------------------------------------------------
Word2vec: iteration based methods:
  General Idea: 
    Instead of global storage of info, create a model to learn the probability of word given context iteratively.
  In the notes, it talks somehow related to reinforcement learning.


--------
The context of words:
   The set of m surrounding words.

- 2 algorithms: 
    continuous bag-of-words (CBOW):
      ->predict a center word from the surrounding context in\
 terms of word vectors
    skip-gram:
      ->predicts the distribution (probability) of context words from a center word.

- 2 training methods: 

    Negative sampling:
      ->defines an objective by sampling negative exam- ples,
    hierarchical softmax:
      ->defines an objective using an efficient tree structure to compute probabilities for all the vocabulary.

Language Models

1.First model the probability of the whole sentence, it is a valid sentence with good grammar structure and contain meaning.

from unary(independent) model to pair wise probable(bigram) model

OHHHHHHHHHHHHHHHH,
This kind of reminds me of doing quantum information engtangling, however, right now we just try to decouple the correletion of whole system to 2 pair objects.



Useful package:

Gensim: library for unsupervised topic modeling NLP task etc.
  feature: data streaming and incremental online algorithms