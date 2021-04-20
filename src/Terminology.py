# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:12:28 2020

@author: Pablo
"""


import requests
import json
import os
import sys
import re

class Terminology():

    Terms=[]
      
    # parameterized constructor
    def __init__(self,terminology_path):
        with open(terminology_path) as json_file:
          data = json.load(json_file)
          data[0]
          for p in data[0]['@graph']:
              #print('id: ' + p['@id'])

              try:
                prefLabels = p['http://www.w3.org/2004/02/skos/core#prefLabel']

                labels={}
                for pref in prefLabels:
                  labels[pref['@language']]= pref['@value']
                  
                term= Term(p['@id'],labels)
                self.Terms.append(term)
              except:
                continue
      
    def annotateText(self,text, lang):

      annotations=[]
      for term in self.Terms:
        id= term.id
        try: ## just in case there is no key
          word = term.PrefLabels[lang]
          matches = re.finditer(word, text)
          
          for m in matches:
            tup= (m.start(), m.end(), word, id)
            annotations.append(tup)
          
        except:
          continue

      return annotations

    def calculate(self):
      return 'holi'        

    def find(self, ids):
      for term in self.Terms:
        if term.id == ids:
          return term
      return -1

class Term():

  def __init__(self, id, prefLabels):
        self.id=id
        self.PrefLabels = prefLabels
        


        
    
   
    