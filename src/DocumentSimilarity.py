# -*- coding: utf-8 -*-





import ElasticLynx as ely
import dcmLynx as dcm
import Portal as portal



import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


#!pip install tensorflow tensorflow_hub tensorflow_text




#!pip install pandas

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")





def searchSimiliarDocuments(collection_source, id_source, collection_target=None):
    
 
     
    
    
    
    dict_de= ely.createDictionary('terminology/de_terminology.txt')
    dict_es= ely.createDictionary('terminology/es_terminology.txt')
    
    
    
    # Cojo el documento
    
    docIdSource= id_source #'d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_9'
    docSource=portal.getElasticDoc(docIdSource,collection_source)
    
    
    TextSource = docSource['text']

    #print('\n\n\n')
    #print('Text to Search')
    #print(TextSource)
    
    # anotaciones
    numbers= set()
    for annot in docSource['annotations']:
        
        termIndex= annot['annotationUnit'][0]['nif:confidence']['@value']
        numbers.add(termIndex)
    
    
    text=''
    for number in numbers:
        
        text=text+ dict_es[number] + ' '
    
    
    if text == '':
        return 0, 0,0,0
    
    ## 1-hago una pregunta por termino
    docsEsp= portal.searchDocuments(text,collection_target)
    
    
    if len(docsEsp) == 0:
        return 0, 0,0,0
    
    CandidatesDocs=[]
    CandidatesIds=[]
    for doc in docsEsp:
        res= portal.processUPM_doc(doc,'id|text')
        CandidatesDocs.append(res[1])
        CandidatesIds.append(res[0])
        
    
    
    
    embeddingsDocSource= embed(TextSource)
    embeddingsDocsTarget= embed(CandidatesDocs)
    
    
    # Compute similarities exactly the same as we did before!
    similarities = cosine_similarity(embeddingsDocSource,embeddingsDocsTarget)
    
    similarities2= similarities[0,:].tolist()
    
    Score= max(similarities2)
    CandidateId=CandidatesIds[similarities2.index(max(similarities2))]
    CandidateDoc= CandidatesDocs[similarities2.index(max(similarities2))]
    
    #print('\n\n\n')
    #print('\033[94m' +'best similiar document: '+ CandidatesIds[similarities2.index(max(similarities2))] +' '+ str(max(similarities2))  +'\033[0m') 
    #print('\033[94m'+ CandidatesDocs[similarities2.index(max(similarities2))] +'\033[0m')
    
    '''
    # Turn into a dataframe
    df= pd.DataFrame(similarities, index=sentences,
                columns=sentences) \
                .style \
                .background_gradient(axis=None)
                
    '''
    #pd.set_option("display.max_rows", None, "display.max_columns", None)
    #df=pd.DataFrame(similarities, index=[docIdSource], columns=CandidatesIds) #.style.background_gradient(axis=None)
    
    
    
    return Score,TextSource,CandidateId, CandidateDoc 



es= ely.getLocalConnection()



listresults= ely.getAllDocumentsFromIndex(es, 'laborlaw_at')
Comparables=[]
for doc in listresults:
   
    ids= ely.processElastic_doc(doc,'_id')[0]
    print(ids)
    #ids='d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_46'
    Score,TextSource,CandidateId, CandidateDoc =searchSimiliarDocuments('laborlaw_at',ids,'laborlaw2')
    if Score>0.60:
        Comparables.append([Score,ids,CandidateId,TextSource, CandidateDoc])






indice= 'laborlaw_at'




import codecs

file = codecs.open("ComparableDocument.txt", "w", "utf-8")
for line in Comparables:
    file.write(str(line)+'\n')
file.close()





