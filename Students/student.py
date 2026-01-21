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
    mobile_phone = db.Column(db.String(80), nullable=False)
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
    return render_template("courses.html")


@app.route('/create_user', methods = ['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['E-mail']
        phone = request.form['Phone']
        mobile_phone = request.form['Mobile_Phone']
        status = request.form['status']

        student = People()

        student.name = name
        student.email = email
        student.phone = phone
        student.mobile_phone = mobile_phone
        student.status = status

        db.session.add(student)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("create_user.html")


# @app.route('/change_user/<int:id>', methods = ['GET', 'POST'])
# def change_user(id):
#     Student.first_name = request.form['first_name']
#     Student.last_name = request.form['las_name']
#     Student.team_numb = request.form['team_numb']
    
#     db.session.update(s)
#     db.session.commit()
#     return redirect(url_for('home'))




# @app.route('/delete_student/<int:id>', methods = ['GET'])
# def delete_student(id):
#     s = Student.query.get(id)
#     db.session.delete(s)
#     db.session.commit()
#     return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)