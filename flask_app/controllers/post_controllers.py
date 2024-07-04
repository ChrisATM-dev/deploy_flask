from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.post import Post





@app.route("/create_post", methods = ["POST"])
def crear_post():

    if not Post.validate_post(request.form):
        return redirect("/dashboard")
    
    Post.save(request.form)
    return redirect("/dashboard")

@app.route("/delete_post/<int:id>")
def delete_post(id):
    
    Post.delete({"id": id})

    return redirect("/dashboard")