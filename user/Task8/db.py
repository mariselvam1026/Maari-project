from flask import Flask,jsonify,request
from user_service import UserService

app = Flask(__name__)
service=UserService()

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(service.get_all())

@app.route('/users/<user_id>', methods=["GET"])
def get_user_id(user_id):
    return jsonify(service.get_by_id(user_id))

@app.route('/users', method=['POST'])
def save_user():
    return jsonify(service.create(request.form))

@app.route('/users/<user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    return jsonify(service.update(user_id,request.form))

if __name__ == '__main__':
    app.run(debug=True)
