import csv
from SHA3 import hashed_data
fields = ['Database']

new_rows = [
    [hashed_data]
]

# Open the CSV file in append mode and write the new rows
with open('my_file.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    
    # Write the column names if the file is empty
    if f.tell() == 0:
        writer.writerow(fields)
    
    # Write each row of data
    for row in new_rows:
        writer.writerow(row)
