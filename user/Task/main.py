import csv
import psycopg2

from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__,template_folder="templates")
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
        id = request.form.get("id")
        name = request.form.get("name")
        age = request.form.get("age")
        salary = request.form.get("salary")
        print("name:" ,name,age,salary)
        cur = con.cursor()
        cur.execute("INSERT INTO final (id, name, age, salary) VALUES (%s, %s, %s, %s)", (id, name, age, salary))
        con.commit()
        
        print("Data Inserted Successfully")
        return redirect(url_for('index'))



@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete(id):
    cur =con.cursor()
    print("name")
    cur.execute("DELETE FROM final WHERE id = {0}".format(id))
    con.commit()
    print("Record Has Been Deleted Successfully")
    return redirect(url_for('index'))


@app.route('/update', methods=['POST','GET'])
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
    app.run(debug=True)
    
   
    