from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

all_posts=[
    {
        'title': 'post 1',
        'content': 'this is the content of post 1.'
    },
    {
        'title': 'post 2',
        'content': 'this is the content of post 2.'
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts= all_posts)

@app.route('/home/<string:name>')
def hello(name):
    return "Hello,"+name

if __name__ == "_main_":
    app.run(debug=True)
