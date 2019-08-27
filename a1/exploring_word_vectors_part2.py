from exploring_word_vectors_part1 import *


##############PAR2:Word2Vec################
#Part 2: Prediction-Based Word Vectors

#Then run the following cells to load the 
#word2vec vectors into memory. Note: This might take several minutes.
# ------------------
def load_word2vec():
    """ Load Word2Vec Vectors
        Return:
            wv_from_bin: All 3 million embeddings, each lengh 300
    """
    import gensim.downloader as api
    wv_from_bin = api.load("word2vec-google-news-300")
    vocab = list(wv_from_bin.vocab.keys())
    print("Loaded vocab size %i" % len(vocab))
    return wv_from_bin
# -----------------------------------
# Run Cell to Load Word Vectors
# Note: This may take several minutes
# -----------------------------------
wv_from_bin = load_word2vec()



"""
The following function is aim to 
Reducing dimensionality of Word2Vec Word Embeddings
Let's directly compare the word2vec embeddings to those of the 
co-occurrence matrix. Run the following cells to:

Put the 3 million word2vec vectors into a matrix M
Run reduce_to_k_dim (your Truncated SVD function) to reduce the vectors from 300-dimensional to 2-dimensional.
"""
# ------------------
def get_matrix_of_vectors(wv_from_bin, required_words=['barrels', 'bpd', 'ecuador', 'energy', 'industry', 'kuwait', 'oil', 'output', 'petroleum', 'venezuela']):
    """ Put the word2vec vectors into a matrix M.
        Param:
            wv_from_bin: KeyedVectors object; the 3 million word2vec vectors loaded from file
        Return:
            M: numpy matrix shape (num words, 300) containing the vectors
            word2Ind: dictionary mapping each word to its row number in M
    """
    import random
    words = list(wv_from_bin.vocab.keys())
    print("Shuffling words ...")
    random.shuffle(words)
    words = words[:10000]
    print("Putting %i words into word2Ind and matrix M..." % len(words))
    word2Ind = {}
    M = []
    curInd = 0
    for w in words:
        try:
            M.append(wv_from_bin.word_vec(w))
            word2Ind[w] = curInd
            curInd += 1
        except KeyError:
            continue
    for w in required_words:
        try:
            M.append(wv_from_bin.word_vec(w))
            word2Ind[w] = curInd
            curInd += 1
        except KeyError:
            continue
    M = np.stack(M)
    print("Done.")
    return M, word2Ind
# -----------------------------------------------------------------
# Run Cell to Reduce 300-Dimensinal Word Embeddings to k Dimensions
# Note: This may take several minutes
# -----------------------------------------------------------------
M, word2Ind = get_matrix_of_vectors(wv_from_bin)
M_reduced = reduce_to_k_dim(M, k=2)


"""
Question 2.1: Word2Vec Plot Analysis [written] (4 points)
Run the cell below to plot the 2D word2vec embeddings for ['barrels', 
'bpd', 'ecuador', 'energy', 'industry', 'kuwait', 'oil', 'output', 
'petroleum', 'venezuela'].

What clusters together in 2-dimensional embedding space? What 
doesn't cluster together that you might think should have? How is the 
plot different from the one generated earlier from the co-occurrence
 matrix?
"""

words = ['barrels', 'bpd', 'ecuador', 'energy', 'industry', 'kuwait', 'oil', 'output', 'petroleum', 'venezuela']
plot_embeddings(M_reduced, word2Ind, words)


######Cosine Similarity#########
#Question 2.2: Polysemous Words

# ------------------
# Write your polysemous word exploration code here.

wv_from_bin.most_similar("")

# ------------------














