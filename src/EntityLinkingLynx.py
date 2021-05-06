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
from Authorizer import TokenGenarator



TokenGen = TokenGenarator('identifier','password')






def createHeader():
    auth_token = TokenGen.getToken()
    hed = {
           'Authorization': 'Bearer ' + auth_token, 
           'accept': 'text/turtle'
           ,'Content-Type': 'application/json',
           'pp-username': 'pcalleja',
           'pp-password': 'PaVKa.32',
           
           }
    return hed



def createParameters():
    parameters=''
    parameters.append('project_id=1E14BF84-57A4-0001-1FAB-1AADDED47C00') 
    parameters.append('&') 
    parameters.append('server_url=https://lynx.poolparty.biz') 
    parameters.append('&') 
    parameters.append('do_disambiguation=true') 
    parameters.append('&') 
    parameters.append('add_labels_and_broaders=true') 
    parameters.append('&') 
    parameters.append('language=en') 

    return parameters
 


def entityLinkingTexts(texts,configuration):
    
    hed= createHeader()
   
    responses=[]
    
    #print('URL:')
    #print(url_lkgp_default)
    counter_processed=0
    
    for text in texts:
        print('Processing  '+str(counter_processed))
        counter_processed=counter_processed +1
        respo=''
        # Renew the header 
        if counter_processed==200:
            counter_processed=0
            hed= createHeader()
            
        
        try:
            
            respo=entityLinkingText(text,hed)
        
           
        except Exception as e:
            print("error in:"+text)
            print(e.args)
            continue
        
        responses.append(respo)

    return responses

def entityLinkingText(text,header):
    if header is None:
        header= createHeader()
    
    parameters= createParameters()
    url='https://apis.lynx-project.eu/api/entity-linking/extract?'+ parameters 
    
    
    data= { 'text': text}
     
    # Post         
    response = requests.post(url, json=data, headers=header)
    print(response.content)
    return response



