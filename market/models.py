from market import db

class Item(db.Model):
    ID = db.Column(db.Integer(), primary_key=True)
    Naziv = db.Column(db.String(length=30), nullable=False, unique=True)
    Barcode = db.Column(db.Integer(), nullable=False)
    Cijena = db.Column(db.String(length=12), nullable=False, unique=True)
    Opis = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'