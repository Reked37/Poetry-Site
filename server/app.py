from flask import jsonify, make_response
from flask_restful import Resource
from config import app, db, api
from models import User, Comment, Poem

@app.route('/')
def home():
    return '<h1>Home Page<h1>'