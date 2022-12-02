from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'ID': 1, 'Naziv': 'Telefon', 'Barcode': '3877002166013', 'Cijena': 500},
        {'ID': 2, 'Naziv': 'Laptop', 'Barcode': '3877013327023', 'Cijena': 900},
        {'ID': 3, 'Naziv': 'Računar', 'Barcode': '3877075528823', 'Cijena': 320}
    ]
    return render_template('market.html', items=items)