
import requests
import json
import os
import sys
from elasticsearch import Elasticsearch
import queryprepocessing





def getDocumentText(es,documentTitle):

    f = open('queryDocument.txt')
    query = f.read()
    f.close()
    query=query.replace('QUESTION',documentTitle)
    
    res = es.search(index=collection_id,size=10, doc_type='doc', body=query)
    text=""
    for hit in res['hits']['hits']:
        #title=hit["_source"]['metadata']['title']['es']
        text= hit["_source"]['text_es']
        break
    return text.replace("\n"," ")


def sendQuery(es,collection_id,question,queryFile):
    
    query= queryprepocessing.createQuestion(queryFile,question)
    res = es.search(index=collection_id,size=10, doc_type='doc', body=query)
    return res    
    
    

def evaluateTitleString(strin1,strin2):
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
        docs=docs+"\n --------------- \n >>> Title:   "+ title+"\n >>> Text:   "+text.replace("\n"," ")
        if evaluateTitleString(title,answer):
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
        GoldDocument= getDocumentText(es,questionparsed[2])
        
        res = sendQuery(es,collection_id, questionparsed[1],queryFile)
        
        passed, docs = evaluation(res,questionparsed[2],N)
        
        
        
        log=log +("\n --------------------------- \n")
        if  passed:
            ok=ok+1
            log=log+ (str(nok+ok)+") ======================  OK")
            log=log + ("\n Query:    "+questionparsed[1])
            log=log + ("\n Gold:     "+questionparsed[2])
            log=log + ("\n GoldDocument:     "+GoldDocument)
            log=log + ("\n Response: "+docs)
        
        else:
            nok=nok+1
            log=log + (str(nok+ok)+") ======================  failed")
            log=log + ("\n Query:    "+questionparsed[1])
            log=log + ("\n Gold:     "+questionparsed[2])
            log=log + ("\n GoldDocument:     "+GoldDocument)
            log=log + ("\n Response: "+docs)
        
    f = open('Res-Index'+collection_id+'-Nprec-'+str(N)+'.txt','w+',encoding="utf8")
    f.write(log)
    f.close()
        
    print('quality: ' + str(ok/total))    
   
    