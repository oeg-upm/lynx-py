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
           'accept': 'application/json'
           ,'Content-Type': 'application/json'
           
           }
    return hed



def createHeader2():
    auth_token = TokenGen.getToken()
    hed = {
           'Authorization': 'Bearer ' + auth_token, 
           'accept': 'application/json'
           ,'Content-Type': 'application/ld+json'
           ,'charset':'utf-8'
           
           }
    return hed

def getListofModels():
    
    header= createHeader()
    
    '''curl -X GET "https://apis.lynx-project.eu/api/summarization/listModels" -H "accept: application/json"'''
    url='https://apis.lynx-project.eu/api/summarization/listModels'
    
    
     
    # Post         
    response = requests.get(url, headers=header)
    print(response.content)
    return response


def summarizeText(modelId,text):
    
    header= createHeader2()
    
    '''curl -X POST "https://apis.lynx-project.eu/api/summarization/summarizeText?models=sds" -H "accept: application/json" -H "Content-Type: application/ld+json" -d "string"'''
    url='https://apis.lynx-project.eu/api/summarization/summarizeText?models='+modelId
    
    
    #data= { 'string': text}
    
    #text = ''+text+''
    data= json.dumps( text )
  

    print(data)
    #encode('utf-8')
    
    # Post         
    response = requests.post(url, data=data, headers=header)
    print(response.content)
    return response





client_id='UPM'
client_secret='61cd67b4-99c1-4219-8b07-ba03024a044e'

doc = '''{
       '@context': 'http://lynx-project.eu/doc/jsonld/lynxdocument.json',

 'id': '6ba6ce14-7c4d-4f27-a0c1-9c057cf21232',
 'metadata': {
 
  'id_local': '20010954',
  'jurisdiction': 'AT',
  'language': 'de',
  
  'title': {'de': 'Sbg. Schutz von Dienstnehmerinnen und Dienstnehmern vor Gefährdungen durch explosionsfähige Atmosphären'},
  'type_document': 'Law',
  'url_consolidated': 'https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20010954&FassungVom=2020-01-01',
  },
 'offset_end': 934,
 'offset_ini': 0,
 'parts': [],
 'text': 'Beachte Diese Rechtsvorschrift gilt in ihrer Fassung vom 31. Dezember 2019 für das Land Salzburg als Verordnung des Bundes, soweit sie „Arbeiterrecht sowie Arbeiter- und Angestelltenschutz, soweit es sich um land- und forstwirtschaftliche Arbeiter und Angestellte handelt“ (Art. 11 Abs. 1 Z 9 B-VG, BGBl. Nr. 1/1930, in der Fassung des Bundesgesetzes BGBl. I Nr. 14/2019) regelt; soweit diese Fassung (allenfalls) den Bestimmungen des Bundes-Verfassungsgesetzes betreffend die Zuständigkeit der Behörden widerspricht, gilt sie als „sinngemäß geändert“ (Art. 151 Abs. 63 Z 4 B-VG). Änderung BGBl. I Nr. 14/2019 (NR: GP XXVI RV 301 AB 463 S. 57. BR: AB 10104 S. 888.) Präambel/Promulgationsklausel Auf Grund der §§ 16 und 29 Abs 1 des Bediensteten-Schutzgesetzes – BSG, LGBl Nr 103/2000, und des § 106 Abs 1 Z 1, 2, 3, 5 und 6 der Salzburger Landarbeitsordnung 1995 – LArbO 1995, LGBl Nr 7/1996, in der geltenden Fassung wird verordnet:',
 'translations': {},
 'type': ['lkg:LynxDocument', 'nif:Context', 'lkg:Legislation']
       }'''


text='true Für Arbeitnehmerinnen und Arbeitnehmer, die als Apothekenleiterinnen bzw. Apothekenleiter oder als andere allgemein berufsberechtigte Apothekerinnen und Apotheker in öffentlichen Apotheken beschäftigt sind, gelten die Bestimmungen dieses Bundesgesetzes mit den folgenden Abweichungen. (2) Für Arbeitnehmerinnen und Arbeitnehmer, in deren Arbeitszeit wegen des Bereitschaftsdienstes der Apotheken'
getListofModels()
summarizeText('german_summ',doc)


