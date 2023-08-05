
list1 = [1, 2, 0]
list2 = [4, 5, 6, 9]
result = False

for item1 in list1:
    if item1 in list2:
        result = True
        break

print(result)

hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True

for hashtag in hashtags:
    if not isinstance(hashtag,str):
        result=False
        break
print(result)

number = 13
if number>1:
    for i in range(2,number):
        if number %i ==0:
            print(f"{number} - not a prime number")
            break
    else:
        print(f"{number} - prime number")
else:
    print(f"{number}- not a prime number")