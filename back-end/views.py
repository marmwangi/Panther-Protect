from flask import Blueprint, render_template

view = Blueprint('views', __name__)

@view.route('/')
def home():
    return render_template('index.html')

@view.route('/map')
def map():
    return "MAP"