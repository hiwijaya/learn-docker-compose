from flask import Flask, Response
app = Flask(__name__)

counter = 0

@app.route('/')
def main():
    return '<h1>FLASK-APPLICATION</h1>'

@app.route('/health')
def health():

    global counter
    counter = counter + 1
    
    if counter > 5:
        return Response("unhealty", status=500)
    else:
        return 'OK'


if __name__ == "__main__":
    app.run(debug=True)
