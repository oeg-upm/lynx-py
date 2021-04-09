# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:39:19 2020

@author: Pablo
"""

import requests

from elasticsearch import Elasticsearch
def questionAnswering(collection_id, query, ids ):
    
    

    hed = {
           'accept': 'application/json'
           }
    
    ids_txt=""
    for ide in ids:
        ids_txt=ids_txt+ide+" "
    ids_txt=ids_txt.strip()
    
    param= 'collection='+collection_id+'&ids='+ids_txt+'&question='+query
    print(param)
    url_lkgp_default='http://qadocenwebapp-88-staging.cloud.itandtel.at/v0/answer?'+ param
    
    response = requests.get(url_lkgp_default, headers=hed)
    print(response.content)
    print(response)



def evaluateTitleString(strin1,strin2):
    title1 = strin1.split(".")[0]
    title2 = strin2.split(".")[0]
    if title1 == title2:
        return True
    return False

def irEvaluation(res,answer,n=3):
    
    title="" 
    text=""
    it=0
    docs=""
    
    
    
    for hit in res['hits']['hits']:
        if n == it:
            break
        it=it+1
        title=hit["_source"]['metadata']['title']['es']
        text= hit["_source"]['text']
        docs=docs+"\n --------------- \n >>> Title:   "+ title+"\n >>> Text:   "+text.replace("\n"," ")
        if evaluateTitleString(title,answer):
            return 'True. Found at '+str(it)
    return 'False. Not found in '+str(it)
        


def createElasticQuery(queryFile,question):
    
    f = open(queryFile+'.txt')
    query = f.read()
    f.close()
    query=query.replace('QUESTION',question)
    
    return query

def preprocessorQuery(Query):
    
    Query= Query.strip()
    Query.replace('?','').replace('¿','')

    return Query




def informationRetrieval(collection_id, query, number =3 ):
    
    
    ElasticQuery= createElasticQuery('queryDocument',query)
    
    ##  Elastic Default localhost 9200
    es = Elasticsearch()
    
    res = es.search(index=collection_id,size=number, body=ElasticQuery)
    
    ids=[]
    
    for hit in res['hits']['hits']:
        ide= hit["_source"]['id']
        ids.append(ide)
        
    return res,ids


def informationRetrievalSearchOpenLaws(collection_id,query, number =3 ):
    '''
    search-controller-v-2
    indexes=laborlaw
    request= {
      "indexes": [
        "laborlaw"
      ],  "maxResults": 10,
      "queryString": "salario AND minimo"
    }

    curl -X POST 
    "https://sear-new-secure-88-staging.cloud.itandtel.at/api/v2/sear/indexes/laborlaw/search" 
    -H "accept: application/json;charset=utf-8" -H "Content-Type: application/json" -d 
    "{ \"indexes\": [ \"laborlaw\" ], \"maxResults\": 10, \"queryString\": \"salario AND minimo\"}"

    Returns
    -------
    None.

    '''
    hed = {
           'accept': 'application/json',
           'charset':'utf-8'
           }
    
    
    bod={
    "indexes": [
    "laborlaw"
    ],  "maxResults": number,
    "queryString": "salario AND minimo"
    }
    
    url='https://sear-new-secure-88-staging.cloud.itandtel.at/api/v2/sear/indexes/'+collection_id+'/search'
    
    response = requests.post(url, headers=hed,json=bod)
    #print(response.content)
    #print(response)
    jsonResponse = response.json()
   
    #print(jsonResponse)
    
    ids=[]
    
    for match in jsonResponse['matches']:
        print(match['lynxId'])
        ids.append(match['lynxId'])
    return None, ids




def informationRetrievalSearchUPM(collection_id,query, jurisdiction, language):
    '''
    http://lkg.lynx-project.eu/search?searchPhrase=maternidad&collection=estatuto
    '''
    hed = {
           'charset':'utf-8'
          }
    
    #collection_id='estatuto'
    
    param= 'searchPhrase='+query+'&collection='+collection_id
    
    url='http://lkg.lynx-project.eu/search?'+param
    print(url)
    response = requests.get(url, headers=hed)
    #print(response.content)
    #print(response)
    jsonResponse = response.json()
   
    #print(jsonResponse)
    
    ids=[]
    
    for match in jsonResponse['rows']:
        
        url= match['resourceurl']
        ids.append(url.replace('res/',''))
        
        
    
    
    return ids





def searchUPM_Doc ( query, collection_id, jurisdiction=None, language=None):
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
        
        print(match)
    
    
    return docs



def processUPM_doc(doc,fields):
    
    listfields= str(fields.strip()).split('|')
    print(listfields)
    docproc=[]
    for f in listfields:
        print(f)
        field_value= doc[f]
        docproc.append(field_value)    
   
    return docproc

def processElastic_doc(doc,fields):
    
    listfields= str(fields.strip()).split('|')
    print(listfields)
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




    
if __name__ == "__main__":
    
    

    ## 1-hago una pregunta por termino
    docsEsp= searchUPM_Doc('baja por maternidad','laborlaw2')

    processedDocs=[]
    for doc in docsEsp:
        processedDocs.append(processUPM_doc(doc,'id|text'))
    

    # 2 - busco el documento 0 en la BBDD
    doc=getElasticDoc(processedDocs[0][0],'laborlaw2')
    
    annotations = processElastic_doc(doc,'annotations')[0]
    
    # 3 - conseguir terminos
    termList=[]
    [termList.append(annot['anchorOf']) for annot in annotations]
    Terminos = set(termList)
    
    
    
    # 4 - buscar en terminologia
    GermanTerms=[]
    for Term in Terminos:
        terminology=searchTerm(Term,'es')
        
        # saco los alemanes
      
        for ter in terminology:
            try:
                ter_de= ter['prefLabel']['de'][0]
                GermanTerms.append(ter_de)
            except:
                pass
        
    
    #5 -
    
    terminosAlemanes= ' '.join(GermanTerms)
    docs= searchUPM_Doc(terminosAlemanes,'laborlaw2')
    processedDocs2=[]
    for doc in docs:
        processedDocs2.append(processUPM_doc(doc,'text'))
        
        
    
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3") 
    ## terminologia de patricia
    

processedDocs=[]
for doc in docsEsp:
    processedDocs.append(processUPM_doc(doc,'text'))
    



embeddingsEs = embed(processedDocs)
embeddingsDE= embed(processedDocs2)


from sklearn.metrics.pairwise import cosine_similarity

# Compute similarities exactly the same as we did before!
similarities = cosine_similarity(embeddingsEs,embeddingsDE)

doc1header=[]
doc2header=[]
[doc1header.append( x[0][0:15]  ) for x in processedDocs];
[doc2header.append( x[0][0:15]) for x in processedDocs2];

pd.set_option('display.max_columns', 500)
pd.set_option('expand_frame_repr', False)
# Turn into a dataframe
d=pd.DataFrame(similarities,
            index=doc2header,
            columns=doc1header)#.style.background_gradient(axis=None)
    
    
   
   