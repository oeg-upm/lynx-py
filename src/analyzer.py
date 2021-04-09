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
import requests
from elasticsearch.client import IndicesClient


def getSettings():
    
    index= sys.argv[2]
    
    # Search GitHub's repositories for requests
    response = requests.get(
        'http://localhost:9200/'+index+'/_settings'
    )
    
    # Inspect some attributes of the `requests` repository
    json_response = response.json()
    #parsed = json.loads(json_response)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    



def getAnalysis():
    
    index= sys.argv[2]
    
    # Search GitHub's repositories for requests
   
    
    
    
    ## Default localhost 9200
    es = Elasticsearch()
    ic=  IndicesClient(es)
    response= ic.analyze(index=index, body={
          "field": "text_es", 
          "text":  "¿Puede ser trabajo de menores?"
         })
    
   
    
   

    
    # Inspect some attributes of the `requests` repository
    #json_response = response.json()
    #parsed = json.loads(json_response)
    print(json.dumps(response, indent=4, sort_keys=True))







    
if __name__ == "__main__":
    
    # type of execution
    conf= sys.argv[1]
    
    if conf == 'analyze':
        getAnalysis()

    if conf == 'settings':
        getSettings()
        

    
    collection_id= sys.argv[1]
    print('querying: '+collection_id)
    
    # type question
    query= sys.argv[2]
    
    
    
    ##  Elastic Default localhost 9200
    es = Elasticsearch()
    
    

    

        
    
   
    