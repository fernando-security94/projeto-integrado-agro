from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Isso conecta o app ao ngrok

@app.route("/")
def home():
    return "<h1>Olá, mundo com Flask!</h1><p>Essa página veio do Python 😎</p>"

if __name__ == "__main__":
    app.run()
