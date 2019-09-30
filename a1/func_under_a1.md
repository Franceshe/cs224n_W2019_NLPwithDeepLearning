Instead of make all functions in a single file, I split them for testing.

-a1
exploring_word_vectors_part1.py
PART1:
  -distinct_words
   |
   -compute_co_occurrence_matrix
   |
   -reduce_to_k_dim
   |
   -plot_embeddings
   |
   co-Occurrence_plot_analysis

exploring_word_vectors_part2.py
PART2:
   wor2vect
   -load_word2vec
   |
   -get_matrix_of_vectors
   |
   

### Co-Occurrence Matrix:
* To understand such matrix, as the example below:
** Example: Co-Occurrence with Fixed Window of n=1**:

Document 1: "all that glitters is not gold"

Document 2: "all is well that ends well"

|     *    | START | all | that | glitters | is   | not  | gold  | well | ends | END |
|----------|-------|-----|------|----------|------|------|-------|------|------|-----|
| START    | 0     | 2   | 0    | 0        | 0    | 0    | 0     | 0    | 0    | 0   |
| all      | 2     | 0   | 1    | 0        | 1    | 0    | 0     | 0    | 0    | 0   |
| that     | 0     | 1   | 0    | 1        | 0    | 0    | 0     | 1    | 1    | 0   |
| glitters | 0     | 0   | 1    | 0        | 1    | 0    | 0     | 0    | 0    | 0   |
| is       | 0     | 1   | 0    | 1        | 0    | 1    | 0     | 1    | 0    | 0   |
| not      | 0     | 0   | 0    | 0        | 1    | 0    | 1     | 0    | 0    | 0   |
| gold     | 0     | 0   | 0    | 0        | 0    | 1    | 0     | 0    | 0    | 1   |
| well     | 0     | 0   | 1    | 0        | 1    | 0    | 0     | 0    | 1    | 1   |
| ends     | 0     | 0   | 1    | 0        | 0    | 0    | 0     | 1    | 0    | 0   |
| END      | 0     | 0   | 0    | 0        | 0    | 0    | 1     | 1    | 0    | 0   |


* Here The Row and Colown includes all the words in both document.
And we scan the matrix row by row, for example, comparing START TOKEN
with the each entry word in the row matrix, and see if it is in the word's
window. In this case, we have window sizen n =1. Thus the word "all" appeared twice
in Start token's window size
* We build a *co-occurrence matrix* $M$, which is a symmetric word-by-word matrix in which $M_{ij}$ is the number of times $w_j$ appears inside $w_i$'s window.


### DataSet
* Reuters (business and financial news) corpus.
* The corpus consists of 10,788 news documents totaling 1.3 million words.
* These documents span 90 categories and are split into train and test.
* For more details, please see https://www.nltk.org/book/ch02.html.

### DataSet Preprocessing:
* [NLTK howto process categorized corpus](http://www.nltk.org/howto/corpus.html)
* DeLete duplicates words and only preserve disctint words.

