import csv
import psycopg2

from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__)
#app.run(debug=True)

con = psycopg2.connect(database="maridb", user="postgres", password="mari", host="127.0.0.1", port="5432")
print('con',con)
print("Database opened successfully")

@app.route('/')
def index():
    print('hel')
    cur = con.cursor()
    cur.execute("SELECT * FROM final")
    data = cur.fetchall()
    cur.close()
    print('data',data)
    return render_template("index.html", employee=data)




@app.route('/insert', methods = ['POST','GET'])
def insert():

    if request.method == "POST":
        
        name = request.form['name']
        age = request.form['age']
        salary = request.form['salary']
        cur = con.cursor()
        cur.execute("INSERT INTO final (name, age, salary) VALUES (%s, %s, %s)", (name, age, salary))
        con.commit()
        print("Data Inserted Successfully")
        return redirect(url_for('index'))



@app.route('/delete/<string:id>', methods = ['GET'])
def delete(id):
    
    cur =con.cursor()
    cur.execute("DELETE FROM final WHERE id=%s", (id,))
    con.commit()
    print("Record Has Been Deleted Successfully")
    return redirect(url_for('index'))


@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        salary = request.form['salary']
        cur = con.cursor()
        cur.execute("""
               UPDATE final
               SET name=%s, age=%s, salary=%s
               WHERE id=%s
            """, (name, age, salary, id))
        print("Data Updated Successfully")
        con.commit()
        return redirect(url_for('index'))


if __name__ == "__main__":
    print('hello')
    index()
    
    app.run()
    