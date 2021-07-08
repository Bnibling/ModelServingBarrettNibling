# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 09:11:48 2021

@author: 943656
"""

# python postrequests.py <url>

import requests
import sys
import json

# url = sys.argv[1]
url = 'https://httpbin.org/post'

with open(sys.argv[1]) as json_file:
    data = json.loads(json_file.read())

print(data)
print(type(data))
response = requests.post(url = url, 
                         data = data
                         )



print(response.text)

print(response.ok)

outputs = json.loads(response.text)['form']

print(outputs)