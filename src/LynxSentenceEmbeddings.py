#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:15:54 2021

@author: Pablo
"""

import pandas as pd

sentences = [
    "Molly ate a fish",
    "Jen consumed a carp",
    "I would like to sell you a house",
    "Я пытаюсь купить дачу", # I'm trying to buy a summer home
    "J'aimerais vous louer un grand appartement", # I would like to rent a large apartment to you
    "This is a wonderful investment opportunity",
    "Это прекрасная возможность для инвестиций", # investment opportunity
    "C'est une merveilleuse opportunité d'investissement", # investment opportunity
    "これは素晴らしい投資機会です", # investment opportunity
    "野球はあなたが思うよりも面白いことがあります", # baseball can be more interesting than you think
    "Baseball can be interesting than you'd think"
]


#!pip install tensorflow tensorflow_hub tensorflow_text


import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text


#!pip install pandas

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")

embeddings = embed(sentences)
from sklearn.metrics.pairwise import cosine_similarity

# Compute similarities exactly the same as we did before!
similarities = cosine_similarity(embeddings)

# Turn into a dataframe
df= pd.DataFrame(similarities,
            index=sentences,
            columns=sentences) \
            .style \
            .background_gradient(axis=None)
            

pd.set_option("display.max_rows", None, "display.max_columns", None)
df=pd.DataFrame(similarities, index=sentences, columns=sentences) #.style.background_gradient(axis=None)



from elasticsearch import Elasticsearch
import json


def getAllDocumentsFromIndex(es, index):
    # Check index exists
    if not es.indices.exists(index=index):
        print("Index " + index + " not exists")
        exit()
        
    index = index
    doc_type = "doc"
    size = 6000
    body = {}

    # Init scroll by search
    data = es.search(
        index=index,
        doc_type=doc_type,
        scroll='25s',
        #params = {'from': 9000},
        size=size,
        body=body
    )

    # Get the scroll ID
    sid = data['_scroll_id']
    scroll_size = len(data['hits']['hits'])
    var=0
    docs =[]    
    while scroll_size > 0:
        "Scrolling..."
        
           # Before scroll, process current batch of hits
        var=process_hits(var,docs,es,data['hits']['hits'])
        
        data = es.scroll(scroll_id=sid, scroll='25s')
        
        # Update the scroll ID
        sid = data['_scroll_id']
        
        # Get the number of results that returned in the last scroll
        scroll_size = len(data['hits']['hits'])
                      
    
    return docs
    
# Process hits here
def process_hits(var,docs,es,hits):
    
    for item in hits:
        docs.append(item['_source']['text'].replace('\n',' '))        
        var=var+1
        print(var)
    return var    



# Define config
host = "127.0.0.1"
port = 9200
timeout = 1000



# Init Elasticsearch instance
es = Elasticsearch(
    [
        {
            'host': host,
            'port': port
        }
    ],
    timeout=timeout
)


listdocs= getAllDocumentsFromIndex(es,'laborlaw')


len(listdocs)

with open("docs.txt", "w") as fout:
    for sentence in listdocs:
        print(sentence, file=fout)
    fout.close()
    
    
print('sss')

embeddings = embed(listdocs)
from sklearn.metrics.pairwise import cosine_similarity

# Compute similarities exactly the same as we did before!
similarities = cosine_similarity(embeddings)





