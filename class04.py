# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:32:30 2020

@author: 88690
"""
import re

pattern1 = "windows10 是 windows7 & windows8 & windoes vista & windows xp & windows 98 & windows 95 的後代"
pattern2 = "95 的後代"
result = pattern2 in pattern1
#print( result )

#print( re.search( pattern2 , pattern1 ) )

#print( re.match( pattern2 , pattern1 ) )

#print( re.fullmatch( pattern2 , pattern1 ) )

#print( re.sub( pattern2 , "rrrrrrrrrrrr", pattern1 ) )

string = "電話號碼:0987654321 , angela"
#if re.search( "[\D\d ,]{20}" , string ) != None:
    #print( re.search( "[\D\d ,]{20}" , string ) )
    
if re.search("^(09)[0-9](8)$" , string) != None:
    print( re.search("^(09)[0-9](8)$" , string ))
    