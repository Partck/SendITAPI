
from flask import request, make_response, jsonify
from werkzeug.security import check_password_hash
import re
from flask_restful import Resource
from SendITapp.api.v2.models.users import UserModel
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity



class Register(Resource):
    """Handle user CRUD."""

    def post(self):
        """Create user."""
        data = request.get_json() or {}
        user = UserModel()

        if not data:
            return "Please fill in the fields"
        
        username = data["username"].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", username)):
            message = 'Incorrect username.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer

        if data['username'] == "":
            message = 'Check your username'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer

        if data['name'] == "":
            message = 'Enter your name'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        
        name = data["name"].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", name)):
            message = 'Check your name.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
             
        if data["email"].find("@") < 2:
            message = 'Incorrect email format'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
                
        if data['password'] == "":
            message = 'Enter your password.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        
        password = data["password"].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", password)):
            message = 'Check your password.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        
        retype_password = data["password"].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", retype_password)):
            message = 'Check your password(s).'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer

        if data['password'] != data["retype_password"]:
            message = 'Passwords do not match.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
                
        if data['role'] != "Admin" and data["role"] != "User":
            message = 'Role input can either be Admin or User'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        
        
        if data['phone'] == "":
            message = 'Enter a valid number.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
        reply_info = user.create_user(data)
        if not reply_info:      
            return "No such credentials"
        if reply_info == "Check you email or password":
            return "Check you email or password"           
        payload = {"Status": "created",
        "User": reply_info}
        answer = make_response(jsonify(payload),200)
        answer.content_type='application/json;charset=utf-8'
        return answer
        
class AllUsers(Resource):
    @jwt_required
    def get(self):
        """Method to get all the parcels."""
        user = UserModel()
        all_users = user.get_all()
        payload = {
            "Status": "Ok",
            "Users": all_users
        }
        answer = make_response(jsonify(payload),200)
        answer.content_type='application/json;charset=utf-8'
        return answer
        
class SingleUser(Resource):
    """Single parcel class."""
    @jwt_required
    def get(self, userid):
        """Get single item."""
        user = UserModel()
        reply_message = False
        userid = str(userid)
        reply_message = user.get_user(userid)

        if reply_message:
            reply = {"Status": "OK", "reply_message": reply_message}
            answer = make_response(jsonify(reply),200)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
        else:
            pack = {"Status": "User does not exist!"}
            return make_response(jsonify(pack), 404)
            

class Login(Resource):
    """This class creates a view for login/authentication"""
    def post(self):
        data = request.get_json() or {}
        if not data:
            return "Please fill in all the fields"
        if data["email"] == "":
            message = 'Enter email'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        if data["email"].find("@") < 2:
            message = 'Incorrect email format'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        if data["password"] == "":
            message = 'Enter your password.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        password = data['password'].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", password)):
            message = 'Check your password.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        user = UserModel()
        email = user.user_details(data["email"])
        if not email:
            return "Check your details"
        if email:
            if email["password"]== data["password"]:
                access_token = create_access_token(identity=email)
                return make_response(jsonify({"message": "Successful login",
                    "token": access_token
                }), 200)
            return "Wrong credentials. Try Again"                            
        return make_response(jsonify({
        "message": "Try again",
        }), 400)