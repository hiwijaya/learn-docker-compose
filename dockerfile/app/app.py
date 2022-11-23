# https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>FLASK-APPLICATION</h1>'


if __name__ == "__main__":
    app.run(debug=True)
