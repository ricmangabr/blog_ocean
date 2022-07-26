from flask import Flask, render_template

app = Flask("hello")

@app.route("/")  # cria uma rota na raiz

def hello(): #cria
    return "Hello world!"

@app.route("/meucontato") #outra rota para contato
def meuContato():
    return render_template('index.html') 
    