sub={'mathematics','phy'}
sub.add('english')
print(sub)

text="Programing in python."
print(text.lower())
print(text.replace(" ",""))
print(text.replace(".",""))
vowels={'a','e','i','o','u'}
letters = set(text)
print(letters)
consotants=letters.difference(vowels)
print(f'Number of items:',len(consotants))

a={2,4,6,8}
b={4,10}
sym_diff=a.symmetric_difference(b)
print(f"Symmentric differnece {sym_diff}")

ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}
result = ad1_id.symmetric_difference(ad2_id)
print(f'Selected ID: {result}')
is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
result=is_clicked.intersection(is_bought)
print(f'Customer ID: {result}')