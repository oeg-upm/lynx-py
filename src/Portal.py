# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:39:19 2020

@author: Pablo
"""

import requests

from elasticsearch import Elasticsearch








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
        
       
    
    print('found '+str(len(docs)))
    return docs



def processUPM_doc(doc,fields):
    
    listfields= str(fields.strip()).split('|')
    
    docproc=[]
    for f in listfields:
       
        field_value= doc[f]
        docproc.append(field_value)    
   
    return docproc

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




    
if __name__ == "__main__":
    
    

    ## 1-hago una pregunta por termino
    docsEsp= searchDocuments('baja por maternidad','laborlaw2')

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
    docs= searchDocuments(terminosAlemanes,'laborlaw2')
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
    
    
   
   