# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:13:02 2020

@author: 88690
"""
import json
import requests
data = requests.get( "https://www.dcard.tw/service/api/v2/forums/pet/posts?limit=30&before=234782450" )

pythonData = json.loads( data.text )

resultList = []
for dictionary in pythonData:
    topics = dictionary[ "topics" ]
    title = dictionary[ "title" ]
    gender = dictionary[ "gender" ]
    #school = dictionary[ "school" ]
    resultDict = { "gender" :gender , "topics" :topics , "title" :title }
    resultList.append( resultDict )
    mediaMeta = dictionary[ "mediaMeta" ]
    #print( mediaMeta )
    for picture in mediaMeta:
        url = picture[ "thumbnail" ]
        print( url )
        data = requests.get( url )
        
        file = open( dictionary[ "title" ] + ".jpg" , "wb" )
        file.write(data.content)
        file.close()
file = open( "result.json" , "w" , encoding = "utf-8" )
file.write( str(resultList) )

file.close()
