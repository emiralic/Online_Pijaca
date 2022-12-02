from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Item(db.Model):
    ID = db.Column(db.Integer(), primary_key=True)
    Naziv = db.Column(db.String(length=30), nullable=False, unique=True)
    Barcode = db.Column(db.Integer(), nullable=False)
    Cijena = db.Column(db.String(length=12), nullable=False, unique=True)
    Opis = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'


@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)