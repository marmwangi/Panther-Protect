<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'this is my home page'
=======
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
>>>>>>> ff3b12523eaffa0201fea3f6571a24a56f70b431
