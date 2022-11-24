from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1>FLASK-APPLICATION</h1>'

@app.route('/ping')
def ping():
    return 'You are in mode ' + os.getenv('MODE', 'local')


if __name__ == "__main__":
    app.run(debug=True)
