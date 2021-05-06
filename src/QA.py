# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:39:19 2020

@author: Pablo
"""

import requests
from Authorizer import TokenGenarator



TokenGen = TokenGenarator('identifier','password')




url_qa= 'https://qadocenwebapp-lynx.apps.cybly.cloud'


example_data= {
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
}



def questionAnsweringWithDCM(collection,question,ids,tokgen):
    '''
    curl -X GET "https://qadocenwebapp-lynx.apps.cybly.cloud/
    
    collections/laborlaw/question-answering?question=How%20long%20is%20maternity%20leave%3F&ids=testie20%20testie30"
    -H "accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJVazZtbWpOZU1KNmswVnRMQ2w1MUFrZ0FOUXVNQUNGNTRvVzlWZTdWM2hJIn0.eyJleHAiOjE2MjAyOTE3MDgsImlhdCI6MTYyMDI5MTQwOCwiYXV0aF90aW1lIjoxNjIwMjkxNDA4LCJqdGkiOiI4ZjRmZWE5Ni1kMjQwLTQ4MjAtYmNjOS03N2MzNjI1ZjUzNDgiLCJpc3MiOiJodHRwczovL2F1dGgubHlueC1wcm9qZWN0LmV1L2F1dGgvcmVhbG1zL0x5bngiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMzRiMTQwNmItNjBjOS00OTdkLWI5NDMtNjI1ZDhiY2E0NjFkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiU3dhZ2dlclVJIiwic2Vzc2lvbl9zdGF0ZSI6ImUyYzJhYzQxLTZkMjYtNGU0NC1iOGQ5LTQ5MTAzZWM2N2M5NyIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZXZlbG9wZXIiLCJ1bWFfYXV0aG9yaXphdGlvbiIsInVzZXIiXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJQYWJsbyBDYWxsZWphIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicGNhbGxlamEiLCJnaXZlbl9uYW1lIjoiUGFibG8iLCJmYW1pbHlfbmFtZSI6IkNhbGxlamEiLCJlbWFpbCI6InBjYWxsZWphQGZpLnVwbS5lcyJ9.D3VnJErMFPyL7-BCEYi-2-hz4sITyU4mqpH_odZtEFGIZSOPsHbb-ULGMvVLiy7M1NLmg7BGGv7fT9JKrp83qptawgsfTPeS-omSmDVx3x5tH_vRIDrlfuHtdhaSmZ1XKpRUnP3CnVd4pKq62fblstPKKk5CoITvDdhh4PYLj2Owm_SUBxHK82fB3ffv-SF0epzAss9tNDqf9oOsF2WH1NUNgTBeuKtFa1pzp8Y1o_JcocABNBdmi4MfgBIJo9lnJxxhokkQ5Z3OXaVIWEt8ktpHBQNIhzY-Sk_5P2_6P_UV8fUb393FrbmdJVcQyDwfOkMLl6vr7Ko-9I6msTLnDw"
    '''
    
    
    
    
    identifiers = ' '.join(str(e) for e in ids)
    
   
   
    auth_token = TokenGen.getToken()
    
    hed = {
           'accept': 'application/json',
           'Authorization': 'Bearer ' + auth_token, 
           
           'Content-Type':'application/json' 
           
           }
    
   
    url=url_qa+'/collections/'+collection+'/question-answering?question='+question+'&ids='+identifiers
    #url='https://qadocenwebapp-lynx.apps.cybly.cloud/answering'
    
    response = requests.get(url, headers=hed)
    
    res = response.json()

    #print(res['answer'])
    
    return res



def generateTextSegmentsData(question, ListSegments):
    
   data= {
  "question": "How long can maternity leave last?",
  "segments": ListSegments
  }
   
   return data
    
    


def questionAnsweringWithTextSegments(data):
    
    

    hed = {
           'accept': 'application/json',
           
           'Content-Type':'application/json' 
           
           }
    
   
    url=url_qa+'/answering'
    #url='https://qadocenwebapp-lynx.apps.cybly.cloud/answering'
    
    response = requests.post(url, json= data,headers=hed)
    
    res = response.json()

    #print(res['answer'])
    return res


    
'''
 for ide in ids:
        ids_txt=ids_txt+ide+" "
    ids_txt=ids_txt.strip()
    
    param= 'collection='+collection_id+'&ids='+ids_txt+'&question='+query
    print(param)
    url_lkgp_default='https://apis.lynx-project.eu/doc/open-api-3/question-answering/answer?'+ param
    
    response = requests.get(url_lkgp_default, headers=hed)
    print(response.content)
    print(response)




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

    
    
    curl -X POST "https://qadocenwebapp-lynx.apps.cybly.cloud/answering" -H "accept: application/json"
    -H "Content-Type: application/json" -d 
    "{\"question\":\"How long can maternity leave last?\",\"segments\":[{\"paragraph\":\"As a mother, you are entitled to take 26 weeks maternity leave from work while you are having a baby. Your contract of employment will state if your employer will pay you when you are on maternity leave (this is not a requirement). \",\"title\":\"Protective leave\",\"language\":\"es\"},{\"paragraph\":\"An adopting mother or sole male adopter is entitled to 24 weeks’ adoptive leave, beginning on the day the child is placed with them. Employers have no obligation to pay an employee for adoptive leave. You may be entitled to Adoptive Benefit.\",\"title\":\"Adoptive leave\"},{\"paragraph\":\"Parental leave: Each parent is entitled to 2 weeks’ leave during the first year of a child’s life, or in the case of adoption, within one year of the placement of the child with the family. \",\"title\":\"Paternal leave\",\"language\":\"es\"},{\"paragraph\":\"Carer’s leave: You are allowed to take unpaid leave to provide full-time care and attention for a person in need of care. The minimum statutory entitlement is 13 weeks and the maximum is 104 weeks. Generally, you need 12 months’ continuous service with your employer to get carer’s leave. You may be eligible for social welfare payment Paternity Benefit.\",\"title\":\"Carers leave\"}]}"


'''


aaa='ass'

li= ['testie20','testie30']
col='laborlaw'
question='how long maternity leave is?'
questionAnsweringWithDCM(col,question,li,None)





