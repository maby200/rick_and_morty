from flask import Blueprint, render_template, redirect, request, flash
from app.models.rick_y_morty import Personajes
from app.db import db
from app.requests import Request


rick_y_morty = Blueprint('rick_y_morty', __name__)


@rick_y_morty.route('/')
def index():
    personajes=Personajes()

    return render_template('index.html',personajes=personajes)


@rick_y_morty.route('/insertar-personaje')
def insertar_personaje():
    personajes = Request()
    db.personajes.insert_many(personajes.characters())
    # db.personajes.insert_one(personajes[0])
    


@rick_y_morty.route('/perfil')
def profile():
    
    pass