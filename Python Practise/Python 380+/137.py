from ast import arg
import numbers
import re
from unittest import result


def maximum(x,y):
    if x>=y:
        return x
    else:
        return y 
    
def maximum(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=z:
        return y
    else:
        return z
numbers=list(range(1,6))
def multi(numbers):
    result=1
    for number in numbers:
        result*=number
    return result
print(multi(numbers))

def map_longest(words):
    length=[]
    for word in words:
        length.append(len(word))
    return length

print(map_longest("abca"))
def filter_ge_6(words):
    result = []
    for word in words:
        if len(word) >= 6:
            result.append(word)
    return result

print(map_longest('dogsdsdsd'))

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))

def count_str(items):
    total=0
    for item in items:
        if isinstance(item,str):
            total+=1
    return total   
                
print(count_str("antu"))


def count_str(items):
    total = 0
    for item in items:
        if isinstance(item, str):
            total += 1
    return total
print(count_str("anaa"))

def remove_duplicates(items):
    return list(set(items))

print(remove_duplicates("antuaaa"))

def is_distinct(items):
    return len(items)==len(set(items))

print(is_distinct('antu'))

def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)

function(3)
function(5, ['a', 'b', 'c'])
function(6)

def function(*args,**kwargs):
    print(arg,kwargs)
    
function(3,4)
function(x=3,y=4)
function(1,2,x=3,y=4)

def is_palindrome(string):
    inverse=string[::-1]
    if string == inverse:
        return True
    else:
        return False
    
print("123")