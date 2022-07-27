from flask import Flask, render_template
from datetime import datetime
app = Flask("hello")

posts = [
    {
        "title": "O meu primeiro post", 
        "body": "Aqui é o texto do post",
        "author": "Feulo",
        "created": datetime(2022,7,25)
    },
    {
        "title": "O meu segundo post", 
        "body": "Aqui é o texto do post",
        "author": "Danilo",
        "created": datetime(2022,7,26)
    },
]
# é uma lista de dicionários dentro
@app.route("/")  # cria uma rota na raiz
def index():
    return render_template("index.html", posts = posts)


