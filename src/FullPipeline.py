# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:39:19 2020

@author: Pablo
"""

import requests

from elasticsearch import Elasticsearch



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





def searchUPM_Doc(collection_id, query, jurisdiction=None, language=None):
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
    
    ids=[]
    
    for match in jsonResponse['rows']:
        
        url= match['resourceurl']
        ids.append(url.replace('res/',''))
        
        
    
    
    return ids




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


    
if __name__ == "__main__":
   
    
    Query="¿Cuál es el marco legal al que están sujetas las relaciones laborales de carácter especial?"
    Index= 'estatuto'
    
    GoldDocument="Artículo 2. Relaciones laborales de carácter especial"
    
    DM='UPM'
    
    print('Query: '+Query )
   
    ## P1
   
    QueryProcessed= preprocessorQuery(Query)
    print('Processed query:'+QueryProcessed)    
    
    # P2
    
    
    # P3
    #, idDocs = informationRetrieval('estatuto',QueryProcessed)
    
    #EJECUTAR DE FOMRA AISLADA
    
    idDocs = informationRetrievalSearchOpenLaws('estatuto',QueryProcessed)
    
    
    idDocs = informationRetrievalSearchUPM('estatuto',QueryProcessed, None,None)


    print(idDocs)
    
    # P4
    #print('IR Eval: '+irEvaluation(docs, GoldDocument))
    
    
    # P5
    questionAnswering('estatuto', Query, idDocs )




    