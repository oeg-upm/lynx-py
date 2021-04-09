# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:39:39 2020

@author: Pablo
"""

import requests
import json
import re
from unicodedata import normalize



queryOriginal= '¿puede ser un contrato verbal de caracter valido?'

from multi_rake import Rake

rake = Rake(
    min_chars=3,
    max_words=3,
    min_freq=1,
    language_code='es'  # 'en'
)



keywords = rake.apply(
    queryOriginal
)

print(keywords)




termSearch="laboral"
lang="es"

term='"'+termSearch+'$"'
lang='"'+lang+'"'
answer=[]
answeruri=''
val=''
try:
    url = ("http://sparql.lynx-project.eu/")
    query = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    SELECT ?c ?label
    WHERE {
    GRAPH <http://sparql.lynx-project.eu/graph/eurovoc> {
    ?c a skos:Concept .
    ?c ?p ?label. 
      FILTER regex(?label, """+term+""", "i" )
      FILTER (lang(?label) = """+lang+""")
      FILTER (?p IN (skos:prefLabel, skos:altLabel ) )
  
    }  
    }
    """
    r=requests.get(url, params={'format': 'json', 'query': query})
    results=json.loads(r.text)
    if (len(results["results"]["bindings"])==0):
        answeruri=''
    else:
        for result in results["results"]["bindings"]:
            answeruri=result["c"]["value"]
            answerl=result["label"]["value"]
            #print(termSearch, answerl)
            if(termSearch.lower() == answerl.lower()):#ATENCION
                
               print(termSearch.lower())
            else:
                tok=answerl.split(' ')
                for i in tok:
                    if('(' in i):
                        tok.remove(i)
                        tokt=term.split(' ')
                        if(len(tok)==len(tokt)):
                            print(tok)
                    elif(termSearch == i):
                        print(tok)
                        
            
except json.decoder.JSONDecodeError:
    answer=[]
    #print('answer', answer, len(answer))   
    #if(len(answer)<1):
    #    answer=uri_term_eurovoc2(termSearch, lang)



### ask to elastic


query1= {
      
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
              "query": "QUESTION", 
              "fields": [
               "metadata.title.es"
               ,
               "text_es"
              ]
              
            }
          }   
          
          ]
        }
      }
}




import requests
import json
import os
import sys
from elasticsearch import Elasticsearch






def createQuestion(queryFile,question):
    
    f = open(queryFile+'.txt')
    query = f.read()
    f.close()
    query=query.replace('QUESTION',question)
    
    return query






def sendQuery(es,collection_id,question,queryFile):
    res = es.search(index=collection_id,size=10, doc_type='doc', body=createQuestion(queryFile,question))
    return res    
    
    

def evaluateString(strin1,strin2):
    title1 = strin1.split(".")[0]
    title2 = strin2.split(".")[0]
    if title1 == title2:
        return True
    return False

def evaluation(res,answer,n):
    
    title="" 
    text=""
    it=0
    docs=""
    
    for hit in res['hits']['hits']:
        if n == it:
            break
        it=it+1
        title=hit["_source"]['metadata']['title']['es']
        text= hit["_source"]['text_es']
        docs=docs+"\n --------------- \n >>> Title:   "+ title+"\n >>> Text:   "+text
        if evaluateString(title,answer):
            return True, docs
    return False,docs
        
        

    
if __name__ == "__main__":
   
    collection_id= sys.argv[1]
    print('Benchmarking: '+collection_id)
    
    N=1
    N= int(sys.argv[2])
    queryFile = "query1"
    queryFile = sys.argv[3]
    
    ## Gold
    f = open("goldstandard.txt",encoding="utf8")
    param=f.read()    
    param=param.strip()
    questions=param.split("\n")
    
    ## Metrics
    total=len(questions)
    ok=0
    nok=0
    
    
    
    ##  Elastic Default localhost 9200
    es = Elasticsearch()
    
    ##
    
    log=""
    
    for question in questions:
        questionparsed= question.split('\t')
        #print(questionparsed)
        res = sendQuery(es,collection_id, questionparsed[1],queryFile)
        
        passed, docs = evaluation(res,questionparsed[2],N)
        
        
        log=log +("\n --------------------------- \n")
        if  passed:
            ok=ok+1
            log=log+ (str(nok+ok)+") ======================  OK")
            log=log + ("\n Query:    "+questionparsed[1])
            log=log + ("\n Gold:     "+questionparsed[2])
            log=log + ("\n Response: "+docs)
        
        else:
            nok=nok+1
            log=log + (str(nok+ok)+") ======================  failed")
            log=log + ("\n Query:    "+questionparsed[1])
            log=log + ("\n Gold:     "+questionparsed[2])
            log=log + ("\n Response: "+docs)
        
    f = open('Res-Index'+collection_id+'-Nprec-'+str(N)+'.txt','w+',encoding="utf8")
    f.write(log)
    f.close()
        
    print('quality: ' + str(ok/total))    
   




