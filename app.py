#this is like a boilerplate
from flask import Flask, render_template, request, url_for, redirect



# app = Flask(__name__)

# @app.route('/') #we can write many such route for different webpage
# def home():
#     return 'This is Home Page'

# if __name__ == "__main__": 
#     app.run(debug=True) # we can change post by writing it like- app.run(debug=True, port=3000)



## flask have something render template, for render template to work
#   you much have template folder inside which you have html folder
#   u have to import render template functionality from flask

# app = Flask(__name__)

# @app.route('/home') 
# def home2():
#     return render_template('home.html') #it will show html data 

# if __name__ == "__main__": 
#     app.run(debug=True)


## similar example like above one
# app = Flask(__name__)

# @app.route('/home') 
# def home2():
#     return render_template('home.html', item1="attribute1", item2="attribute2") # we can add attribute here

# if __name__ == "__main__": 
#     app.run(debug=True)




## forms 
#for this we have to import request from flask
# app = Flask(__name__)

# @app.route('/home', methods=['GET', 'POST']) #we add post and get method to show form
# def home2():

#     if request.method == 'GET':
#         return render_template('home.html')
#     elif request.method == 'POST':
#         return request.form
    
# if __name__ == "__main__": 
#     app.run(debug=True)





# NOW WE WILL LEARN SQLALCHEMY(LIKE HTML NOW WE WILL WORK ON DATABASES iN PYTHON)

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy  #sqlalchemy is a library which helps us to work with database in python
# from models import db, User, Role, Association #this is the model class which will help us to create table in database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manymany.db' #this is the path where our database will be stored, we can also use mysql or postgresql but for that we have to install their library
db=SQLAlchemy(app) #this is the object of SQLAlchemy class which will help us to work with database

app.app_context().push() #this is used to avoid the error of working outside application context

# =======Controllers for Role Model Frist==========
#child table
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)
#     role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False) #this is the foreign key which will help us to create relationship between user and role table

#parent table
# class Role(db.Model):  #if class name is Role then table name will be role by default, if we want to change it then we can use __tablename__ = 'role_table' in class
#     id = db.Column(db.Integer, primary_key=True)
#     role_name = db.Column(db.String(80), unique=True, nullable=False) #this is the relationship between user and role table, backref is used to create a new property in user table which will help us to access role table from user table, lazy is used to load the data from role table when we access it from user table
#     users = db.relationship('User', backref='role')


#======manyone=======


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    roles = db.relationship('Role', secondary='association', backref=db.backref('users', lazy=True)) #this is the relationship between user and role table, backref is used to create a new property in user table which will help us to access role table from user table, lazy is used to load the data from role table when we access it from user table 

class Role(db.Model):  #if class name is Role then table name will be role by default, if we want to change it then we can use __tablename__ = 'role_table' in class
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False) #this is the relationship between user and role table, backref is used to create a new property in user table which will help us to access role table from user table, lazy is used to load the data from role table when we access it from user table

class association(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

db.create_all()

@app.route('/')
def home():
    roles = Role.query.all()
    return render_template('index.html', roles=roles)

@app.route('/add', methods=['POST'])
def add_role():
    role_name = request.form.get('role_name')
    if role_name:
        new_role = Role(role_name=role_name)
        db.session.add(new_role)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_role(id):
    role = Role.query.get_or_404(id)
    if request.method == 'POST':
        role_name = request.form.get('role_name')
        if role_name:
            role.role_name = role_name
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit.html', role=role)

@app.route('/delete/<int:id>')
def delete_role(id):
    role = Role.query.get(id)
    if role:
        db.session.delete(role)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)





