from traceback import print_tb


x = -1.5
expression = 'x**2 + x'

print(eval(expression))


var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))
characters = ['k', 'b', 'c', 'j', 'z', 'w']
print(f'first : {min(characters)}')
print(f'first : {max(characters)}')
ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')
print(list(zip(ticker,full_name)))

items = (' ', '0', 0.1, True)
print(all(items))
items = (' ', 0.0, 0, False)
print(any(items))
number = 234
binary = bin(number)
binary=binary[2:]
print(binary.count('1'))
