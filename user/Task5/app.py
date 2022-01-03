from flask import Flask,jsonify,request
import json
app=Flask(__name__)

employee = [
    {"id":0,
    "name":"MARI",
    "age":"23",
    "salary":"1111"},
    {"id":1,
    "name":"Selvam",
    "age":"24",
    "salary":"24444"},
    {"id":2,
    "name":"RAMAR",
    "age":"25",
    "salary":"4444"}
]

@app.route('/')
def index():
    return "Hi"

@app.route('/employee', methods=['GET'])
def get():
    return jsonify(employee)

@app.route('/employee/<int:id>', methods=['GET'])
def get_id(id):
    return jsonify({'employee':employee[id]})


@app.route('/employee', methods=['POST'])
def insert():
    #new={'id':4,
    #'name':'MARISELVAM',
    #'age':'27',
    #'salary':'8888'}
    new=json.loads(request.data)
    print("data:" , new)
    employee.append(new)
    return jsonify({'insert':employee})

@app.route('/employee/<int:id>', methods=['PUT'])
def update(id):
    employee[id]['name'] = "Mmmm"
    return jsonify(employee[id])
    # return "success"

@app.route('/employee', methods=['DELETE'])
def delete():
    id=int(request.args.get('id'))
    print("id1:", type(id))
    employee.remove(employee[id])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

