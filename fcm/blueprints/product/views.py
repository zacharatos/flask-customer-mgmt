from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
    request
)

from fcm.extensions import db
from fcm.blueprints.product.models import Product, Category

product = Blueprint('product',
                    __name__,
                    template_folder='templates',
                    url_prefix='/product')


# Create routes related to products
@product.route('/add', methods=['GET', 'POST'])
def add_product():
    pass


@product.route('/edit/<int:pk>')
def edit_product(pk):
    pass


@product.route('/delete/<int:pk>')
def delete_product(pk):
    pass


# Create routes related to categories
@product.route('/cat/add', methods=['GET', 'POST'])
def add_cat():
    cat = Category(name='test')
    db.session.add(cat)
    db.session.commit()
    return redirect(url_for('webpage.products'))


@product.route('/cat/edit/<int:pk>')
def edit_cat(pk):
    pass


@product.route('/cat/delete/<int:pk>')
def delete_cat(pk):
    pass
