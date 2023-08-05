from array import array
from itertools import count
import re
from unittest import result


y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]

def accuray(y_true,y_pred):
    counter=0
    for i,j in zip(y_true,y_pred):
        if i==j:
            counter+=1
    return counter

print(accuray(y_true,y_pred))

def mae(y_true, y_pred):
    return round(sum([abs(i[1] - i[0]) for i in zip(y_true, y_pred)]) / len(y_true), 3)
print(mae([0, 0, 1, 1, 0, 1, 0],[0, 0, 1, 0, 0, 1, 0]))

def relu(x):
    return max(0,x)

print(relu(5))

def flatten(items):
    result=[]
    for item in items:
        result.extend(item)
    return result

print(flatten("an"))

def transfer_zeros(items):
    result=[]
    counter=0
    for item in items:
        if item ==0:
            counter+=1
        else:
            result.append(item)
    result.extend([0]*counter)
    return result
print(transfer_zeros('antu khan'))
def euclidean_distance(x, y):
    squared_diff = [(i - j)**2 for i, j in zip(x, y)]
    return (sum(squared_diff)) ** 0.5

def arrange(start,stop,step=1):
    result=[]
    for i in range(start,stop,step):
        result.append(i)
    return result 
l1 = [0, 0, 1, 1, 0, 1, 0]
l2 = [0, 0, 1, 0, 0, 1, 0]
def concat(l1, l2):
    result = []
    for i, j in zip(l1, l2):
        result.append([i[0], j[0]])
    return result
def identity(n):
    array=[[0]*n for i in range(n)]
    for idx,item in enumerate(array):
        item[idx]=1
    return array

print(identity(2))

def fill_value(height,width,value):
    return [[value]*width for i in range(height)]
print(fill_value(2,4,3))

def max_prob(array):
    result=[]
    for item in array:
        max_val=max(item)
        for idx,val in enumerate(item):
            if val==max_val:
                result.append([val])
                
    return result

def count_none(items):
    counter=0
    for item in items:
        if not item:
            counter+=1
    return counter

print(count_none([5,4,25,1,25]))

def top_n(arr,n):
    arr.sort(reverse=True)
    return arr[:n]

print(top_n([25,2,1,8],2))

def detect_class(array):
    result = []

    for item in array:
        max_val = max(item)
        empty = [0] * len(item)
        for idx, val in enumerate(item):
            if val == max_val:
                empty[idx] = 1
                result.append(empty)
    return result
