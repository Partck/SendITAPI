
from flask import request, make_response, jsonify
from werkzeug.security import check_password_hash
import re
from flask_restful import Resource
from SendITapp.api.v2.models.users import UserModel
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import bcrypt


class Register(Resource):
    """Handle user CRUD."""

    def post(self):
        """Create user."""
        data = request.get_json() or {}
        user = UserModel()

        if data['username'] == "":
            message = 'Check your username'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)

        if data['name'] == "":
            message = 'Enter your name'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
             
        if data["email"].find("@") < 2:
            message = 'Incorrect email format'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
                
        if data['password'] == "":
            message = 'Enter your password.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)

        if data['password'] != data["retype_password"]:
            message = 'Passwords do not match.'
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
            
        # password = bcrypt.hashpw(data["password"], bcrypt.gensalt())
        reply_info = user.create_user(data)

        if reply_info:
            user_data = [data["username"], data["name"],
            data["email"], data["role"], data["phone"], data["password"]]

            payload = {"Status": "created",
            "User": user_data}
            return make_response(jsonify(payload), 200) 
        payload = {"Status": "Failed", "Message": reply_info}
        return make_response(jsonify(payload), 400)
        
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

        if data["email"] == "":
            message = 'Enter email'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)

        if data["email"].find("@") < 2:
            message = 'Incorrect email format'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
        
        if data["password"] == "":
            message = 'Enter your password.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)

        password = data['password'].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", password)):
            message = 'Check your password.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
                    
        user = UserModel()
        password = user.user_password(data["email"])
        email = user.user_email(data["email"])
        # if check_password_hash(password["password"], data["password"]):

        if data["password"] ==password["password"]:
            access_token = create_access_token(identity=email["email"])
            return make_response(jsonify({"message": "Successful login",
            "token": access_token
        }), 200)
        return make_response(jsonify({
        "message": "Try again",
        }), 400)