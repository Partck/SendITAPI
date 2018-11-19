
from flask import request, make_response, jsonify
import re
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from SendITapp.api.v2.models.users import UserModel
from flask_jwt_extended import jwt_required


class Register(Resource):
    """Handle user CRUD."""

   

    def post(self):
        """Create user."""
        data = request.get_json() or {}
        user = UserModel()

        for key in data.keys():
            #Check email validation
            if key == 'username' or key == 'name':
                username = data['username'].replace(" ", "")
                name = data['name'].replace(" ", "")
                if not (re.match("^[a-zA-Z0-9_]*$", username)) or\
                    not (re.match("^[a-zA-Z0-9_]*$", name)):
                    message = 'Check your name and usename'
                    payload = {"Status": "Failed", "Message": message}
                    answ = make_response(jsonify(payload), 400)
                    answ.content_type = 'application/json;charset=utf-8'
                    return answ

            if key == 'email':
                if data[key].find("@") < 2:
                    message = 'Incorrect email format'
                    payload = {"Status": "Failed", "Message": message}
                    answ = make_response(jsonify(payload), 400)
                    answ.content_type = 'application/json;charset=utf-8'
                    return answ

            if key == 'password':
                password = data['password'].replace(" ", "")
                if not (re.match("^[a-zA-Z0-9_]*$", password)) or \
                data['password'] != data["retype_password"]:
                    message = 'Check your password.'
                    payload = {"Status": "Failed", "Message": message}
                    answ = make_response(jsonify(payload), 400)
                    answ.content_type = 'application/json;charset=utf-8'
                    return answ

            if key == 'role':
                if data['role'] != "Admin" and data["role"] != "User":
                    message = 'Role input can either be Admin or User'
                    payload = {"Status": "Failed", "Message": message}
                    answ = make_response(jsonify(payload), 400)
                    answ.content_type = 'application/json;charset=utf-8'
                    return answ

            if key == 'phone':
                if data['phone'] == "":
                    message = 'Enter a valid number.'
                    payload = {"Status": "Failed", "Message": message}
                    answ = make_response(jsonify(payload), 400)
                    answ.content_type = 'application/json;charset=utf-8'
                    return answ

        password = password = user.generate_hash(data['password'])
        reply_info = user.create_user(data["username"], data["name"],
         data["email"], data["role"], data["phone"], password)

        if reply_info:
            user_data = [data["username"], data["name"],
            data["email"], data["role"], data["phone"], data["password"]]

            payload = {"Status": "created",
            "User": user_data}
            answ = make_response(jsonify(payload), 200)
            answ.content_type = 'application/json;charset=utf-8'
            return answ

        payload = {"Status": "Failed", "Message": reply_info}
        answ = make_response(jsonify(payload), 400)
        answ.content_type = 'application/json;charset=utf-8'
        return answ

    @jwt_required
    def get(self):
        """Method to get all the parcels."""
        user1 = UserModel()
        all_users = user1.get_all()

        payload = {
            "Status": "Ok",
            "Users": all_users
        }
        answ = make_response(jsonify(payload), 200)
        answ.content_type = 'application/json;charset=utf-8'
        return answ


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
            answ = make_response(jsonify(reply), 200)
            answ.content_type = 'application/json;charset=utf-8'
            return answ
        else:
            pack = {"Status": "User does not exist!"}
            answ = make_response(jsonify(pack), 404)
            answ.content_type = 'application/json;charset=utf-8'
            return answ


class Login(Resource):
    """This class creates a view for login/authentication"""

    def post(self):
        data = request.get_json() or {}
        for key in data.keys():
            if key == 'email':
                if data[key].find("@") < 2:
                    message = 'Incorrect email format'
                    payload = {"Status": "Failed", "Message": message}
                    answ = make_response(jsonify(payload), 400)
                    answ.content_type = 'application/json;charset=utf-8'
                    return answ

            if key == 'password':
                password = data['password'].replace(" ", "")
                if not (re.match("^[a-zA-Z0-9_]*$", password)):
                    message = 'Check your password.'
                    payload = {"Status": "Failed", "Message": message}
                    answ = make_response(jsonify(payload), 400)
                    answ.content_type = 'application/json;charset=utf-8'
                    return answ
        user = UserModel()
        email = data["email"]
        password = data["password"]
        auth = user.user_login(email)
        if auth:
            if auth:
                access_token = create_access_token(identity=email)
                return make_response(jsonify({"message": "Successful login",
                "token": access_token
            }), 200)
        return make_response(jsonify({
            "message": "Try again",
            }), 400)

        return make_response(jsonify({
            "message": "Try again",
            }), 400)

