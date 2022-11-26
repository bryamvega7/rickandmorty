from flask import Blueprint,render_template,redirect,url_for
from app.db import db

personajes_ruta = Blueprint('libros_ruta',__name__)

@personajes_ruta.route('/') #Mostrar la tabla
def index():
    personajes = db.personajes.find()
    return render_template('index.html',personajes=personajes)

@personajes_ruta.route('/crear-personaje',methods=['POST','GET']) #Crear un libro
def guardar_personaje():
        #
        db.personaje.insert_one(nuevo_personaje.to_json())

    