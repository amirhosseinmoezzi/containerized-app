from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_there():
    return '<h1>Hello from Flask inside a container</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)