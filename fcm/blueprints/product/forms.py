from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory

from fcm.extensions import db
from fcm.blueprints.product.models import Product, Category

# Create the base Model Form
BaseModelForm = model_form_factory(FlaskForm)


class ProductForm(ModelForm):
    class Meta:
        model = Product
