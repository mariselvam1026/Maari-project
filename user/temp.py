import sql.connector

con=mysql.connector.connect(host="localhost",user="root",password="root",database="final.db")




while True:
    print("1.Insert")
    print("2.update")
    print("3.select")
    print("4.delete")
    print("5.Exit")
    
choice=int(input("Enter your choice:"))
