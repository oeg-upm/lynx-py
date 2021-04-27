# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:39:37 2020

@author: Pablo
"""



def nopreprocessing(query):
    return query



def createQuestion(queryFile,question):
    
    f = open(queryFile+'.txt')
    query = f.read()
    f.close()
    query=query.replace('QUESTION',question)
    
    return query