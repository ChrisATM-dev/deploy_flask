from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #encargado de encriptar la contraseña

from flask_app.models.comment import Comment


class Post:
    def __init__(self, data):

        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

        self.user_name = data["user_name"]

        self.comments = data["comments"]


    
    @classmethod
    def save(cls, form):
        query = "insert into posts(content, user_id) values (%(content)s, %(user_id)s);"
        return connectToMySQL("foro_publicaciones").query_db(query, form)
    
    @staticmethod
    def validate_post(form):
        is_valid = True
        if len(form["content"]) < 2:
            flash("El contenido es valido", "post")
            is_valid = False

        return is_valid
    
    @classmethod
    def get_all(cls):
        print("obteniendo todos los post")
        query = "select posts.*, users.first_name as user_name from posts join users on posts.user_id = users.id order by posts.created_at desc;"
        results = connectToMySQL("foro_publicaciones").query_db(query)
        posts = []
        for post in results:
            lista_comentarios = Post.get_all_comment(post["id"])
            post["comments"] = lista_comentarios
            posts.append(cls(post))
        return posts

    @classmethod
    def delete(cls, form):
        print(form)
        query = "delete from posts where id = %(id)s"
        return connectToMySQL("foro_publicaciones").query_db(query, form)
    
    @staticmethod
    def get_all_comment(id):
        query = f"select comments.*, users.first_name as user_name from comments join users on comments.user_id = users.id where comments.post_id = {id};"
        results = connectToMySQL("foro_publicaciones").query_db(query)
        comentarios = []
        for comentario in results:
            comentarios.append(Comment(comentario))
        return comentarios
    
