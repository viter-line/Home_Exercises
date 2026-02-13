from flask import Flask, request, jsonify
import mysql.connector

from flask_cors import CORS 

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

db = mysql.connector.connect(
    user = 'support',
    password = 'password123',
    host = 'localhost',
    database = 'students_db'
)

@app.route('/api', methods=['GET'])
def home():

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM people;")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return jsonify(data)

@app.route('/api/student', methods=['GET'])
def student():
    
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT name, email, phone FROM people;")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return jsonify(data)

@app.route('/api/course', methods=['GET'])
def course():

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT course, name, status FROM people;")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return jsonify(data)

@app.route("/api/create_user", methods=["POST"])
def create_user():

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    course = data.get('course')
    status = data.get('status')

    cursor = db.cursor()
    sql_query = "INSERT INTO people (name, email, phone, course, status) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql_query, (name, email, phone, course, status))
    db.commit()
    return jsonify({"message":"user created!"}), 200


@app.route('/api/student/delete/<int:id>', methods = ['DELETE'])
def student_delete(id):

    cursor = db.cursor()
    query = " DELETE FROM people WHERE id=%s "
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    return jsonify({"message":"user deleted!"}), 200

@app.route('/api/course/delete/<int:id>', methods = ['DELETE'])
def course_delete(id):

    cursor = db.cursor()
    query = " DELETE FROM people WHERE id=%s "
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    return jsonify({"message":"course deleted!"}), 200
    

@app.route('/api/student/edit/<int:id>', methods=["PUT"])
def edit_student(id):

    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    course = data['course']
    status = data['status']

    cursor = db.cursor(dictionary=True)
    query = " UPDATE people SET name=%s, email=%s, phone=%s, course=%s, status=%s WHERE id=%s; "
    cursor.execute(
        query, 
        (name, email, phone, course, status, id)
    )
    db.commit()
    cursor.close()
    return jsonify({"message": "student updated!"}), 200

@app.route('/api/course/edit/<int:id>', methods=["PUT"])
def edit_course(id):

    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    course = data['course']
    status = data['status']

    cursor = db.cursor(dictionary=True)
    query = " UPDATE people SET name=%s, email=%s, phone=%s, course=%s, status=%s WHERE id=%s; "
    cursor.execute(
        query, 
        (name, email, phone, course, status, id)
    )
    db.commit()
    cursor.close()
    return jsonify({"message": "course updated!"}), 200

if __name__ == '__main__':
    app.run(debug=True)