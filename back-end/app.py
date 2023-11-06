from flask import Flask, render_template 
from . import views

app = Flask(__name__)
app.register_blueprint(view, url_prefix='/')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('Slay')

if __name__ == '__main__':
    app.run(debug=True)
