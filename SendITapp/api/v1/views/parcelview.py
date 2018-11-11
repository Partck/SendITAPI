"""Install relevant packages."""
from flask import request, make_response, jsonify
from flask_restful import Resource
from SendITapp.api.v1.models.parcel import Parcel

class AllParcels(Resource):
    """Class to handle parcel views."""

    def get(self):
        """Method to get all the parcels available in the system."""
        par1 = Parcel()
        all_parcels = par1.get_all()

        payload = {
            "Status": "OK",
            "Parcels": all_parcels
        }
        answ = make_response(jsonify(payload), 200)
        answ.content_type = 'application/json;charset=utf-8'
        return answ

    def post(self):
        """Method to create a parcel order. It uses the POST method"""
        data = request.get_json() or {}
        for key in data.keys():

            """Check email validation."""
            if key == 'sender' :
                if data['sender'] == "":
                    message = 'Please confirm the sender'
                    payload = {"Status": "Failed", "Message": message}
                    answ = make_response(jsonify(payload), 400)
                    answ.content_type = 'application/json;charset=utf-8'
                    return answ

            if key == 'destination' or key =='recipient':
                if data['destination'] == "" or data['recipient'] == "":
                    message = 'Check your details. Destination, Recipient...'
                    payload = {"Status": "Failed", "Message": message}
                    answ = make_response(jsonify(payload), 400)
                    answ.content_type = 'application/json;charset=utf-8'
                    return answ

            if key == 'price' or key == 'weight':
                if data['price'] == "" or data['weight'] == "":
                    message = 'Kindly confirm the wight and pricing of your package'
                    payload = {"Status": "Failed", "Message": message}
                    answ = make_response(jsonify(payload), 400)
                    answ.content_type = 'application/json;charset=utf-8'
                    return answ

        par1 = Parcel()
        par1.create_parcel(data["destination"], data["recipient"], data["sender"],
        data["weight"], data["price"])

        created_parcel = data["destination"], data["recipient"], data["sender"],\
                        data["weight"], data["price"]

        

        payload = {"Status": "OK", "Parcel": created_parcel}
        answ = make_response(jsonify(payload), 200)
        answ.content_type = 'application/json;charset=utf-8'
        return answ


class SingleParcel(Resource):
    """Single parcel class."""

    def get(self, parcelid):
        """Get single item."""
        parcel = Parcel()
        parcelid = str(parcelid)
        reply_message = False
        reply_message = parcel.get_one_parcel(parcelid)

        if reply_message:
            reply = {"Status": "OK", "reply_message": reply_message}
            answ = make_response(jsonify(reply), 200)
            answ.content_type = 'application/json;charset=utf-8'
            return answ
        else:
            pack = {"Status": "Not Found!!", "id": parcelid}
            answ = make_response(jsonify(pack), 404)
            answ.content_type = 'application/json;charset=utf-8'
            return answ


class ParcelsByUser(Resource):
    """Parcel by user."""

    def get(self, userid):
        """Get single item."""
        parcel = Parcel()
        reply_message = False
        userid = str(userid)
        reply_message = parcel.get_parcels_by_user(userid)

        if reply_message:
            reply = {"Status": "OK", "reply_message": reply_message}
            answ = make_response(jsonify(reply), 200)
            answ.content_type = 'application/json;charset=utf-8'
            return answ
        else:
            reply = {"Status": "No parcel!"}
            answ = make_response(jsonify(reply), 404)
            answ.content_type = 'application/json;charset=utf-8'
            return answ


class CancelParcelOrder(Resource):
    """This class handles cancel order requests."""
    def put(self, parcelid):
        """This method uses the PUT method to cancel a request."""
        parcelid = str(parcelid)
        for item in Parcel.parcels:
            if item['id'] == parcelid:
                item["status"] = "canceled"
        payload = {"Status": "OK", "Parcel":Parcel.parcels}
        answ = make_response(jsonify(payload), 200)
        answ.content_type = 'application/json;charset=utf-8'
        return answ

