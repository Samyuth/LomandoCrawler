from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def get_leveled_tree():
    output = []

    with open("leveled_tree.json", "r") as infile:
        output = json.loads(infile.read())

    return jsonify(output)

if __name__ == "__main__":
    app.run(port = 5000)