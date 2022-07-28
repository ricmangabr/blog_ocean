from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask("hello")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"    # é um link para um banco na minha pasta
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False   # melhora a performance das consultas ao banco de dados

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)   # definida a coluna, o tipo de dado, indica que é a chave primária e numera automaticamante
    title = db.Column(db.String(70), nullable=False)   #string, não pode ser nulo
    body = db.Column(db.String(500)) # tamanho até 500 caracteres, podendo ser vazio
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id =db.Column(db.Integer, db.ForeignKey('users.id'))

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='author')

db.create_all()

@app.route("/")  # cria uma rota na raiz
def index():
    posts = Post.query.all()
    return render_template("index.html", posts = posts)

@app.route("/populate")   
def populate():
    user = User(username="feulo", email= "gag.com", pasword_hash= "a")
    post1 = Post(title="Post 1", body="Texto do post", author=user)
    post2 = Post(title="Post 2", body="Texto do post", author=user)
    post3 = Post(title="Post 3", body="Texto do post", author=user)
    db.session.add(user)
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.commit()
    return redirect(url_for('index'))
