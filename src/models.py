from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email= db.Column(db.String(250), nullable=False, unique=True)
    userName = db.Column(db.String(80), nullable=False, unique=True)
    password= db.Column(db.String(250), nullable=False)
    favorites = db.relationship("Favorite", uselist=True, backref='user') 

    def __repr__(self):
        return '<User %r>' % self.userName
    
    def serialize(self):
        return {

            "id": self.id,
            "email": self.email,
            # do not rerialize the password, its a security breach
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_planeta = db.Column(db.String(80), nullable=False)
    poblacion = db.Column(db.String(250), nullable=False)
    favorites = db.relationship("Favorite", db.ForeignKey("favorites.id"))

class Vehicle(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    vehicle_type = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    favorites = db.relationship("Favorite", db.ForeignKey("favorites.id"))   


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    color_ojos = db.Column(db.String(250), nullable =False)
    favorites = db.relationship("Favorite", db.ForeignKey("favorites.id"))


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    planeta_id = db.Column(db.Integer(), db.ForeignKey("planet.id"))
    people_id = db.Column(db.Integer(), db.ForeignKey("people.id"))
    vehiculos_id = db.Column(db.Integer(), db.ForeignKey("vehiculos.id"))
