from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #encargado de encriptar la contraseña
import re
EMAILREGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$') #Expresion regular de email

class User:
    def __init__(self, data):

        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    
    @classmethod
    def save(cls, form):
        query = "insert into users(first_name, last_name, email, password) values (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL("foro_publicaciones").query_db(query, form)
    
    @classmethod
    def get_by_email(cls, form):
        query = "select * from users where email = %(email)s;"
        result = connectToMySQL("foro_publicaciones").query_db(query, form)

        if len(result) < 1:
            return False
        else:
            return cls(result[0])
        
    @classmethod
    def get_by_name(cls, form):
        query = "select * from users where id = %(id)s;"
        result = connectToMySQL("foro_publicaciones").query_db(query, form)
        return cls(result[0])

    @staticmethod
    def validate_user(form):
        is_valid = True
        if len(form["first_name"]) < 2:
            flash("first name must have at leats 2 character", "register")
            is_valid = False

        if len(form["last_name"]) < 2:
            flash("last name must have at leats 2 character", "register")
            is_valid = False

        if len(form["password"]) < 6:
            flash("password must have at leats 2 character", "register")   
            is_valid = False

        query = "select * from users where email = %(email)s"
        result = connectToMySQL("login_registro").query_db(query, form)
        if len(result) >= 1:
            flash("E-mail alredy registred", "register") 
            is_valid = False
        
        if form["password"] != form["confirm"]:
            flash("Passwords do not match", "register")   
            is_valid = False

        if not EMAILREGEX.match(form["email"]):
            flash("Email not valid", "register")   
            is_valid = False

        return is_valid
