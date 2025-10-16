from flask import Flask

apka = Flask(__name__)

@apka.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    apka.run(host="0.0.0.0", port=8000)
