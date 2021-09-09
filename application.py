# Librería para conectar con la variable de entorno
import os

from flask import Flask, session, request, redirect, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required

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

# Esta sección de código registra a un usuario en el sitio WEB proveyendo un nombre de usuario y una contraseña.
# Ejecuta el inicio de sesión y el cierre de sesión del usuario registrado en el sitio WEB.

# Enrutamiento a Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not email:
            return apology("No se ha podido encontrar tu cuenta de usuario")

        elif not password:
            return apology("Su contraseña es incorrecta. Inténtelo nuevamente")

        elif not confirmation:
            return apology("La confirmación del password no coincide con el anterior")

        elif password != confirmation:
            return apology("Las contraseñas no coinciden")

        USER_ID = 0

        validar = db.execute("SELECT count(email) as total FROM users WHERE email = :email", {"email":email}).mappings().all()
        print(type(validar))
        print(validar)
        if validar[0]["total"] == 1:
            return apology("Este usuario ya existe")

        try:
            USER_ID = db.execute("insert into users(name, last_name, email, password, confirmation) values(:NAME, :LASTNAME, :EMAIL, :PASSWORD, :CONFIRMATION) returning id_users",
                                 {"NAME" :name, "LASTNAME" :last_name, "EMAIL" :email, "PASSWORD" :generate_password_hash(password), "CONFIRMATION" :confirmation})
            print(USER_ID)
            session["user_id"] = dict(USER_ID.fetchone())["id_users"]
            db.commit()
            return redirect("/")

        except Exception as a:
            print(a)
            return apology("El nombre de usuario ya existe")
        
    else:
        return render_template("register.html")
