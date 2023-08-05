import calendar
from datetime import  date
import imp
from unittest import result

#print(calendar.calendar(2020))
#print(calendar.month(2020,6))

date1=date(2016,4,3)
date2=date(2022,8,29)
diff=date2-date1
print(diff)
import re
string ="Python 3.8"
result=re.findall(pattern=r"\d",string=string)
print(result)
string='!@#$%^&45wc'
result=re.findall(pattern=r"\w",string=string)
print(result)
raw_text = "Send an email to info@template.com or sales-info@template.it"
result = re.findall(r"[\w\.-]+@[\w\.-]+", raw_text)
print(result)
text = 'Programming in Python - from A to Z'
result  =re.split(pattern=r'\s+',string=text)
print(result)

import string
print(string.ascii_letters)
from collections import Counter
counter=Counter()
items=['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
for item in items:
    counter[item]+=1
print(counter)
import math

def sigmoid(x):
    return 1/(1+math.exp (-x))

import random
random.seed(12)

items = ['python', 'java', 'sql', 'c++', 'c']
choice = random.choice(items)
print(choice)
random.seed(15)
items = ['python', 'java', 'sql', 'c++', 'c']
random.shuffle(items)
print(items)
import pickle
ids=['001','003','011']
with open('data.pickle', 'wb') as file:
    pickle.dump(ids, file)
    
import json
stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
result=json.dumps(stocks,sort_keys=True,indent=4)
print(result)