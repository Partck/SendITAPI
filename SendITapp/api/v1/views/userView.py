from flask import request, make_response, jsonify
from flask_restful import Resource
from SendITapp.api.v1.models.users import UserModel
import bcrypt


class User(Resource):
    """Handle user CRUD."""

    def post(self):
        """Create user."""
        data = request.get_json() or {}
        user = UserModel()

        if data['username'] == "":
            message = 'Check your usename'
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
            

    
        if data['role'] != "Admin"and data["role"] != "User":
            message = 'Role input can either be Admin or User'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            

    
        if data['phone'] == "":
            message = 'Enter a valid number.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            

        # password = bcrypt.hashpw(data["password"], bcrypt.gensalt())
        password = data['password']
        reply_info = user.create_user(data["username"], data["name"],
         data["email"], data["role"], data["phone"], password)

        if reply_info:
            user_data = {
                "username": data["username"],
                "name": data["name"],
                "Email": data["email"],
                "Role": data["role"],
                "phone": data["phone"]
                }

            payload = {"Status": "User Registered",
            "User": user_data}
            return make_response(jsonify(payload), 200)
            

        payload = {"Status": "Failed", "Message": reply_info}
        return make_response(jsonify(payload), 400)
        

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
            
