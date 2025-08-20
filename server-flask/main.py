from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app) #enable CORS in all routes

#pruebas
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/api/users')
def get_users():
    return {
        "users": ["Alice", "Bob", "Charlie"]
    }


if __name__ == '__main__':
    app.run(debug=True) #By Default runs in port 5000