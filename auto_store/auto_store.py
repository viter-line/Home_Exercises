from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mysql+pymysql://support:password123@localhost/first_flask_db"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    engine = db.Column(db.String(100), nullable=False)
    fluel = db.Column(db.String(100), nullable=False)




cars = []

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def add_auto():
    car = {
        'brand': request.form['nm'],
        'model': request.form['md'],
        'year': request.form['yr'],
        'engine': request.form['ven'],
        'fuel': request.form['fl']
    }
    cars.append(car)
    return redirect(url_for('view'))

@app.route('/read')
def view():
    return render_template('view.html', cars=cars)




if __name__ == '__main__':
    app.run(debug=True)
