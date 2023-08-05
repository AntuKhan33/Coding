text = 'Python programming'
text = text.lower()
print(text)
characters = list(set(text))
print(characters)
characters.remove(" ")
print(characters) 
characters.sort()
print(characters) 

filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
filenames.remove('ball.png')
print(filenames)
day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1.extend(day2)
print(day1)
hashtags = ['summer', 'time', 'vibes']
print("#".join(hashtags))