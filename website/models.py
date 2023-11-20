from pickle import TRUE
from sqlalchemy import true
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(150),unique=True)
    registernumber=db.Column(db.Integer,unique=True)
    email=db.Column(db.String(150),unique=True)
    phonenumber=db.Column(db.String(15),unique=True)
    department=db.Column(db.String(25))
    graduationyear=db.Column(db.String(15))
    password=db.Column(db.String(150))
    books=db.relationship('Book')


class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    bookname=db.Column(db.String(40))
    authorname=db.Column(db.String(40))
    genre=db.Column(db.String(40))
    review=db.Column(db.String(100))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
