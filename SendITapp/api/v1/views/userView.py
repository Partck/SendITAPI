from flask import request, make_response, jsonify
from flask_restful import Resource
from SendITapp.api.v1.models.users import UserModel


class User(Resource):
    """Handle user CRUD."""

    def post(self):
        """Create user."""
        data = request.get_json() or {}
        user = UserModel()

        for key in data.keys():
            #Check email validation
            if key == 'username' or key =='name':
                if data['username'] == "" or data['name'] == "":
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
                if data['password'] == "" or data['password'] != data["retype_password"]:
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



        reply_info = user.create_user(data["username"], data["name"],
         data["email"], data["role"], data["phone"], data["password"])

        if reply_info == True:
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
