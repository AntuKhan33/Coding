dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
result=dji1+dji2
print(result) 
result = (dji1, dji2)
print(result)
members = (('Kate', 23), ('Tom', 19))

members=(members[0],('john',21),members[1])
print(members)
default = ('YES', 'NO', 'NO', 'YES', 'NO')
print(default.count("YES"))
names = ('Monica', 'Tom', 'John', 'Michael')
sorted_names=tuple(sorted(names))
print(sorted_names)

info = (('Monica', 19), ('Tom', 21), ('John', 18))
asc=tuple(sorted(info,key=lambda item:item[1]))
desc=tuple(sorted(info,key=lambda item:item[1],reverse=True))
print(f"Ascending: {asc}")
print(f"descending: {desc}")

stocks = (('Apple Inc', ('AAPL.US', 310)), ('Microsoft Corp', ('MSFT.US', 184)))
print(stocks[0][1][0])