import psycopg2

import xlsxwriter
from xlsxwriter.workbook import Workbook

con = psycopg2.connect(database="maridb", user="postgres", password='mari', host="127.0.0.1", port="5432")
print('con',con)
print("Database opened successfully")

workbook = xlsxwriter.Workbook('D:\\user\\Book1.xlsx')
worksheet = workbook.add_worksheet()
#wb=Workbook()
#Workbook['Sheet1'].title ="MARISELVAM"
#sh1=Workbook.active
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'ID', bold)
worksheet.write('B1', 'Name', bold)
worksheet.write('C1', 'Age', bold)
worksheet.write('D1', 'salary', bold)
 

def select():
    res = con.cursor()
    
    qry="SELECT * FROM final;"
    res.execute(qry)
    result=res.fetchall()
    i=2
    for row in result:
        print(row)
        #print("Id", row[0])
        #print("NAME:", row[1])
       # print("AGE:", row[2])
        #print("SALARY:", row[3])
        
 
        worksheet.write("A{0}".format(i),row[0])
        worksheet.write("B{0}".format(i),row[1])
        worksheet.write("C{0}".format(i),row[2])
        worksheet.write("D{0}".format(i),row[3]) 
        i=i+1
        
        
        
           
        #for row1 in result:
            #worksheet.write('A3', row1[1])
            #worksheet.write('B3', row1[2])
            #worksheet.write('C3', row1[3])
        
        
    print("Select data successfully")
    workbook.close()
    quit()
    
def insert(id,name, age, salary):
    res=con.cursor()
    qry="INSERT into final(id, name, age, salary) values (%s, %s, %s, %s);"
    #result=(name, age, salary)
    res.execute(qry, (id, name, age, salary))
    con.commit()
    print("Insert data successfully")

def update(id, name, age, salary):
    res=con.cursor()
    qry="UPDATE final SET name=%s ,age=%s, salary=%s WHERE id=%s;"
    res.execute(qry, (name, age, salary, id))
    con.commit()
    print("Update data successfully")

def delete(id):
    res=con.cursor()
    qry="DELETE FROM final WHERE id =%s;"
    result=(id,)
    res.execute(qry, result)
    con.commit()
    print("Delete successfully")

    

while True:
    print("1.select")
    print("2.insert")
    print("3.update")
    print("4.delete")
    print("5.Exit")

    choice=int(input("Enter your choice"))
    if choice == 1:
        select()

    elif choice == 2:
        id = input("Enter the id:")
        name = input("Enter the name:")
        age = input("Enter the age")
        salary = input("Enter the salary")
        insert(id, name, age, salary)

    elif choice == 3:
        id=input("Enter the id:")
        name=input("Enter the name:")
        age=input("Enter the age:")
        salary=input("Enter the salary:")

        update(id, name, age, salary)
    
    elif choice == 4:
        id=input("Enter the id:")
        delete(id)

    elif choice == 5:
        quit()

    else:
        print('Invalid selection')
        quit()
    
    print("THANK YOU")

    