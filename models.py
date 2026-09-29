from flask_sqlalchemy import SQLAlchemy  #sqlalchemy is a library which helps us to work with database in python
db = SQLAlchemy() #this is the object of SQLAlchemy class which will help us to work with database




class User(db.Model): #this is the model class which will help us to create table in database
    id = db.Column(db.Integer, primary_key=True) #this is the primary key of the table
    username = db.Column(db.String(20), unique=True, nullable=False) #this is
    password = db.Column(db.String(60), nullable=False) #this is the password column of the table

class Role(db.Model): #this is the model class which will help us to create table in database
    id = db.Column(db.Integer, primary_key=True) #this is the primary key of the table
    role_name = db.Column(db.String(20), unique=True, nullable=False) #this is the name column of the table

class Association(db.Model): #this is the model class which will help us to create table in database
    id = db.Column(db.Integer, primary_key=True) #this is the primary key of the table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #this is the foreign key column of the table
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False) #this is the foreign key column of the table



