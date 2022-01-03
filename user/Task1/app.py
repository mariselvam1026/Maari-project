import csv
import psycopg2
import psycopg2.extras
from weasyprint import HTML

from fpdf import FPDF

from flask import Flask,render_template,Response,make_response

app = Flask(__name__, template_folder="templates")
#app.run(debug=True)

con = psycopg2.connect(database="maridb", user="postgres", password="mari", host="127.0.0.1", port="5432")
print('con',con)
print("Database opened successfully")

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/download/report/pdf')
def download_report():

    print("hello")
    
    try:
        cur = con.cursor()
          
        cur.execute("SELECT * FROM final")
        result = cur.fetchall()
        

        print(result)
  
        pdf = FPDF()
        pdf.add_page()
          
        page_width = pdf.w - 2 * pdf.l_margin
          
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Employee Data', align='C')
        pdf.ln(10)
  
        pdf.set_font('Courier','', 12)
          
        col_width = page_width/4
          
        pdf.ln(1)
          
        th = pdf.font_size
        print('yes')
        
        for row in result:
            
            pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(col_width, th, row[1], border=1)
            pdf.cell(col_width, th, str(row[2]), border=1)
            pdf.cell(col_width, th, str(row[3]), border=1)
            pdf.ln(th)

            
            
          
            # return index()
        print('yes5')
        #response = make_response(pdf, content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        #return response

        #response = make_response(pdf.output(dest='S').encode('latin-1'))
        #response.headers.set('Content-Disposition', 'attachment', filename='employee_report.pdf')
        #response.headers.set('Content-Type', 'application/pdf')
        #return response

        #return redirect(url_for('index')) 
        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=employee.pdf'})
    except Exception as e:
        print(e)
        return 'hello'
    finally:
        cur.close() 
        con.close()
    
          
  
if __name__ == "__main__":
    app.run(debug=True)
    