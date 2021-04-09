# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:39:19 2020

@author: Pablo
"""

import requests
from elasticsearch import Elasticsearch
import json
import re




def getLocalConnection():
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

    return es



def getLynxDocs(ElasticResults):
    res=[]
    for doc in ElasticResults:
        #print(doc)
        docSource  = doc['_source']
        res.append(docSource)
    return res

def filterDocsByMetadata(listdocs,field,value):
    
    res=[]
    i=0
    for doc in listdocs:
        print(i)
        i=i+1
        try:
            if doc['metadata'][field] == value:
                res.append(doc)
        except:
            print('failed')
            print(doc)
            continue
            
    return res





def processElastic_doc(doc,fields):
    
    listfields= str(fields.strip()).split('|')
    
    docproc=[]
    for f in listfields:
        print(f)
        field_value= doc[f]
        docproc.append(field_value)    
   
    return docproc


def getElasticDoc(ident,index):
    
    es= Elasticsearch()
    res = es.get(index=index,doc_type='doc', id=ident)
    #print(res['_source'])
    return res['_source']



def sendDocument(doc, es, index_):
    res = es.index(index=index_, id=doc['id'], body=doc,doc_type='doc')
    print(res['result'])
    

def getAllDocumentsFromIndex(es, index):
    # Check index exists
    if not es.indices.exists(index=index):
        print("Index " + index + " not exists")
        exit()
        
    
    doc_type = "doc"
    size = 6000
    body = {}

    # Init scroll by search
    data = es.search(
        index=index,
        doc_type=doc_type,
        scroll='35s',
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
        var2=process_hits(docs,es,data['hits']['hits'])
        var= var+var2
        data = es.scroll(scroll_id=sid, scroll='25s')
        
        # Update the scroll ID
        sid = data['_scroll_id']
        
        # Get the number of results that returned in the last scroll
        scroll_size = len(data['hits']['hits'])
                      
    
    
    print('total_found in collection: '+str(var))
    return docs


    
# Process hits here
def process_hits(docs,es,hits):
    
    for item in hits:
        docs.append(item)        
       
    
    return len(hits) 








### Annotations




def createDictionary(path):
    
        # Using readlines()
    file1 = open(path, 'r')
    lis=[]
    Lines = file1.readlines()
    for L in Lines:
        lis.append(str(L).strip(' ').replace('\n',''))
        #lis.append(str(L).capitalize().strip(' ').replace('\n',''))
        
    return lis


import pandas as pd

def createMultilingualDictionary():
    dictionary= pd.read_csv('terminology.csv')
    dictionary.columns=['id','es','de']
    
    return dictionary




def generate_annotations(iddoc,text, dictionary):
    
   
    annotationList= []
    
    terms= dictionary    
    pos=0

    for term in terms:
        
        
        
        for m in re.finditer(term, text,re.UNICODE):
            # generate annotation
            
            
            annotation={
                "id": iddoc+"#offset_"+str(m.start())+"_"+str(m.end()),
                "type": [
                "nif:OffsetBasedString"
                ,
                "lkg:LynxAnnotation"
                ],
                "referenceContext": iddoc,
                "offset_ini": str(m.start()),
                "offset_end": str(m.end()),
                "anchorOf": term,
                "annotationUnit": [
                {
                "@type": "nif:AnnotationUnit",
                "nif:confidence": {
                "@type": "xsd:double",
                "@value": pos
                }
            
                
                }
                ]
            }
            print('annotation')
            annotationList.append(annotation)
        
        pos=pos+1
    return annotationList






def annotateDocumentDictionary(es,doc,dictionary):

    try:
        iddoc= doc['_source']['id']
        docProc= doc['_source']
        #doc = json.loads(doc)
        lang = docProc['metadata']['language']
        anot = docProc['annotations']
        text = docProc['text']
        annotations=[]
    
    
        annotations =generate_annotations(iddoc,text, dictionary)
        for annote in annotations:
            anot.append(annote)
       
                
        
    except Exception as e:
        print(e.with_traceback())
        print('failed to process: '+iddoc)
        return docProc
        
        pass        
    
    return docProc



def postDocument(doc, es, index_):
    res = es.index(index=index_, id=doc['id'], body=doc,doc_type='doc')
    print(res['result'])


    



def filterDocsByLang(listdocs):
    
    my=[]
    for doc in listdocs:
        #print(doc)
        if doc['_source']['metadata']['language'] == 'de':
            my.append(doc['_source']['text'])
    return my

    

def postDocuments(es,docs,index):
    
    count=0
    for doc in docs:
        print('Posting: '+str(count))
        postDocument(doc,es,index)
        #break
        count= count+1
        
        
def annotateDocumentsDict(es,docs,dictionary):
    
    count=0
    listDocs=[]
    for doc in docs:
        print('annotating: '+str(count))
        count=count+1
        docproc= annotateDocumentDictionary(es, doc,dictionary)
        listDocs.append(docproc)
    return listDocs            
        
        

       







   
   