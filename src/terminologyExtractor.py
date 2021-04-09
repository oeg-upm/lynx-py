#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:45:14 2021

@author: Pablo
"""




import json


with open('/Users/Pablo/Desktop/laborlaw.json') as json_file:
    data = json.load(json_file)
    

    my_list = []
    for hit in data:
        print(hit)
        for term in hit['@graph']:
            
            try:
                for tee in term['http://www.w3.org/2004/02/skos/core#prefLabel']:
                
                    lang= tee['@language']
                    
                    if lang == 'de':
                        
                        ter= tee['@value']
                        
                        print(ter)
                        my_list.append(ter)        
                
            except:   
                pass
         


with open('/Users/Pablo/Desktop/term_de.txt', 'w') as f:
    for item in my_list:
        f.write(item)
        f.write('\n')
        
        
        
        
        
        
"""
Created on Thu Oct  8 11:05:34 2020
@author: pmchozas
"""


import json


preflist_es=[]
altlist_es=[]
preflist_en=[]
altlist_en=[]






with open('/Users/Pablo/Desktop/laborlaw.json') as jsonfile:
    data= json.load(jsonfile)
    for p in data:
        for l in p['@graph']:
            try:
                for i in l['http://www.w3.org/2004/02/skos/core#prefLabel']:
                    if i['@language'] == 'de':
                        preflist_es.append(i['@value'])
                    
            except:
                continue
            try:
                for i in l['http://www.w3.org/2004/02/skos/core#altLabel']:
                    if i['@language'] == 'de':
                        altlist_es.append(i['@value'])
            except:
                continue
        
print(preflist_es)
print(altlist_es)
with open('/Users/Pablo/Desktop/term_de.txt', 'w') as f:
    for item in preflist_es:
        f.write("%s\n" % item)
    for o in altlist_es:
        f.write("%s\n" % o)
        
        
f.close()
