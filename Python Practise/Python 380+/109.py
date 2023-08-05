from asyncore import read
from tempfile import TemporaryFile
from unittest import result


sum = 3000
counter = 0
try:
    result=sum/counter
    print(result)
except ZeroDivisionError:
    print(ZeroDivisionError )

try:
    with open ('file.txt','r') as file:
        content=file.read()
except:
    print('file note found')
    
users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
user_id = '004'

try:
    print(users[user_id])
except KeyError:
    print(f"the {user_id} key is not in the dictionary")
    