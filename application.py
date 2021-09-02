# Librería para conectar con la variable de entorno
import os

from flask import Flask, session, request, redirect, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#Inicialización de aplicción Flask
app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Enrutamiento al index
@app.route("/")
def index():
    return render_template("index.html")

# Enrutamiento a Register
@app.route("/register")
def register():
    return render_template("register.html")

# Enrutamiento al Sign in
@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")

# Enrutamiento a Offers
@app.route("/offers")
def offers():
    return render_template("offers.html")

# Enrutamiento a Novelties
@app.route("/novelties")
def novelties():
    return render_template("novelties.html")

# Enrutamiento a Best Sellers
@app.route("/bestsellers")
def bestsellers():
    return render_template("bestsellers.html")

# Enrutamiento a Help
@app.route("/help")
def help():
    return render_template("help.html")
