from flask import Blueprint, render_template

webpage = Blueprint('webpage', __name__, template_folder='templates')


# Create the routes related to the wabpage
@webpage.route('/')
def dashboard():
    return render_template('webpage/dashboard.html')


@webpage.route('/customers')
def customers():
    return render_template('webpage/customers.html')


@webpage.route('/products')
def products():
    return render_template('webpage/products.html')


@webpage.route('/orders')
def orders():
    return render_template('webpage/orders.html')
