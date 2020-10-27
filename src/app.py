from flask import Flask
from src.controllers.controller import controller_blueprint

app = Flask(__name__)

app.register_blueprint(controller_blueprint, url_prefix='/controller')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/route/<username>', methods=['GET', 'POST'])
def route(username):
    return {
        "username": username,
        "theme": "User Theme",
    }


if __name__ == '__main__':
    app.run()
