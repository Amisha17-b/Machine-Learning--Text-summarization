import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import networkx as nx
import numpy as np;


def read_article(filedata):
  """
    Reads an article and preprocesses it by splitting into sentences.

    Args:
        filedata (str): The content of the article.

    Returns:
        list: A list of sentences, where each sentence is represented as a list of words.
    """
  # file = open(file_name)
  # filedata = file.read()

  # split the text into paragraphs
  paragraphs = filedata.split("\n{2,}")

  # split each paragraph into sentences
  sentences = []
  for paragraph in paragraphs:
      # split the paragraph into sentences
      paragraph_sentences = paragraph.split(". ")
      for sentence in paragraph_sentences:
          # remove any non-alphabetic characters and split the sentence into words
          sentences.append(sentence.replace("[^a-zA-Z]"," ").strip().split(" "))
  sentences.pop()
  return sentences

# print(read_article("india.txt"))

def sentence_similarity(sent1,sent2,stopword=None):
  """
    Computes the cosine similarity between two sentences.

    Args:
        sent1 (list): The first sentence.
        sent2 (list): The second sentence.
        stopword (list): List of stopwords to ignore.

    Returns:
        float: Cosine similarity between the two sentences.
    """
  if stopword is None:
    stopwords=[]
  stopwords=[w.lower() for w in sent1]
  stopwords=[w.lower() for w in sent2]
  all_words = list(set(sent1+sent2))

  vector1 = [0] * len(all_words)
  vector2 = [0] * len(all_words)
  for w in sent1:
    if w in stopwords:
      continue
    vector1[all_words.index(w)] +=1
  
  for w in sent2:
    if w in stopwords:
      continue
    vector2[all_words.index(w)] +=1
  return 1-cosine_distance(vector1,vector2)


def gen_sim_matrix(sentences,stop_words):
  """
    Generates a similarity matrix between sentences.

    Args:
        sentences (list): List of sentences.
        stop_words (list): List of stopwords.

    Returns:
        numpy.ndarray: A 2D array representing the similarity matrix.
    """
  similarity_matrix = np.zeros((len(sentences),len(sentences)))
  for idx1 in range(len(sentences)):
    for idx2 in range(len(sentences)):
      if idx1 == idx2:
        continue
      similarity_matrix[idx1][idx2]=sentence_similarity(sentences[idx1],sentences[idx2],stop_words)
  return similarity_matrix


def generate_summary(data,top_n=5):
  """
    Generates a summary of the given data.

    Args:
        data (str): The content of the data.
        top_n (int): Number of sentences to include in the summary.

    Returns:
        str: The generated summary.
    """
  stop_words = stopwords.words('english')
  summarize_text = []
  # sentences = input()
  sentences = read_article(data)
  sentence_similarity_matrix = gen_sim_matrix(sentences,stop_words)
  sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
  scores = nx.pagerank(sentence_similarity_graph)
  ranked_sentences = sorted(((scores[i],s)for i,s in enumerate(sentences)),reverse=True)
  for i in range(min(top_n, len(ranked_sentences))):
    summarize_text.append(" ".join(ranked_sentences[i][1]))
  # print("Summary \n",". ".join(summarize_text)+".")
  return ". ".join(summarize_text)+"."

# generate_summary("india.txt",4)