
from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <h1>Jovian Careers</h1>
    <p>Welcome to the Jovian Careers Website</p>
    """

if __name__ == "__main__":
    cli = sys.modules['flask.cli']
    cli.show_server_banner = lambda *x: None
    app.run(host='0.0.0.0', port=5000, log_level='ERROR')
