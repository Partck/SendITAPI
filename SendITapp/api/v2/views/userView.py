
from flask import request, make_response, jsonify
import re
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from SendITapp.api.v2.models.users import UserModel
from flask_jwt_extended import jwt_required
import bcrypt


class Register(Resource):
    """Handle user CRUD."""

   

    def post(self):
        """Create user."""
        data = request.get_json() or {}
        user = UserModel()


        username = data['username'].strip()
        name = data['name'].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", username)) or\
            not (re.match("^[a-zA-Z0-9_]*$", name)):
            message = 'Check your name and usename'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            

    
        if data["email"].find("@") < 2:
            message = 'Incorrect email format'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            

    
        password = data['password'].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", password)) or \
        data['password'] != data["retype_password"]:
            message = 'Check your password.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            

    
        if data['role'] != "Admin" and data["role"] != "User":
            message = 'Role input can either be Admin or User'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            

    
        if data['phone'] == "":
            message = 'Enter a valid number.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            

        password = bcrypt.hashpw(data["password"], bcrypt.gensalt())
        reply_info = user.create_user(data["username"], data["name"],
         data["email"], data["role"], data["phone"], password)

        if reply_info:
            user_data = [data["username"], data["name"],
            data["email"], data["role"], data["phone"], data["password"]]

            payload = {"Status": "created",
            "User": user_data}
            return make_response(jsonify(payload), 200)
            

        payload = {"Status": "Failed", "Message": reply_info}
        return make_response(jsonify(payload), 400)
        

    @jwt_required
    def get(self):
        """Method to get all the parcels."""
        user1 = UserModel()
        all_users = user1.get_all()

        payload = {
            "Status": "Ok",
            "Users": all_users
        }
        return make_response(jsonify(payload), 200)
        


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
            return make_response(jsonify(reply), 200)
            
        else:
            pack = {"Status": "User does not exist!"}
            return make_response(jsonify(pack), 404)
            


class Login(Resource):
    """This class creates a view for login/authentication"""

    def post(self):
        data = request.get_json() or {}
        
        if data["email"].find("@") < 2:
            message = 'Incorrect email format'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            

    
        password = data['password'].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", password)):
            message = 'Check your password.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            
        
        user = UserModel()
        email = data["email"]
        password = data["password"]
        auth = user.user_login(email)
        
        if auth:
            access_token = create_access_token(identity=email)
            return make_response(jsonify({"message": "Successful login",
            "token": access_token
        }), 200)
        return make_response(jsonify({
        "message": "Try again",
        }), 400)

        

