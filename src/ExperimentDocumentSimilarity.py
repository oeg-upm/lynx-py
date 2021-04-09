# -*- coding: utf-8 -*-





import ElasticLynx as ely
import dcmLynx as dcm
import Portal as portal












## 1- Preprocesar los datos de Christian e incluirlos en nuestro DCM

'''
files =dcm.readJsonFiles('/Users/Pablo/Documents/oeg/proyectos/Lynx/projects/pylynx/text/labourlaw_at')

files=dcm.filterFiles(files)

for f in files:
    #writeJsonFiles(f['@id'].split('documents/')[1],f['text'])
    dcm.dcmPostDocument('laborlaw_at',f)
    
'''

### 2- Anotar los documentos con la terminologia
 

es= ely.getLocalConnection()

dict_de= ely.createDictionary('terminology/de_terminology.txt')
dict_es= ely.createDictionary('terminology/es_terminology.txt')

### Para los datos de Christian

'''
indice= 'laborlaw_at'

listresults= ely.getAllDocumentsFromIndex(es, indice)

docs = ely.annotateDocumentsDict(es,listresults,dict_de)

ely.postDocuments(es,docs,indice)


'''
### Para los de Español



#!pip uninstall googletrans -y

#!pip install googletrans==2.4.0

#!!pip install google_trans_new

'''
#Traducción
from googletrans import Translator

#translator = Translator()
from google_trans_new import google_translator
translator = google_translator()  
dict_es=[]
for term in dict_de:
    
    res= translator.translate(term,lang_src='de',lang_tgt='es')
    dict_es.append(res)
'''


    

'''

indice= 'laborlaw2'

listresults= ely.getAllDocumentsFromIndex(es, indice)

docs = ely.annotateDocumentsDict(es,listresults,dict_es)

ely.postDocuments(es,docs,indice)

'''


### 3- Dado un documento, recuperar los que tenga cod de término en común 



# Documento : d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_9

