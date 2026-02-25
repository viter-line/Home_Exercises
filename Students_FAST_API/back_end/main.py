from fastapi import FastAPI
from pydantic import BaseModel 
import mysql.connector

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Unit(BaseModel):
    name: str
    email: str
    phone: int
    course: str
    status: str

# DB connect
db = mysql.connector.connect(
    user = 'support',
    password = 'password123',
    host = 'localhost',
    database = 'students_db'
)

@app.get("/api")
async def home():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM people;")
    data = cursor.fetchall()
    cursor.close()
    return data

@app.get("/api/students")
async def students():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email, phone FROM people;")
    data = cursor.fetchall()
    cursor.close()
    return data

@app.get("/api/courses")
async def courses():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, course, name, status FROM people;")
    data = cursor.fetchall()
    cursor.close()
    return data

@app.post("/api/create_user")
async def create_user(user: Unit):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO people (name, email, phone, course, status) VALUES (%s, %s, %s, %s, %s)",
        (user.name, user.email, user.phone, user.course, user.status)
    )
    db.commit()
    cursor.close()
    return {"message": "user created!"}

@app.delete("/api/students/delete/{id}")
async def students_delete(id):
    cursor = db.cursor()
    query = " DELETE FROM people WHERE id=%s "
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    return 'user deleted'

@app.delete("/api/courses/delete/{id}")
async def courses_delete(id: int):
    cursor = db.cursor()
    query = " DELETE FROM people WHERE id=%s "
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    return 'courses deleted'

@app.put("/api/students_edit/{id}")
async def edit_student(id: int, user: Unit):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE people SET name=%s, email=%s, phone=%s, course=%s, status=%s WHERE id=%s",
        (user.name, user.email, user.phone, user.course, user.status, id)
    )
    db.commit()
    cursor.close()
    return {"message": "student updated"}

@app.put("/api/courses_edit/{id}")
async def edit_courses(id: int, user: Unit):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE people SET name=%s, course=%s, status=%s WHERE id=%s",
        (user.name, user.course, user.status, id)
    )
    db.commit()
    cursor.close()
    return {"message": "courses updated"}

@app.patch("/api/students_edit/{id}")
async def edit1_student(id: int, user: Unit):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE people SET name=%s, email=%s, phone=%s, course=%s, status=%s WHERE id=%s",
        (user.name, user.email, user.phone, user.course, user.status, id)
    )
    db.commit()
    cursor.close()
    return {"message": "student updated"}

@app.patch("/api/courses_edit/{id}")
async def edit1_courses(id: int, user: Unit):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE people SET name=%s, course=%s, status=%s WHERE id=%s",
        (user.name, user.course, user.status, id)
    )
    db.commit()
    cursor.close()
    return {"message": "courses updated"}