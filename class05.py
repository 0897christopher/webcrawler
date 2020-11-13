# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:13:01 2020

@author: 88690
"""

import requests
import json

data = { "NAME" :'Adolph' , "HEIGHT" :163 , "MALE" :True }
#print( data.text )
jsonData = json.dumps( data )
print( jsonData )

file = open( "id.json" , "w")

json.dump( jsonData , file )
file.close()

file = open( "id.json" , "r" )
jsonData = json.load( file )
print( jsonData )
file.close()