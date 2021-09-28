import nltk
from nltk.metrics import scores
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
def read_article(file_name):
    file = open(file_name,"r")
    filedata=file.readlines()
    article = filedata[0].split(". ")
    sentences=[]
    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z"," ").split(" "))
    sentences.pop()
    return sentences
def sentence_similiarity(sent1,sent2,stopwords=None):
    if stopwords is None:
        stopwords=[]
    sent1=[w.lower() for w in sent1]
    sent2=[w.lower() for w in sent2]
    all_words=list(set(sent1+sent2)) 

    vector1=[0]*len(all_words)
    vector2=[0]*len(all_words)
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] +=1
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)]+=1
    return 1-cosine_distance(vector1,vector2)
def gen_sim_matrix(sentences,stop_words):
    similiarity_matrix=np.zeros((len(sentences),len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1==idx2:
                continue
            similiarity_matrix[idx1][idx2]=sentence_similiarity(sentences[idx1],sentences[idx2],stop_words)
    return similiarity_matrix
def generate_summary(file_name,top_n=5):
    stop_words=stopwords.words('english') 
    summmarize_text=[]
    sentences=read_article(file_name)
    sentence_similiarity_matrix=gen_sim_matrix(sentences,stop_words)
    sentence_similiarity_graph=nx.from_numpy_array(sentence_similiarity_matrix)
    scores=nx.pagerank(sentence_similiarity_graph)
    ranked_sentence=sorted(((scores[i],s)for i,s in enumerate(sentences)),reverse=True)
    for i in range(top_n):
        summmarize_text.append(" ".join(ranked_sentence[i][1]))
    print("summary \n",". ".join(summmarize_text))
generate_summary("mrft.txt", 2)        


