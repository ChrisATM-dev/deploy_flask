from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #encargado de encriptar la contraseña


class Comment:
    def __init__(self, data):

        self.id = data["id"]
        self.post_id = data["post_id"]
        self.user_id = data["user_id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.user_name = data["user_name"]


    @classmethod
    def guardar_comentario(cls, form):
        print("guardando el comentario")
        query = "insert into comments(post_id, user_id, content) values (%(post_id)s, %(user_id)s, %(content)s);"
        return connectToMySQL("foro_publicaciones").query_db(query, form)

    
