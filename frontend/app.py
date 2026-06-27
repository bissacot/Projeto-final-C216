from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "http://backend:8000"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/categorias")
def categorias():
    response = requests.get(f"{API_URL}/categorias/")
    categorias = response.json()
    return render_template("categorias.html", categorias=categorias)


@app.route("/produtos")
def produtos():
    response = requests.get(f"{API_URL}/produtos/")
    produtos = response.json()
    return render_template("produtos.html", produtos=produtos)


@app.route("/vendas")
def vendas():
    response = requests.get(f"{API_URL}/vendas/")
    vendas = response.json()
    return render_template("vendas.html", vendas=vendas)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)