from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>🚀 Flask rodando no Azure App Service!</h2>"

@app.route("/api")
def api():
    return jsonify({"mensagem": "Olá, mundo!", "ambiente": os.getenv("AZURE_ENV", "local")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
