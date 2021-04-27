# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:39:19 2020

@author: Pablo
"""

import requests




def questionAnswering(collection_id, query, ids ):
    
    

    hed = {
           'accept': 'application/json'
           }
    
    ids_txt=""
    for ide in ids:
        ids_txt=ids_txt+ide+" "
    ids_txt=ids_txt.strip()
    
    param= 'collection='+collection_id+'&ids='+ids_txt+'&question='+query
    print(param)
    url_lkgp_default='https://apis.lynx-project.eu/doc/open-api-3/question-answering/answer?'+ param
    
    response = requests.get(url_lkgp_default, headers=hed)
    print(response.content)
    print(response)



    
   
   