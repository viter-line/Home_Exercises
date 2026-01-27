from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    user = 'support',
    password = 'password123',
    host = 'localhost',
    database = 'students_db'
)

@app.route('/', methods=['GET'])
def home():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM people;")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return jsonify(data)

@app.route('/student', methods=['GET'])
def student():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT name, email, phone FROM people;")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return jsonify(data)

@app.route('/course', methods=['GET'])
def course():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT course, name, status FROM people;")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return jsonify(data)

@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.get_json()
    
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    course = data.get('course')
    status = data.get('status')

    cursor = db.cursor()
    sql_query = "INSERT INTO students_db (name, email, phone, course, status) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql_query, (name, email, phone, course, status))
    db.commit()
    return jsonify({"message":"user created!"}), 200


@app.route('/student/delete/<int:id>', methods = ['DELETE'])
def student_delete(id):
    cursor = db.cursor()
    query = " DELETE FROM students_db WHERE id=%s "
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    return jsonify({"message":"user deleted!"}), 200

@app.route('/course/delete/<int:id>', methods = ['DELETE'])
def course_delete(id):
    cursor = db.cursor()
    query = " DELETE FROM students_db WHERE id=%s "
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    return jsonify({"message":"course deleted!"}), 200
    

@app.route('/student/edit', methods=["PUT"])
def edit_student():
    id = request.get_json('id')
    name = request.get_json('name')
    email = request.get_json('email')
    phone = request.get_json('phone')
    course = request.get_json('course')
    status = request.get_json('status')
    cursor = db.cursor(dictionary=True)
    query = " UPDATE students_db SET name=%s, email=%s, phone=%s, course=%s, status=%s WHERE id=%s;"
    cursor.execute(query, (name, email, phone, course, status, id))
    db.commit()
    cursor.close()
    return jsonify({"message": "student updated!"}), 200

@app.route('/course/edit', methods=["PUT"])
def edit_course():
    id = request.get_json('id')
    name = request.get_json('name')
    email = request.get_json('email')
    phone = request.get_json('phone')
    course = request.get_json('course')
    status = request.get_json('status')
    cursor = db.cursor(dictionary=True)
    query = " UPDATE people SET name=%s, email=%s, phone=%s, course=%s, status=%s WHERE id=%s;"
    cursor.execute(query, (name, email, phone, course, status, id))
    db.commit()
    cursor.close()
    return jsonify({"message": "course updated!"}), 200

if __name__ == '__main__':
    app.run(debug=True)