# from wtforms_alchemy import ModelFormField
from wtforms_sqlalchemy.fields import QuerySelectField

from fcm.blueprints import ModelForm
from fcm.blueprints.product.models import Product, Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        strip_string_fields = True
        only = ['name']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        strip_string_fields = True
        only = ['name', 'desc', 'price', 'options']

    category_id = QuerySelectField('Category',
                                   query_factory=lambda: Category.query,
                                   allow_blank=False)
