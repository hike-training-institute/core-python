from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def hello_world():
    return 'Hello World'

def welcome_user():
    return "Welcome Users .... "

app.add_url_rule('/',  view_func=hello_world)
app.add_url_rule('/hi', view_func=welcome_user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1900, debug=True)