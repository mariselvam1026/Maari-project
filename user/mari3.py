import pandas as pd
import pdfkit as pdf

a = pd.read_csv("D:\\user\\ram6.csv")
a.to_html("Table.html")
html_file = a.to_html()

pdf.from_file('Table.html', 'Table.pdf')
