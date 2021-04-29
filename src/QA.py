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



    
'''
curl -X 'POST' \
  'https://apis.lynx-project.eu/document-platforms/upm-elastic/answering' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJVazZtbWpOZU1KNmswVnRMQ2w1MUFrZ0FOUXVNQUNGNTRvVzlWZTdWM2hJIn0.eyJleHAiOjE2MTk2ODg3MTQsImlhdCI6MTYxOTY4ODQxNCwiYXV0aF90aW1lIjoxNjE5Njg4NDEzLCJqdGkiOiI2NTQ1OWZjMi1kNDRhLTQ2ZDgtOTU0OS1mZmIzYjQ4NGNmOTEiLCJpc3MiOiJodHRwczovL2F1dGgubHlueC1wcm9qZWN0LmV1L2F1dGgvcmVhbG1zL0x5bngiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMzRiMTQwNmItNjBjOS00OTdkLWI5NDMtNjI1ZDhiY2E0NjFkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiU3dhZ2dlclVJIiwic2Vzc2lvbl9zdGF0ZSI6ImJhMmJiNTEyLTc4MWYtNGE1ZS05YjkxLTE3NzQyNWY5YzZiYiIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZXZlbG9wZXIiLCJ1bWFfYXV0aG9yaXphdGlvbiIsInVzZXIiXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJQYWJsbyBDYWxsZWphIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicGNhbGxlamEiLCJnaXZlbl9uYW1lIjoiUGFibG8iLCJmYW1pbHlfbmFtZSI6IkNhbGxlamEiLCJlbWFpbCI6InBjYWxsZWphQGZpLnVwbS5lcyJ9.eQ6GeXtrfF27bPF02k9Q7AJJr8KA2OLuLix04kdZuHv-lBuERaeXyxLNJ4hGZXqSyiT3le2-WIXkFU-rkCSZbhqcP7S_-DIZ2DhlmB5PoAa-cQvO_WSNLdUBvkOp7KS_n3JS6aE01mirMxQhEQl0bm5Q7WdMq8FduBJbVxCJDb0OykO7j47prhNHUuYw6drtRq6UPk9ekMBVPXBipBU5MKDpdCzQ4kCDbXXcnDH1Vx4K727n3ioDsSpawUnCLcYM-D_k5LWQqeaipHh0Bi5-wDvJfMVTbq2AaWR7H-sHBKLEH15_SxQNJ_bf3xBbPotVtYeJTvBKVG1N0yHDjSDlzg' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "How long can maternity leave last?",
  "segments": [
    {
      "paragraph": "PARRAFO SOBRE MATERNIDAD: You are entitled to take 26 weeks maternity leave from work while you are having a baby. Your contract of employment will state if your employer will pay you when you are on maternity leave (this is not a requirement). ",
      "title": "Protective leave",
      "language": "es"
    },
    {
      "paragraph": "PARRAFO SOBRE ADOPCION: An adopting mother or sole male adopter is entitled to 24 weeks’ adoptive leave, beginning on the day the child is placed with them. Employers have no obligation to pay an employee for adoptive leave. You may be entitled to Adoptive Benefit.",
      "title": "Adoptive leave"
    },
    {
      "paragraph": "PARRAFO SOBRE AMBOS PADRES Parental leave: Each parent is entitled to 2 weeks’ leave during the first year of a child’s life, or in the case of adoption, within one year of the placement of the child with the family. ",
      "title": "Paternal leave",
      "language": "es"
    },
    {
      "paragraph": "PARRAFO SOBRE CUIDADO. Carer’s leave: You are allowed to take unpaid leave to provide full-time care and attention for a person in need of care. The minimum statutory entitlement is 13 weeks and the maximum is 104 weeks. Generally, you need 12 months’ continuous service with your employer to get carer’s leave. You may be eligible for social welfare payment Paternity Benefit.",
      "title": "Carers leave"
    }
  ]
}'



'''