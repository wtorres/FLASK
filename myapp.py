# -*- coding: utf-8 -*-
"""
    CRUD DE USUARIO
    ~~~~~~~~~~~~
    A crud example application written with
    Flask and MySQL.
    :copyright: (c) 2017 by Wilmer Torres.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla


app = Flask(__name__)
app.config.from_pyfile('config.py')

# creamos el objeto de base de datos
db = SQLAlchemy(app)

# Vista de Flask
@app.route('/')
def index():
    return redirect('/admin/')


class User(db.Model):
    __tablename_ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35))
    email = db.Column(db.String(40), unique=True)
    status = db.Column(db.String(1))

    def __str__(self):
        return self.name, self.email, self.status

#Create model for class User
class UserAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['name', 'email', 'status']


# Create admin
admin = admin.Admin(app, name='CRUD CON SQLALCHEMY', template_mode='bootstrap2')
admin.add_view(UserAdmin(User, db.session))


if __name__ == '__main__':
    app.run(debug=True)
