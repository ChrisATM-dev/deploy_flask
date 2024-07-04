from flask import Flask, render_template, redirect, request, session

from flask_app import app

from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.comment import Comment

from flask_bcrypt import Bcrypt

from flask import flash 

bcrypt = Bcrypt(app)


@app.route("/guardar_comentario", methods = ["POST"])
def crear_comment():

    Comment.guardar_comentario(request.form)
    return redirect("/dashboard")




