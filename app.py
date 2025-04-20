
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <h1>Jovian Careers</h1>
    <p>Welcome to the Jovian Careers Website</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
