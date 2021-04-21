# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:12:28 2020

@author: Pablo
"""


import requests
import json
import os
import sys
from elasticsearch import Elasticsearch
import requests
from elasticsearch.client import IndicesClient




    


def generate_lynxAnnotation(id, word, idTerminology, start, end ):
  annot= {
  'anchorOf': word,
  'annotationUnit': [{'@type': 'nif:AnnotationUnit',
    'nif:confidence': {'@type': 'xsd:double', '@value': str(idTerminology)}}],
  'id': str(id)+'#offset_'+str(start)+'_'+str(end),
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
    
   
    