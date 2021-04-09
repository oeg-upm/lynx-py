# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:12:28 2020

@author: Pablo
"""


import requests
import json
import os
import sys
from elasticsearch import Elasticsearch




def createQuestion(question):
    q= {
      
      "query": {
        "bool": {
          "filter": {
          	"bool" : {
              "must" :  [    		
                {"term": {"metadata.jurisdiction": "es"} }
              ]
            }
          },
          "must": [{
            "multi_match": {
              "query": "\""+question+"\"",
              "fields": [
               "metadata.title.es"
               
              ]
            }
          }   
          
          ]
        }
      }
    }
    return q





def sendQuery(es,collection_id,question):
    
  
    #
    # GET /exp01/doc/_search
   
    
    
    return str(title), str(text)    
    
    


    
if __name__ == "__main__":
   
    collection_id= sys.argv[1]
    print('querying: '+collection_id)
    
    query= sys.argv[2]
    
    
    
    ##  Elastic Default localhost 9200
    es = Elasticsearch()
    
    
    res = es.search(index=collection_id,size=10, doc_type='doc', body=createQuestion(query))
   
    
   
    title="" 
    text=""
    num=0
    for hit in res['hits']['hits']:
        title=hit["_source"]['metadata']['title']['es']
        text= hit["_source"]['text_es']
        if(num==3):
            break
        num=num+1
        print("Title:    "+title)
        print("Text:     "+text)
 
        
        
    
   
    