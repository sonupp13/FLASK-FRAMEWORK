from flask import Flask,render_template



app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1> sonu </h1>'

# @app.route('/home')
# def home():
#     return '<h1> good morning</h1>'

# @app.route('/hy')
# def home():
#     return '<h1> good night</h1>'

# @app.route('/users/<name>')
# def users(name):
#     return '<h1> hy hello {} </h1>'.format(name)

# @app.route('/users/<name>')
# def users(name):
#     return '<h1> hy hello {} </h1>'.format(name[3])

# @app.route('/users/<name>')
# def users(name):
#     return '<h1> hy hello {} </h1>'.format(name[6])  #errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

# @app.route('/add/<int:a>/<int:b>')
# def add(a,b):
#     result=a+b
#     return f"the result of {a} + {b} is {result}"

# @app.route('/sub/<int:a>/<int:b>')
# def sub( a ,b):
#     result=a-b
#     return f"the result of {a} - {b} is {result}"

@app.route('/hello')
def hello():
    return render_template('index.html')

@app.route('/good_after_noon')
def hy():
    return render_template('sonu.html')

if __name__== "__main__":
    app.run(debug=True)

