# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:58:34 2020

@author: 88690
"""

import requests
import json


dic = { "SearchType" :"S",
        "Lang" :"TW",
        "StartStation" :"NanGang",
        "EndStation" :"ZuoYing",
        "OutWardSearchDate" :"2020/11/13",
        "OutWardSearchTime" :"21:00",
        "ReturnSearchDate" :"2020/11/13",
        "ReturnSearchTime" :"21:00",
        "DiscountType" :""
        }
#print( dic )

data = requests.post( "https://www.thsrc.com.tw/TimeTable/Search" , data = dic )
#print( data.text )
pythonData = json.loads( data.text )

datas = pythonData[ "data" ]
departureTable = datas[ "DepartureTable" ]

TrainItems = departureTable[ "TrainItem" ]
for TrainItem in TrainItems:
    TrainNumber = TrainItem[ "TrainNumber" ]
    DepartureTime = TrainItem[ "DepartureTime" ]
    DestinationTime = TrainItem[ "DestinationTime" ]
    NonReservedCar = TrainItem[ "NonReservedCar" ]
    print( "車次:" + TrainNumber + "," + "出發時間:" + DepartureTime + "," + "抵達時間:" + DestinationTime + "," + "自由座車廂:" + NonReservedCar )