'''

"@context": "http://lynx-project.eu/doc/jsonld/lynxdocument.json",
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"type": [
"lkg:LynxDocument"
,
"nif:Context"
,
"lkg:Legislation"
],
"text": "Artikel 7 (1) Wird ein Dienstnehmer, der im Gebiet eines Vertragsstaates von einem Unternehmen beschäftigt wird, von diesem Unternehmen zur Ausführung einer Arbeit für dessen Rechnung in das Gebiet des anderen Vertragsstaates entsendet, so gelten bis zum Ende des 24. Kalendermonats nach dieser Entsendung die Rechtsvorschriften des ersten Vertragsstaates so weiter, als wäre er in dessen Gebiet beschäftigt. (2) Wird ein Dienstnehmer eines Luftfahrunternehmens mit dem Sitz im Gebiet eines Vertragsstaates aus dessen Gebiet in das Gebiet des anderen Vertragsstaates entsendet, so gelten die Rechtsvorschriften des ersten Vertragsstaates so weiter, als wäre er in dessen Gebiet beschäftigt. (3) Für die Besatzung eines Seeschiffes sowie andere nicht nur vorübergehend auf einem Seeschiff beschäftigte Personen gelten die Rechtsvorschriften des Vertragsstaates, dessen Flagge das Schiff führt. Für Erwerbstätige, die gewöhnlich innerhalb der Hoheitsgewässer oder im Hafen eines Vertragsstaates an Bord eines die Flagge des anderen Vertragsstaates führenden Schiffes tätig sind, ohne zur Besatzung dieses Schiffes zu gehören, gelten die Rechtsvorschriften des anderen Vertragsstaates",
"metadata": {
"skos:prefLabel": "Soziale Sicherheit (Spanien)",
"lkg:partOfURI": "/res/d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83",
"lkg:partId": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83#offset_5510_6691",
"created": "2021-03-16",
"jurisdiction": "AT",
"language": "de",
"id_local": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"title": {
"de": "Artikel 7"
},
"lkg:documentFullTitle": "Soziale Sicherheit (Spanien)",
"lkg:partOf": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83"
},
"parts": [ ],
"annotations": [
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_44_50",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "44",
"offset_end": "50",
"anchorOf": "Gebiet",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 170
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_191_197",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "191",
"offset_end": "197",
"anchorOf": "Gebiet",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 170
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_389_395",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "389",
"offset_end": "395",
"anchorOf": "Gebiet",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 170
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_478_484",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "478",
"offset_end": "484",
"anchorOf": "Gebiet",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 170
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_518_524",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "518",
"offset_end": "524",
"anchorOf": "Gebiet",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 170
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_532_538",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "532",
"offset_end": "538",
"anchorOf": "Gebiet",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 170
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_671_677",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "671",
"offset_end": "677",
"anchorOf": "Gebiet",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 170
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_57_64",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "57",
"offset_end": "64",
"anchorOf": "Vertrag",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 178
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_210_217",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "210",
"offset_end": "217",
"anchorOf": "Vertrag",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 178
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_340_347",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "340",
"offset_end": "347",
"anchorOf": "Vertrag",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 178
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_491_498",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "491",
"offset_end": "498",
"anchorOf": "Vertrag",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 178
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_551_558",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "551",
"offset_end": "558",
"anchorOf": "Vertrag",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 178
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_622_629",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "622",
"offset_end": "629",
"anchorOf": "Vertrag",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 178
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_844_851",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "844",
"offset_end": "851",
"anchorOf": "Vertrag",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 178
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_977_984",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "977",
"offset_end": "984",
"anchorOf": "Vertrag",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 178
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_1030_1037",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "1030",
"offset_end": "1037",
"anchorOf": "Vertrag",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 178
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_1166_1173",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "1166",
"offset_end": "1173",
"anchorOf": "Vertrag",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 178
}
}
]
}
,
{
"id": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7#offset_295_305",
"type": [
"nif:OffsetBasedString"
,
"lkg:LynxAnnotation"
],
"referenceContext": "d274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_7",
"offset_ini": "295",
"offset_end": "305",
"anchorOf": "Entsendung",
"annotationUnit": [
{
"@type": "nif:AnnotationUnit",
"nif:confidence": {
"@type": "xsd:double",
"@value": 205
}
}
]
}
],
"offset_ini": 0,
"offset_end": 1181,
"translations": { }
}
'''


# Cojo el documento

docIdSource= 'd274e8fb-4c88-4ad9-a8ec-7a8c9fba9a83_Part_9'
docSource=portal.getElasticDoc(docIdSource,'laborlaw_at')


TextSource = docSource['text']

# anotaciones
numbers= set()
for annot in docSource['annotations']:
    
    termIndex= annot['annotationUnit'][0]['nif:confidence']['@value']
    numbers.add(termIndex)


text=''
for number in numbers:
    
    text=text+ dict_es[number] + ' '


## 1-hago una pregunta por termino
docsEsp= portal.searchDocuments(text,'laborlaw2')


CandidatesDocs=[]
CandidatesIds=[]
for doc in docsEsp:
    res= portal.processUPM_doc(doc,'id|text')
    CandidatesDocs.append(res[1])
    CandidatesIds.append(res[0])
    


    









#!pip install tensorflow tensorflow_hub tensorflow_text


import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

#!pip install pandas

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")



embeddingsDocSource= embed(TextSource)
embeddingsDocsTarget= embed(CandidatesDocs)


# Compute similarities exactly the same as we did before!
similarities = cosine_similarity(embeddingsDocSource,embeddingsDocsTarget)

'''
# Turn into a dataframe
df= pd.DataFrame(similarities, index=sentences,
            columns=sentences) \
            .style \
            .background_gradient(axis=None)
            
'''
pd.set_option("display.max_rows", None, "display.max_columns", None)
df=pd.DataFrame(similarities, index=[docIdSource], columns=CandidatesIds) #.style.background_gradient(axis=None)










