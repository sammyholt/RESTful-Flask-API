from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Please see the README.md at https://github.com/sammyholt/RESTful-Flask-API for information about this API."})

if __name__ == '__main__':
    app.run(debug=True)