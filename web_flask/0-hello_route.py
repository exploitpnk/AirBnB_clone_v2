from flask import Flask
""" starts a Flask web application """
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbtn():
    """ Show Hello HBNB when / is called """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
