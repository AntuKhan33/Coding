from audioop import reverse


filename="view.jpj"
print(filename[-3:]) 
print(filename[3:])

print(filename[:-3]) 
print(filename[:3])

string = 'PKV-89415-PLN'

code=string[:3]+string[:-3]
print(code)
string = '1 0 0 1 0 1'
binary=string[::3]
string = '1 0 0 1 0 1'
binary = string[::2]
numbers = int(binary,2)
print(f'Number found: {numbers}')

text = 'Python Course'
print(text[::-1])
