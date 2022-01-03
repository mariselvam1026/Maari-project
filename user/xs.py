import xlsxwriter
workbook = xlsxwriter.Workbook('D:\\user\\Book.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Name')
worksheet.write('B1', 'Age')
worksheet.write('C1', 'salary')

worksheet.write('A2', 'MARI')
worksheet.write('B2', '22')
worksheet.write('C2', '1000')

worksheet.write('A3', 'SELVAM')
worksheet.write('B3', '23')
worksheet.write('C3', '2000')

workbook.close()