from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    hrbet = db.relationship('Hrbet')
    prsa = db.relationship('Prsa')
    noge = db.relationship('Noge')
    ramena = db.relationship('Ramena')
    roke = db.relationship('Roke')
    zapiski = db.relationship('Zapiski')

class Hrbet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(255))
    mimetype = db.Column(db.String(50), nullable=False)
    data = db.Column(db.LargeBinary, nullable = False)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Model ni uporabljen, bil je namenjen za preizkušanje



class Prsa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(255), nullable = False)
    mimetype = db.Column(db.String(50), nullable=False)
    data = db.Column(db.LargeBinary, nullable = False)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Model ni uporabljen, bil je namenjen za preizkušanje

class Noge(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(255), nullable = False)
    mimetype = db.Column(db.String(50), nullable=False)
    data = db.Column(db.LargeBinary, nullable = False)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Model ni uporabljen, bil je namenjen za preizkušanje



class Ramena(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(255), nullable = False)
    mimetype = db.Column(db.String(50), nullable=False)
    data = db.Column(db.LargeBinary, nullable = False)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Model ni uporabljen, bil je namenjen za preizkušanje


class Roke(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(255))
    mimetype = db.Column(db.String(50), nullable=False)
    data = db.Column(db.LargeBinary, nullable = False)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Model ni uporabljen, bil je namenjen za preizkušanje

class Zapiski(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Model ni uporabljen, bil je namenjen za preizkušanje


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    message = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Model ni uporabljen, bil je namenjen za preizkušanje

class Hrbet_slike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    message = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Model ni uporabljen, bil je namenjen za preizkušanje

class Vrsta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime_vaje = db.Column(db.String(255), nullable=False, unique=True)
    vaje = db.relationship('Vaje', backref='vrsta', lazy=True)



class Vaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opis_vaje = db.Column(db.Text)
    slika = db.Column(db.String(255), nullable=False)
    vrsta_id = db.Column(db.Integer, db.ForeignKey('vrsta.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user = db.relationship('User', backref='vaje', lazy=True)
    

    



