from flask import Flask,jsonify,request,make_response
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import json
from pytz import utc
from datetime import datetime 

app = Flask(__name__)
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config ['SQLALCHEMY_DATABASE_URI'] = "postgresql://wwdvjxfnarrfgi:1ca950510df44652e0ead171affb4ae982837e7deefbaa21efb494462f330a88@ec2-44-205-41-76.compute-1.amazonaws.com:5432/d7hv5jt6s3aits"
else:
    app.debug = False
    app.config ['SQLALCHEMY_DATABASE_URI'] = "postgresql://wwdvjxfnarrfgi:1ca950510df44652e0ead171affb4ae982837e7deefbaa21efb494462f330a88@ec2-44-205-41-76.compute-1.amazonaws.com:5432/d7hv5jt6s3aits"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    passport = db.Column(db.String(100), unique = True, nullable = False)
    register = db.Column(db.Integer, nullable = False)
    status = db.Column(db.String(100))
    eyeCondition = db.Column(db.String(100))



class Checkin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    time = db.Column(db.DateTime(timezone=True),
                           default=datetime.utcnow)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    place = db.Column(db.String(100))


@app.route('/')
def hello_world():
    return 'Hello Sammy!'

@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }
        
        return jsonify(data)
@app.route('/register', methods = ['GET','POST'])
def register():
    print("in")
    if(request.method == 'POST'):
        form = json.loads(request.data)
        email = form["email"]
        password = form["password"]
        name = form["name"]
        passport = form["passport"]
        user = User.query.filter_by(email=email).first()
        if user:
            return make_response(json.dumps('Email already exists!')), 400
        else:
            new_user = User(email=email,
                            password = password,
                            name = name,
                            passport = passport,
                            register = 0,
                            )
            db.session.add(new_user)
            db.session.commit()
            # login_user(new_user, remember=True)
            
            return make_response(json.dumps('Successfully registered')), 200

@app.route('/login', methods = ['GET','POST'])
def login():
    if(request.method == 'POST'):
        form = json.loads(request.data)
        email = form["email"]
        password = form['password']
        user = User.query.filter_by(email=email).first()
        if user:

            if(user.password == password):

                return make_response(json.dumps("Login Successfull")),200
            else:
                return make_response(json.dumps('Incorrect password'))
        else:
            return make_response(json.dumps('Email does not exist!'))

@app.route('/checkin', methods = ['GET','POST'])
def checkin():
    if(request.method == 'POST'):
        form = json.loads(request.data)
        place = form["place"]
        user = form["user"]
        userid = User.query.filter_by(passport = user).first()
        if(userid):
            print(place, userid.id)
            new_checkin = Checkin(  place = place,
                                    user = userid.id,
                                )
            db.session.add(new_checkin)
            db.session.commit()
            return make_response(json.dumps('Successfully Check in')), 200
        else:
            return make_response(json.dumps("Unsuccessful Check in"))

@app.route('/getuser', methods = ['GET'])
def getUser():
    if(request.method == 'GET'):
        user = User.query.all()
        name = []
        for i in user:
            name.append(i.passport)
        print(name)
        return jsonify(name)

@app.route('/checkregistered', methods = ['POST'])
def checkRegistered():
    if(request.method == 'POST'):
        form = json.loads(request.data)
        passport = form["passport"]
        userid = User.query.filter_by(passport = passport).first()

        if(userid):
            print(userid.register)
            if(userid.register == 0):
                return make_response(json.dumps("1"))
            else:
                return make_response(json.dumps("0"))
        else : 
            return make_response(json.dumps("2"))

if __name__ == "__main__":
    app.run(debug=True)


