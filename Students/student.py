from flask import Flask, render_template, request, redirect, url_for

# incude block SQLAlchemy with PYMySQL:
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ("mysql+pymysql://support:password123@localhost/students_db")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# create class for work with DB

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    course = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()

# end block SQLAlchemy with PYMySQL

@app.route('/')
def home():
    people = People.query.all()
    return render_template("index.html", people=people)

@app.route('/course')
def courses():
    people = People.query.all()
    return render_template("courses.html", people=people)


@app.route('/create_user', methods = ['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['E-mail']
        phone = request.form['Phone']
        course = request.form['course']
        status = request.form['status']

        student = People()

        student.name = name
        student.email = email
        student.phone = phone
        student.course = course
        student.status = status

        db.session.add(student)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("create_user.html")


@app.route('/change_user/<int:id>', methods = ['GET','POST'])
def change_user(id):
    if request.method == 'POST':
        student = People.query.get(id)        
        student.name = request.form['name']
        student.email = request.form['E-mail']
        student.phone = request.form['Phone']
        student.course = request.form['course']
        student.status = request.form['status']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("create_user.html", student = People)



@app.route('/delete_user/<int:id>', methods = ['GET','DELETE'])
def delete_user(id):
    student = People.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('home'))

# @app.route('/find_user/<int:id>', methods = ['GET'])
# def find_user(id):
#     student = People.query.get(id)
#     return render_template("index.html", people=[student])

if __name__ == '__main__':
    app.run(debug=True)