# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:39:19 2020

@author: Pablo
"""

import requests

#from elasticsearch import Elasticsearch








def searchDocuments ( query, collection_id, jurisdiction=None, language=None):
    '''
    http://lkg.lynx-project.eu/search?searchPhrase=maternidad&collection=estatuto
    '''
    hed = {
           'charset':'utf-8'
          }
    
    #collection_id='estatuto'
    
    param= 'searchPhrase='+query+'&collection='+collection_id
    
    if jurisdiction != None:
        param=param+'&jurisdiction='+jurisdiction
    if language != None:
        param=param+'&language='+language
        
    
    
    
    url='http://lkg.lynx-project.eu/search?'+param
    
    
    response = requests.get(url, headers=hed)
    #print(response.content)
    #print(response)
    jsonResponse = response.json()
   
    #print(jsonResponse)
    
    docs=[]
    
    for match in jsonResponse['rows']:
        
        docs.append(match)
    
    return docs



def processUPM_doc(doc,fields):
    
    listfields= str(fields.strip()).split('|')
    
    docproc=[]
    for f in listfields:
       
        field_value= doc[f]
        docproc.append(field_value)    
   
    return docproc



'''
def processElastic_doc(doc,fields):
    
    listfields= str(fields.strip()).split('|')
    
    docproc=[]
    for f in listfields:
     
        field_value= doc[f]
        docproc.append(field_value)    
   
    return docproc

def getElasticDoc(ident,index):
    
    es= Elasticsearch()
    res = es.get(index=index,doc_type='doc', id=ident)
    #print(res['_source'])
    return res['_source']



def searchTerm(term,lang):
    
    hed = {
           'charset':'utf-8'
          }

    
    url='https://terminoteca.linkeddata.es/search/?text='+term
    
    response = requests.get(url, headers=hed)
    jsonResponse = response.json()
    
    terms=[]
    
    for match in jsonResponse:
        t1=match['prefLabel'][lang][0].lower() 
        t2=term.lower()
        #print (str(t1)+' '+str(t2))
        if t1 == t2:
            print(term)
            terms.append(match)    
    return terms

'''






    
   
   