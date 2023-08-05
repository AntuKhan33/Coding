from urllib.parse import uses_fragment


headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open('users.csv','w')as file:
    file.write(','.join(headers)+"\n")
    for i in users:
        file.write(','.join(i)+'\n')
        
import json


stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open('stocks.json', 'w') as file:
    json.dump(stocks, file, indent=4)
    
numbers = list(range(1, 20))
even = [number for number in numbers if number % 2 == 0]

with open('num.txt', 'w') as file:
    for num in even:
        file.write(str(num) + '\n')