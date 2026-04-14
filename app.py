from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = str(len(users) + 1)
    users[user_id] = data
    return jsonify({"message": "User added"}), 201

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    if id in users:
        users[id] = request.json
        return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    if id in users:
        del users[id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)