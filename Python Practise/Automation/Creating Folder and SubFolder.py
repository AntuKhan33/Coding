from pathlib import Path
import calendar
from re import T

# 1.Create a single folder
Path('new_folder12').mkdir(exist_ok=True)
Path('new_folder1/new_subfolder/new_subsubfolder').mkdir(parents=True,exist_ok=True)
month_names=list(calendar.month_name[1:])
day_names=list(calendar.day_name[1:])

for i,month in enumerate(month_names):
    for day in day_names:
        Path(f"2022/{i+1}.{month}/{day}").mkdir(parents=True,exist_ok=True)
