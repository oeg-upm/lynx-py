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
import sys



client_id=''
client_secret=''



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



def setAuth(ClientID, ClientSecret):
    client_id= ClientID
    client_secret = ClientSecret
    

def getToken():
    url_authen='https://auth.lynx-project.eu/auth/realms/Lynx/protocol/openid-connect/token'
    
    grant_type = "client_credentials"
    data = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret
        #"scope": scope
    }
    
    auth_response = requests.post(url_authen, data=data)
    
    # Read token from auth response
    
    auth_response_json = auth_response.json()
    auth_token = auth_response_json["access_token"]    
    return auth_token


def getTokenFromFile():
    f = open("../lkg_populator/credentials/client_id.txt",encoding="utf8")
    client_id=f.read().strip()    
    f = open("../lkg_populator/credentials/client_secret.txt",encoding="utf8")
    client_secret=f.read().strip()
    
    return getToken()







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
    auth_token = getToken()
    hed = {
           'Authorization': 'Bearer ' + auth_token, 
           'accept': 'application/json'
           ,'Content-Type': 'application/ld+json'
           
           }
    return hed







def populateFiles(ListFiles,parameters):
    
    hed= createHeader()
    url_lkgp_default='https://apim-88-staging.cloud.itandtel.at/api/workflows/population/instances?'+ parameters 
    
    print('URL:')
    print(url_lkgp_default)
    counter_processed=0
    
    for f in ListFiles:
        print('Processing  '+f)
        counter_processed=counter_processed +1
        
        # Renew the header 
        if counter_processed==200:
            counter_processed=0
            hed= createHeader()
            
        
        try:
            # Read the json file
            with open(f,encoding="utf8") as json_file:
                    data = json.load(json_file)
            
            
           
            
            # Post         
            response = requests.post(url_lkgp_default, json=data, headers=hed)

            print(response.content)
           
        except Exception as e:
            print("error in:"+f)
            print(e.args)
            continue



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
    
    
    auth_token = getToken()
    hed = {
           'Authorization': 'Bearer ' + auth_token, 
           'accept': 'application/json',
           'Content-Type': 'application/json'
          }
        
    url_lkgp_status='https://apim-88-staging.cloud.itandtel.at/api/workflows/population/instances/'+ wf_id
    
    
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

    
    auth_token = getToken()
    hed = {
           'Authorization': 'Bearer ' + auth_token, 
           'accept': 'application/json',
           'Content-Type': 'application/json'
          }
        
    url_lkgp_status='https://apim-88-staging.cloud.itandtel.at/api/workflows/population/tags/'+ tagID+'/instances-status'
    
    
    
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
    
    auth_token = getToken()
    hed = {
           'Authorization': 'Bearer ' + auth_token
          
          }
        
    url='https://apim-88-staging.cloud.itandtel.at/api/workflows/population/instances?tag='+tagID
   
    print(url)
    response = requests.delete(url, headers=hed)
    print(response)
    print(response.content)
    print(response.text)
    
   








