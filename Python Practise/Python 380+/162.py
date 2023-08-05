from unittest import result


with open ("gaming.txt",'r') as file:
    text=file.readlines()
text=[line.replace("\n",'') for line in text]
text=[line for line in text if len(line)>0]
print(text)

tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]
gross_price=[round(price * (1+tax),2) for price in net_price]
print(gross_price) 

data=dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))
result=[[key,val] for key,val in data.items()]
print(result)