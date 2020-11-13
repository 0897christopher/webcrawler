# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:08:22 2020

@author: 88690
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.books.com.tw/"
data = requests.get(url)
soup = BeautifulSoup( data.text , "html.parser" )

print( soup.prettify() )
#print( soup.title )
#print( soup.title.string )

#print( soup.body )

#print( soup.div.attrs )
#print( soup.get_text() )
"""
a_element = soup.find( 'a' )
print( a_element.get( "href" ) )
print( a_element.text )
print( a_element )

for element in soup.find_all( "a" ):
    print( element )
    print( element.get( "href" ) )
    print( element.text )

#print(len( soup.find_all( 'a' )))
"""
divs = soup.find_all( "div" )
for element in divs:
    #print( element )
    h4s = element.find_all( "h4 ")
    
    for h4 in h4s:
        print( h4 )
        if h4 == None:
            continue
        
        a__s = h4.find_all( "a___s" )
        for a in a__s:
            print( a )
            if a == None:
                continue
            bookname = a.text
            print( bookname )
