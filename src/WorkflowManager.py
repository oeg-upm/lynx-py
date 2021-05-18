#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:34:44 2021

@author: Pablo
"""




import requests
import json
import os
import requests.exceptions
from Authorizer import TokenGenarator



TokenGen = TokenGenarator('identifier','password')



'''


enTranslationModelId=smt-4eafabb9-7cd6-4ae6-9dd6-6b7cc68925bb
NERModelId=BERTNER_ES

enTranslationModelId=smt-4eafabb9-7cd6-4ae6-9dd6-6b7cc68925bb



collectionId=cctest1
indexDocument=true
documentPlatform=upm-elastic
priority=2056
tag=cctest1
logAnnotationRequests=true



collectionId=wftesten
indexDocument=true
documentPlatform=upm-elastic
entityLinkingProjectId=1E14BF84-57A4-0001-1FAB-1AADDED47C00
deTranslationModelId=smt-99b2f71a-1b3b-418e-bd6b-125f61a53feb
NERModelId=ner-wikinerEn_PER;ner-wikinerEn_LOC;ner-wikinerEn_ORG
GEOModelId=ner-wikinerEn_LOC
prioritize=true











'''






def readWFParametersFile(filePath):
    
    f = open("wf-parameters.txt",encoding="utf8")
    param=f.read()    
    param= parseWFParamaters(param)
    return param


def parseWFParamaters(text):
    text=text.strip()
    text=text.replace('\n','&')
    text=text.replace(';','%3B') # %3B
    return text


def createHeader():
    auth_token = TokenGen.getToken()
    hed = {
           'Authorization': 'Bearer ' + auth_token, 
           'accept': 'application/json'
           ,'Content-Type': 'application/ld+json'
           
           }
    return hed



def readLynxDocuments(ListFiles):
    
    counter_processed=0
    lynxdocs=[]
    
    for f in ListFiles:
        print('Processing  '+str(counter_processed))
        counter_processed=counter_processed +1
        
       
        
        try:
            # Read the json file
            with open(f,encoding="utf8") as json_file:
                    data = json.load(json_file)
                    lynxdocs.append(data)
            
       
           
        except Exception as e:
            print("error in:"+f)
            print(e.args)
            continue

    return lynxdocs


def postInstances(lynxdocuments,parameters):
    
    hed= createHeader()
    url_lkgp_default='https://apis.lynx-project.eu/api/workflows/population/instances?'+ parameters 
    
    print('URL:')
    print(url_lkgp_default)
    counter_processed=0
    
    for lynxdoc in lynxdocuments:
        print('Processing  '+str(counter_processed))
        counter_processed=counter_processed +1
        
        # Renew the header 
        if counter_processed==200:
            counter_processed=0
            hed= createHeader()
            
        
        try:
           
            # Post         
            response = requests.post(url_lkgp_default, json=lynxdoc, headers=hed)

            print(response)
            print(response.json())
           
        except Exception as e:
            print("error in:"+lynxdoc)
            print(e.args)
            continue

def postInstance(lynxdocument,parameters):
    
    hed= createHeader()
    url_lkgp_default='https://apis.lynx-project.eu/api/workflows/population/instances?'+ parameters 
    
    print('URL:')
    print(url_lkgp_default)
    
    
    response = requests.post(url_lkgp_default, json=lynxdocument, headers=hed)

    print(response)
    print(response.json())
           
   


def getFiles(path, init,limit):
    files = []
    
    pointer=0
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if (pointer>=int(init)) and (pointer<int(limit)):
                files.append(os.path.join(r, file))
               
            pointer=pointer+1;

    return files     





def getStatusByWfId(wf_id):
    
    """Check the status of the workflow instance by its ID

    Parameters:
    argument1 (string): ID

    Returns:
    status

   """
    
    
    auth_token = TokenGen.getToken()
    hed = {
           'Authorization': 'Bearer ' + auth_token, 
           'accept': 'application/json',
           'Content-Type': 'application/json'
          }
        
    url_lkgp_status='https://apis.lynx-project.eu/api/workflows/population/instances/'+ wf_id
    
    
    response = requests.get(url_lkgp_status, headers=hed)
    print(response)
    print(response.json())  
    


def getStatusByTAG(tagID):
    
    """Check the status of  workflow instanceS by its TAG ID

    Parameters:
    argument1 (string): ID

    Returns:
    status

   """

    
    auth_token = TokenGen.getToken()
    hed = {
           'Authorization': 'Bearer ' + auth_token, 
           'accept': 'application/json',
           'Content-Type': 'application/json'
          }
        
    url_lkgp_status='https://apis.lynx-project.eu/api/workflows/population/tags/'+ tagID+'/instances-status'
    
    
    
    response = requests.get(url_lkgp_status, headers=hed)
    
    res= response.json()
    print(res)
    
    print('*** Failed')
    for failed in res['failedInstances']:
        wf_id= failed
        print(wf_id)
        getStatusByWfId(wf_id)
    print('*** active')    
    for act in res['activeInstances']:
        wf_id= act
        print(wf_id)
        getStatusByWfId(wf_id)


def deleteByTag(tagID):
    
    """Delete workflow instanceS by its TAG ID

    Parameters:
    argument1 (string): ID

    Returns:
    status

   """
    
    auth_token = TokenGen.getToken()
    hed = {
           'Authorization': 'Bearer ' + auth_token
          
          }
        
    url='https://apim-88-staging.cloud.itandtel.at/api/workflows/population/instances?tag='+tagID
   
    print(url)
    response = requests.delete(url, headers=hed)
    print(response)
    
    
   






'''

import LynxDoc as lkg
doc = lkg.create_Lynx_doc('1', 'prueba', 'prueba', 'en', Jurisdict = 'ES')

doc

client = 'UPM'
password= '61cd67b4-99c1-4219-8b07-ba03024a044e'
TokenGen= TokenGenarator(client, password)

lynxdocuments=[doc]
parameters2  ---  collectionId=collection_review
indexDocument=collection_review
indexId=collection_review
documentPlatform=upm-elastic
priority=2056
tag=collection_review--
populateFiles(lynxdocuments,parseWFParamaters(parameters2))
'''

