from flask import Blueprint, render_template

customer = Blueprint('customer', __name__, template_folder='templates')


# Create routes related to the customers
@customer.route('/customer/add', methods=['POST'])
def add_customer():
    pass


@customer.route('/customer/edit/<int:pk>')
def edit_customer(pk):
    pass


@customer.route('/customer/delete/<int:pk>')
def delete_customer(pk):
    pass
