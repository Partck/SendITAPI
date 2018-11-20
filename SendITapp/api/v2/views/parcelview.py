"""Install relevant packages."""
import re
from flask import request, make_response, jsonify
from flask_restful import Resource
from SendITapp.api.v2.models.parcel import Parcel
from flask_jwt_extended import jwt_required, get_jwt_identity


class AllParcels(Resource):
    """Class to handle parcel views."""
    @jwt_required
    def get(self):
        """Method to get all the parcels available in the system."""
        par1 = Parcel()
        all_parcels = par1.get_all()

        payload = {
            "Status": "OK.",
            "Parcels": all_parcels
        }
        answ = make_response(jsonify(payload), 200)
        return answ

    @jwt_required
    def post(self):
        """Method to create a parcel order. It uses the POST method"""
        data = request.get_json() or {}
        sender = data['sender'].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", sender)) or \
        data['sender'] == "":
            message = 'Please confirm the sender'
            payload = {"Status": "Failed", "Message": message}
            answ = make_response(jsonify(payload), 400)
            return answ
        recipient = data['recipient'].strip()
        destination = data['destination'].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", recipient)) or \
        not (re.match("^[a-zA-Z0-9_]*$", destination)) or \
        data['destination'] == "" or data['recipient'] == "":
            message = 'Check your details. Destination, Recipient...'
            payload = {"Status": "Failed", "Message": message}
            answ = make_response(jsonify(payload), 400)
            return answ

    
        weight = data['weight'].strip()
        price_status = ["Paid", "Not Paid"]
        if data['price'] not in price_status or \
        not (re.match("^[a-zA-Z0-9_]*$", weight)) or \
        data['weight'] == "":
            message = 'Check Weight or Price. Price status is: Paid or Not Paid.'
            payload = {"Status": "Failed", "Message": message}
            answ = make_response(jsonify(payload), 400)
            return answ
    
        accepted=["Pending","Canceled","Delivered"]
        if data['status'] not in accepted:
                message = 'Status can only be Pending, Delivered or Canceled'
                payload = {"Status": "Failed", "Message": message, "Data": data['status']}
                answ = make_response(jsonify(payload), 400)
                return answ

        par1 = Parcel()
        par1.create_parcel(data["destination"], data["recipient"], data["sender"],
        data["weight"], data["price"], data["status"])

        payload = {"Status": "Created.....Your order is on its way", "Parcel": data}
        answ = make_response(jsonify(payload), 200)
        return answ


class SingleParcel(Resource):
    """Single parcel class."""
    @jwt_required
    def get(self, parcelid):
        """Get single item."""
        parcel = Parcel()
        parcelid = str(parcelid)
        reply_message = False
        reply_message = parcel.get_one_parcel(parcelid)

        if reply_message:
            reply = {"Status": "OK", "reply_message": reply_message}
            answ = make_response(jsonify(reply), 200)
            return answ
        else:
            pack = {"Status": "Not Found!!", "id": parcelid}
            answ = make_response(jsonify(pack), 404)
            return answ


class ParcelsByUser(Resource):
    """Parcel by user."""
    @jwt_required
    def get(self, userid):
        """Get single item."""
        parcel = Parcel()
        reply_message = False
        userid = str(userid)
        reply_message = parcel.get_parcels_by_user(userid)

        if reply_message:
            reply = {"Status": "OK", "reply_message": reply_message}
            answ = make_response(jsonify(reply), 200)
            return answ
        else:
            reply = {"Status": "No parcel!"}
            answ = make_response(jsonify(reply), 404)
            return answ


class UpdateOrder(Resource):
    """This class handles cancel order requests."""

    @jwt_required
    def patch(self, parcelid):
        """This method uses the PUT method to cancel a request."""
        data = request.get_json() or {}
        

            
        sender = data['sender'].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", sender)) or \
        data['sender'] == "":
            message = 'Please confirm the sender'
            payload = {"Status": "Failed", "Message": message}
            answ = make_response(jsonify(payload), 400)
            return answ

    
        recipient = data['recipient'].strip()
        destination = data['destination'].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", recipient)) or \
        not (re.match("^[a-zA-Z0-9_]*$", destination)) or \
        data['destination'] == "" or data['recipient'] == "":
            message = 'Check your details. Destination, Recipient...'
            payload = {"Status": "Failed", "Message": message}
            answ = make_response(jsonify(payload), 400)
            return answ

    
        weight = data['weight'].strip()
        price_status = ["Paid", "Not Paid"]
        if data['price'] not in price_status or \
        not (re.match("^[a-zA-Z0-9_]*$", weight)) or \
        data['weight'] == "":
            message = 'Check Weight or Price. Price status is: Paid or Not Paid.'
            payload = {"Status": "Failed", "Message": message}
            answ = make_response(jsonify(payload), 400)
            return answ
    
        accepted=["Pending","Canceled","Delivered"]
        if data['status'] not in accepted:
                message = 'Status can only be Pending, Delivered or Canceled'
                payload = {"Status": "Failed", "Message": message, "Data": data['status']}
                answ = make_response(jsonify(payload), 400)
                return answ
        parcelid = str(parcelid)
        pass


class CancelParcelOrder(Resource):
    """This class handles cancel order requests."""
    @jwt_required
    def put(self, parcelid):
        """This method uses the PUT method to cancel a request."""
        parcelid = str(parcelid)
        pass