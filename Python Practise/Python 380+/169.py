
from unicodedata import name
from unittest import result


x={i:i**2 for i in range(1,8)}
print(x) 
stocks = ['Playway', 'CD Projekt', 'Boombit']

result={name:len(name) for name in stocks}
print(result)
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
result={value:key for key,value in stocks.items()}
print(result)

stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
result = {key:val for key, val in stocks.items() if val > 100}
print(result)

data=[{i:i**j for i in range(1,10) for j in range(1,4)}]
print(data)
properties = ['number of companies', 'companies', 'cap']
indeks = ['WIG20', 'mWIG40', 'sWIG80']
data = {idx: {i: None for i in properties} for idx in indeks}
print(data)

data={key:val for key,val in enumerate(indeks)}
print(data)