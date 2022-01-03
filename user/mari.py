import psycopg2
import xlrd

con = psycopg2.connect(database="maridb", user="postgres", password="mari", host="127.0.0.1", port="5432")
#loc=('D:\\user\\ram.csv')
wb=xlrd.open_workbook("D:\\user\\ram.csv")
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,10):
    print(sheet.row_values(i))
con.close()
