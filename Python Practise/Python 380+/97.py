import re
from unittest import result


result=[]
for i in range(1,100):
    if i%10==0:
        result.append(i)
print(result)

result=[]
for i in range(1,100):
    if i%10==0 and i%3!=0:
        result.append(i)
print(result)

items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
result = []
for item in items:
    if not item % 2 != 0:
        result.append(item)
print(result)
##############################################
text = 'Python is a very popular programming language'
words=text.split(" ")
result=[]
for x,word in enumerate(words):
    if x<4:
        result.append(word.lower())
print(result)
##############################################
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []

for prob in probabilities:
    if prob >0.5:
        result.append(prob) 
        
print(result)
x=[]
for prob in probabilities:
    if prob >0.5:
        x.append(prob.__ceil__())
    if prob<0.5:
        x.append(prob.__floor__())
print(x)

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x','p']
freq={}

for item in items:
    if item in freq.keys():
        freq[item]+=1
    else:
        freq[item]=1
        
print(freq)
        
text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""
words=text.split()
words=[word.lower() for word in words] 
words = [word.replace('.', '').replace(',', '') for word in words]
words=[word for word in words if len(word)>6]
        
print(words)

indexes = [
    'BOVESPA', 'DOW JONES COMP', 'DOW JONES INDU',
    'DOW JONES TRANS', 'DOW JONES UTIL', 'IPC',
    'IPSA', 'MERVAL', 'NASDAQ COMP', 'NASDAQ100',
    'S&P500', 'S&P/TSX COMP'
]
for index in indexes:
    if "DOW" in index or "S&P" in index:
        print(index)
        
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

for x in names:
    if x.isalpha():
        print(f"hello {x}")
        
text = 'Python is a very popular programming language'

words = text.split(' ')
print(words)
result = []
for idx,word in enumerate(words):
    if idx<4:
        result.append(word.lower())
print(result)

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}
for ticker,close in gaming.items():
    if close>100:
        print(ticker)