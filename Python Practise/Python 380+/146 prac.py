stocks = ['playway', 'boombit', 'cd projekt']
length=list(map(lambda stock: len(stock),stocks))
length=list(map(lambda x: len(x),stocks))
print(length) 

def sort_list(items):
    return sorted(items,key=lambda item: item[1])
