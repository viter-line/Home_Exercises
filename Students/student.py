from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

# with app.app_context():
#     db.create_all()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    team_numb = db.Column(db.String(80), nullable=False)
    birthdate = db.Column(db.String(80))

    def __repr__(self):
        return 'Student %r' % self.id

with app.app_context():
    db.create_all()

@app.route('/home', methods = ['GET', 'POST'])
def home():
    students = Student.query.all()
    return render_template('01_students_index.html', students=students)



@app.route('/add_student', methods = ['GET', 'POST'])
def add_student():
    if request.method == 'POST':
    
        s = Student(
            first_name = request.form['first_name'],
            last_name = request.form['last_name'],
            team_numb = request.form['team_numb'],
            # birthdate = request.form['birthdate']
        )

        db.session.add(s)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('02_editing_student.html')


@app.route('/edit_student/<int:id>', methods = ['GET', 'POST'])
def edit_student(id):
    Student.first_name = request.form['first_name']
    Student.last_name = request.form['las_name']
    Student.team_numb = request.form['team_numb']
    
    db.session.update(s)
    db.session.commit()
    return redirect(url_for('home'))




@app.route('/delete_student/<int:id>', methods = ['GET'])
def delete_student(id):
    s = Student.query.get(id)
    db.session.delete(s)
    db.session.commit()
    return redirect(url_for('home'))



@app.route('/students_visits')
def students_visits():
    # s = Student(
    #         first_name = request.form['first_name'],
    #         last_name = request.form['last_name']
    #     )
    return render_template('03_visiting_index.html')



@app.route('/students_teams')

def students_teams():
    return render_template('04_group_index.html')


if __name__ == '__main__':
    app.run(debug=True)