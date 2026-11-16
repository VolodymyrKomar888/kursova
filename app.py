import yaml
from flask import Flask, jsonify

app = Flask(__name__)

with open("config.yaml", encoding="utf-8") as f:
    config = yaml.safe_load(f)


@app.route("/")
def index():
    return jsonify(app=config["app_name"], version=config["version"])


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
