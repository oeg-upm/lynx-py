# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:12:28 2020

@author: Pablo
"""


import requests
import json





    


def generate_lynxAnnotation(id, word, idTerminology, start, end ):
  annot= {
  'anchorOf': word,
  'annotationUnit': [{'@type': 'nif:AnnotationUnit',
    'nif:confidence': {'@type': 'xsd:double', '@value': '10.0'}}],
  'id': str(idTerminology),#str(id)+'#offset_'+str(start)+'_'+str(end),
  'offset_end': start,
  'offset_ini': end,
  'referenceContext': str(id) ,
  'type': ['nif:OffsetBasedString', 'lkg:LynxAnnotation']
  
  }
  return annot
    

def generate_lynxAnnotations(document, annotations ):

  Lynx_annot=[]
  for annot in annotations:
    #(1041, 1046, 'Organ', 'http://lynx-project.eu/kos/LT6003113')
    a = generate_lynxAnnotation(document['id'], annot[2], annot[3], annot[0],annot[1])
    Lynx_annot.append(a)

  document['annotations']= Lynx_annot
  return document      
    
   



def create_Lynx_doc(Id, Title, Text, Lang, Jurisdict = 'En', PartOf= None):
    data = {}
    data["@context"]= "http://lynx-project.eu/doc/jsonld/lynxdocument.json"
    data["id"]= Id
    data["type"]= []
    data["type"].append("lkg:Legislation")
    data["type"].append("nif:Context")
    data["type"].append("lkg:LynxDocument")
    data["metadata"]={}
    data["metadata"]["title"]={}
    data["metadata"]["title"][Lang]= Title
    data["metadata"]["language"]=Lang
    
    data["metadata"]["jurisdiction"]=Jurisdict
    if PartOf != None:
        data["metadata"]["lkg:partOf"]=PartOf
    data["text"]= Text
    data["offset_ini"]= 0
    data["offset_end"]= len(Text)
    return data