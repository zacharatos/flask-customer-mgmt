from flask import Blueprint, render_template

webpage = Blueprint('webpage', __name__, template_folder='templates')


# Create the routes related to the wabpage
@webpage.route('/')
def home():
    # return render_template('home.html')
    return 'Hello world!! from Blueprints!'
