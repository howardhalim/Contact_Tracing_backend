# from flask import Flask,jsonify,request,make_response
# from flask_sqlalchemy import SQLAlchemy
# from itsdangerous import json
# from flask_login import login_user, logout_user, login_required, current_user
# from flask_cors import CORS, cross_origin
# from sqlalchemy import func

# app =   Flask(__name__)
# # CORS(app)
# # # app.config['CORS_HEADERS'] = 'Content-Type'
# # # app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/database'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)

# # # class Student(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     firstname = db.Column(db.String(100), nullable=False)
# # #     lastname = db.Column(db.String(100), nullable=False)
# # #     email = db.Column(db.String(80), unique=True, nullable=False)
# # #     age = db.Column(db.Integer)
    
# # #     bio = db.Column(db.Text)

# # #     def __repr__(self):
# # #         return f'<Student {self.firstname}>'

# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key = True)
# #     email = db.Column(db.String(100), unique = True, nullable = False)
# #     password = db.Column(db.String(100), nullable = False)
# #     name = db.Column(db.String(100), nullable = False)
# #     passport = db.Column(db.String(100), unique = True, nullable = False)
# #     register = db.Column(db.Integer, nullable = False)
# #     status = db.Column(db.String(100))
# #     eyeCondition = db.Column(db.String(100))



# # class Checkin(db.Model):
# #     id = db.Column(db.Integer, primary_key = True)
# #     time = db.Column(db.DateTime(timezone=True),
# #                            server_default=func.now())
# #     user = db.Column(db.Integer, db.ForeignKey('user.id'))
# #     place = db.Column(db.String(100))



# # db.create_all()
# @app.route('/returnjson', methods = ['GET'])
# @cross_origin()
# def ReturnJSON():
#     if(request.method == 'GET'):
#         data = {
#             "Modules" : 15,
#             "Subject" : "Data Structures and Algorithms",
#         }
        
#         return jsonify(data)

# # @app.route('/register', methods = ['GET','POST'])
# # def register():
# #     print("in")
# #     if(request.method == 'POST'):
# #         form = json.loads(request.data)
# #         email = form["email"]
# #         password = form["password"]
# #         name = form["name"]
# #         passport = form["passport"]
# #         user = User.query.filter_by(email=email).first()
# #         if user:
# #             return make_response(json.dumps('Email already exists!')), 400
# #         else:
# #             new_user = User(email=email,
# #                             password = password,
# #                             name = name,
# #                             passport = passport,
# #                             register = 0,
# #                             )
# #             db.session.add(new_user)
# #             db.session.commit()
# #             # login_user(new_user, remember=True)
            
# #             return make_response(json.dumps('Successfully registered')), 200

# # @app.route('/login', methods = ['GET','POST'])
# # def login():
# #     if(request.method == 'POST'):
# #         form = json.loads(request.data)
# #         email = form["email"]
# #         password = form['password']
# #         user = User.query.filter_by(email=email).first()
# #         if user:

# #             if(user.password == password):

# #                 return make_response(json.dumps("Login Successfull")),200
# #             else:
# #                 return make_response(json.dumps('Incorrect password'))
# #         else:
# #             return make_response(json.dumps('Email does not exist!'))

# # @app.route('/checkin', methods = ['GET','POST'])
# # def checkin():
# #     if(request.method == 'POST'):
# #         form = json.loads(request.data)
# #         place = form["place"]
# #         user = form["user"]
# #         userid = User.query.filter_by(passport = user).first()
# #         if(userid):
# #             print(place, userid.id)
# #             new_checkin = Checkin(  place = place,
# #                                     user = userid.id,
# #                                 )
# #             db.session.add(new_checkin)
# #             db.session.commit()
# #             return make_response(json.dumps('Successfully Check in')), 200
# #         else:
# #             return make_response(json.dumps("Unsuccessful Check in"))

# # @app.route('/getuser', methods = ['GET'])
# # def getUser():
# #     if(request.method == 'GET'):
# #         user = User.query.all()
# #         name = []
# #         for i in user:
# #             name.append(i.passport)
# #         print(name)
# #         return jsonify(name)

# # @app.route('/checkregistered', methods = ['POST'])
# # def checkRegistered():
# #     if(request.method == 'POST'):
# #         form = json.loads(request.data)
# #         passport = form["passport"]
# #         userid = User.query.filter_by(passport = passport).first()

# #         if(userid):
# #             print(userid.register)
# #             if(userid.register == 0):
# #                 return make_response(json.dumps("1"))
# #             else:
# #                 return make_response(json.dumps("0"))
# #         else : 
# #             return make_response(json.dumps("2"))
# # @app.route('/', methods = ['POST'])
# # def test():
# #     student_john = Student(firstname='howard', lastname='halim',
# #                        email='howard@gmail.com', age=21,
# #                        bio='Biologysad student')
# #     db.session.add(student_john)
# #     db.session.commit()
# #     return make_response(json.dumps("SUCCESS"), 200)

# # @app.route('/', methods =['GET'])
# # def ret():
# #     students = Student.query.all()
# #     data = []
# #     for row in students:
# #         data.append(row.firstname)
# #     print(jsonify(data))
# #     return make_response(json.dumps(data),200)


# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Sammy!'