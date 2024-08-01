from flask import render_template, request, jsonify
from database.db import add_user

def func_home_page():
    return render_template("home.html")

def func_register_page():
    return render_template("register.html")

def func_consult_page():
    return render_template("consult.html")

def func_register_user():
    try:
        Id = request.form["Id"]
        Nombre = request.form["Nombre"]
        Apellido = request.form["Apellido"]
        Cumpleaños = request.form["Cumpleaños"]
        
        # Add user to the database
        confirm_user = add_user(Id, Nombre, Apellido, Cumpleaños)
        
        if confirm_user:
            return "The user was successfully created", 201
        else:
            return "The user was not created", 400
    
    except KeyError as e:
        return f"Missing required field: {str(e)}", 400
    except Exception as e:
        return f"An error occurred: {str(e)}", 500


def func_consult_user():
    obj_user = request.get_json()
    id = obj_user["id"]
    consult_user(id)
    return "ok"