from datetime import datetime
from fcm.extensions import db


class Product(db.Model):
    """
    A class for creating the database schema for the
    model Product
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    desc = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False, default=0)
    options = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"


class Category(db.Model):
    """
    A class for creating the database schema for the
    model Category
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return f"<Category {self.name}>"
