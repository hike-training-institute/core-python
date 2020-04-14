from flask import Flask

app = Flask(__name__)

def hello_world():
    return 'Hello World'

def welcome_user():
    return "Welcome Users .... "

app.add_url_rule('/',  view_func=hello_world)
app.add_url_rule('/hi', view_func=welcome_user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1900)