from flask import Flask, render_template, redirect, request, jsonify,json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class CodeSpeedyBlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    posted_by = db.Column(db.String(20), nullable=False, default='N/A')
    posted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return self.title


db.create_all()
db.session.commit()

@app.route('/')
#@app.route('/home')
#@app.route('/CodeSpeedy')
def Welcome():
    return "Hloo"


@app.route('/employee', methods=['GET'])
def get():
    return jsonify(CodeSpeedyBlog)

@app.route('/employee/<int:id>', methods=['GET'])
def get_id(id):
    return jsonify({'employee':CodeSpeedyBlog[id]})


@app.route('/employee', methods=['POST'])
def insert():
    #new={'id':4,
    #'name':'MARISELVAM',
    #'age':'27',
    #'salary':'8888'}
    new=json.loads(request.data)
    print("data:" , new)
    CodeSpeedyBlog.append(new)
    return jsonify({'insert':CodeSpeedyBlog})



@app.route('/employee', methods=['DELETE'])
def delete():
    id=int(request.args.get('id'))
    print("id1:", type(id))
    CodeSpeedyBlog.remove(CodeSpeedyBlog[id])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

