from time import timezone


text = 'python is a popular programming language.'

print(text.capitalize())
print(f"number of occurance:{text.count('p')}")
print(f"number of occurance: {text.count('p')}")
code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'
print(f"Code endswith",code1.endswith("2020"))
print(f"code endswith {code2.endswith('2020')}")
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'
print(f"path1: {path1.startswith('youtube')}")
print(f"path1: {path1.startswith('youtube')}")
path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'
print(f"path1: {path1.find('scientist')}")
print(f"path3: {path3.find('scientist')}")
code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'

print(f'code:{code1.isalnum()}')
print(f"code:{code2.isalnum()}")
print(code2.lower())
print(code2.upper())
text = '  Google Colab   '
print(text.strip())
code = 'FVNISJND-XX'

print(code.replace('-',""))
text = '340-23-245-235'
print(text.replace("-",""))
text = 'Open,High,Low,Close'
print(text.split(','))
text = """Python is a general-purpose language.
Python is popular."""
print(text.splitlines())
num = 34
print(str(num).zfill(6))
print(str(num).zfill(6))
url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
name=url.split('/')[-1]
name=name.replace("-",' ' )
print(name)

#name=url.split('com')[:1]
url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
name=url.split('com')[0]
y='com'
x=name+y
print(x)
# for x in name:
#     print(name.replace)
import webbrowser 
new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs

import webbrowser

webbrowser.open_new_tab(x)