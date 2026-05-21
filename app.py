from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello CI/CD Pipeline!"

if _name_ == "__main__":
    app.run(host="0.0.0.0", port=5000)
