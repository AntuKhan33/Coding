capitals={
    'usa':'washington',
    'germany':'berlin',
    "australia":'vienna'
}
print(capitals )
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals.get("australia"))
stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
print(stocks['MSFT.US']["Microsoft Corp"])
print(stocks["AAPL.US"])

stocks['MSFT.US']['Microsoft Corp']=190
print(stocks['MSFT.US']["Microsoft Corp"])
stocks['V.US']={'Visa Inc':185}
print(stocks.values())

print(list(enumerate(stocks)))
tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]
print(list(enumerate(tickers)))
print(dict(enumerate(tickers)))
project_ids = {
    '01': 'open', 
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
result=list(set(project_ids))
result.sort()
print(result)
stats={'site':"e-smart",'traffic':100}
del stats['traffic']
print(stats)
users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
print(users.get('004','indefinite'))
print(users.items())