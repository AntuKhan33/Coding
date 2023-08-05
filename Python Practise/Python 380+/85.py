


filename = '01012020_sales.xlsx'
if filename.endswith("xlsx"):
    print('yes')
else:
    print("no")
code="DIVISION"
if code.isupper():
    print("yes")
    
number=1.0
if isinstance(number,int):
    print('yes')
else:
    print("No")
    
password = 'cskdnjcasa#!'
if len(password)>11:
    print("Yes") 
if len(password)>11 and "!" in password:
    print("password correct")
else:
    print("password correct")
    
project_ids = ['02134', '24253']
project_id = '02135'

if project_id not in project_ids:
    project_ids.append(project_id)
print(project_ids)

project_ids = {
    '01': 'open', 
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}

if project_ids['02']=="new":
    project_ids['02']="open"
print(project_ids)

item = '001'
items = ['001', '000', '003', '005', '006']

if item in items:
    items.remove(item)
print(items)