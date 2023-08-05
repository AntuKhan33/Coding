import os
from pathlib import Path

# path_os=os.getcwd()
# path_Path=Path.cwd()

path=Path('text/expenses.txt')
print(path)
print(path.name)
print(path.parts)
print(path.stem)
print(path.suffix)