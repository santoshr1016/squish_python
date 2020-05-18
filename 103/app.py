from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Float
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# I am configuring my database here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')
app.config['JWT_SECRET_KEY'] = 'secure-secret'

# This is initializing the database, before start using it, this is constructor, Now make the models, ie classes
db = SQLAlchemy(app)
mm = Marshmallow(app)
jwt = JWTManager(app)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database Created")


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database Destroyed')


@app.cli.command('db_seed')
def db_seed():
    mercury = Planet(planet_name='Mercury',
                     planet_type='Class D',
                     home_star='Sun',
                     mass=3.258e23,
                     radius=1516,
                     distance=35.34e98
                     )
    venus = Planet(planet_name='Venus',
                   planet_type='Class K',
                   home_star='Sun',
                   mass=4.258e23,
                   radius=3716,
                   distance=67.24e34
                   )

    earth = Planet(planet_name='Earth',
                   planet_type='Class M',
                   home_star='Sun',
                   mass=5.258e23,
                   radius=3959,
                   distance=92.9e53
                   )

    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)

    test_user = User(first_name='Santosh',
                     last_name='Kumar',
                     email='san@example.com',
                     password="secret"
                     )
    db.session.add(test_user)
    db.session.commit()
    print("Database Seeded")


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/ping')
def ping():
    return jsonify(message='The response for /ping endpoint  is Pong')


@app.route('/not_found')
def not_found():
    return jsonify(message='The resource is not found'), 404


# localhost:5000/params?name=santosh&age=2
@app.route('/params')
def param():
    name = request.args.get('name')
    age = int(request.args.get('age'))

    if age < 18:
        return jsonify(message='Hello ' + name + ', You are under age'), 401
    else:
        return jsonify(message="Welcome to the club, " + name)


# localhost:5000/url_param/santosh/2
@app.route('/url_param/<string:name>/<int:age>')
def url_param(name: str, age: int):
    if age < 18:
        return jsonify(message='Hello ' + name + ', You are under age'), 401
    else:
        return jsonify(message="Welcome to the club, " + name)


@app.route('/planets', methods=['GET'])
def planets():
    planet_list = Planet.query.all()

    result = planets_schema.dump(planet_list)

    return jsonify(result)


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    test = User.query.filter_by(email=email).first()
    if test:
        return jsonify(message='The user email {}, already exists'.format(email)), 409
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message='The new user with email {}, Added successfully'.format(email)), 201


@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']

    test = User.query.filter_by(email=email, password=password).first()
    if test:
        access_token = create_access_token(identity=email)
        return jsonify(message='Login Successful', access_token=access_token)
    else:
        return jsonify(message='You entered bad email and password'), 401


# Database models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


# Marshmallow serialization
class UserSchema(mm.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class PlanetSchema(mm.Schema):
    class Meta:
        fields = ('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)


if __name__ == '__main__':
    app.run(debug=True)
