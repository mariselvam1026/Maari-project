import csv
import psycopg2

con = psycopg2.connect(database="maridb", user="postgres", password="mari", host="127.0.0.1", port="5432")
print('con',con)
print("Database opened successfully")
#cur=con.cursor()
l=list()
file = open('D:\\user\\ram6.csv')
csvreader=csv.reader(file)
header=next(csvreader)
print (header)
rows=[]
for row in csvreader:

    rows.append(tuple(row))
print(rows)
cur=con.cursor()
qry="INSERT INTO final(id, name, age, salary) VALUES (%s, %s, %s, %s);"
cur.executemany(qry, rows)
con.commit()
con.close()
file.close()
 
