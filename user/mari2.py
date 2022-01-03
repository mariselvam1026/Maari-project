import csv
with open('D:\\user\\ram6.csv',newline='') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)

