from sqlalchemy import MetaData. ForeignKey, Column, Table
from sqlalchemy.orm import validates, relationship
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db

class Poem(db.Model, SerializerMixin):
    __tablename__='poems'

    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String, nullable=False)
    body= db.Column(db.String, nullable=False)

    user= db.relationship('User', back_populates='poems')
    user_id= db.Column(db.String, nullable=False)

    comment=db.relationship('Comment', back_populates='poems')
    comment_id=db.Column(db.String)

    serialize_rules=('-comments', '-users')

    def __repr__(self):
        return f'Poem(id: {self.id} title:{self.title} body:{self.body})'

class Comment (db.Model, SerializerMixin):
    __tablename__='comments'

    id= db.Column(db.String, primary_key=True)
    comment= db.Column(db.String, nullable=False)

    user= db.relationship('User', back_populates='comments')
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

    poem=db.relationship('Poem', back_populates='comments')
    poem_id=db.Column(db.Integer)

    serialize_rules=('-users', '-poems')

     def __repr__(self):
        return f'Comment(id: {self.id} comment:{self.comment})'

class User (db.Model, SerializerMixin):
    __tablename__= 'users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)

    poem= db.relationship('Poem', back_populates='users')
    poem_id=db.Column(db.Integer)

    comment= db.relationship('Comment', back_populates='users')
    comment_id= db.Column(db.String)

    serialize_rules=('-comments', '-poems')

     def __repr__(self):
        return f'User(id: {self.id} username:{self.username} password:{self.password})'
