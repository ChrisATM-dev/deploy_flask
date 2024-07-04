from flask import Flask, render_template, redirect, request, session

from flask_app import app

from flask_app.models.user import User
from flask_app.models.post import Post

from flask_bcrypt import Bcrypt

from flask import flash 

bcrypt = Bcrypt(app)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods = ["POST"])
def registred():
    # metodo para validar la info
    if not User.validate_user(request.form):
        return redirect("/")
    # encriptar contraseña
    pass_hash = bcrypt.generate_password_hash(request.form["password"])
    # crear diccionario
    form = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pass_hash
    }
    id = User.save(form) # recibe el id del nuevo registro
    session["user_id"] = id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    
    dicc = {"id": session["user_id"]}
    user = User.get_by_name(dicc)

    posts = Post.get_all()

    print(posts[0].comments)


    return render_template("dashboard.html", user = user, posts = posts)


@app.route("/login", methods = ["POST"])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("E-mail not found", "login")
        return redirect("/")

    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Password is incorrect", "login")
        return redirect("/")
    
    session["user_id"] = user.id

    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


