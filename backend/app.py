from flask import Flask, request, jsonify
import mysql.connector
import os
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Database Configuration
DB_HOST = os.getenv('DB_HOST', 'database')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'mydb')

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# POST route to add user
@app.route('/submit', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    address = data.get('address')

    if not name or not address:
        return jsonify({'error': 'Missing name or address'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, address) VALUES (%s, %s)", (name, address))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'User added successfully'}), 201

# GET route to fetch users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
