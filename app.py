from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


SECRET_KEY = os.getenv("example_env_gitignore")


secret = [
    {
        "message": SECRET_KEY
    }
]

@app.route("/example", methods=['GET'])
def get_secret_message():
    return jsonify(secret)

if __name__ == '__main__':
    app.run(debug=True)
