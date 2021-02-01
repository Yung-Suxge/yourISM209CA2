from flask import Flask

app = Flask(__name__)

@app.route ("/")
def home () :
    return '''My name is Emmanuel Orji. This is my CA2 work.
    My GitHub Url is https://github.com/Yung-Suxge'''


if __name__ == "__main__":
    app.run(port=5005)
