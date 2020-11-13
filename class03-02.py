# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:09:36 2020

@author: 88690
"""
import re
import requests
from bs4 import BeautifulSoup

data = requests.get( "https://www.books.com.tw/web/sys_saletopb/books/" )

soup = BeautifulSoup( data.text , "html.parser" )
#print( soup.prettify() )

lis = soup.find_all( "li" , class_ = "item" )

for li in lis:
    #print( li )
    if li == None:
        continue
    
    imgs = li.find_all( "img" )
    #print( imgs )
    
    for img in imgs:
        print(re.search("(https)[\w:/\d.?&;= ]+(https)[\w:/\d.?&;=]+", str( img )))
        
        """
        #url = img.get( "src" )
        #name = img.get( "alt" )
        
        print( name )
        print( url )
        
        image = requests.get( url )
        
        try:
            file = open( name + ".png" , "wb" )
            file.write( image.content )
        except:
            print( "ERROR!!!ERROR!!!ERROR!!!")
        finally:
            file.close()
        """
    