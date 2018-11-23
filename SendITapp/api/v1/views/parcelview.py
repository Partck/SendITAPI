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
            "Status": "OK.",
            "Parcels": all_parcels
        }
        answ = make_response(jsonify(payload), 200)
        return answ

    def post(self):
        """Method to create a parcel order. It uses the POST method"""
        data = request.get_json() or {}
        """Check email validation."""            
        if data['sender'] == "" or data['sender'].isalpha()==False:
            message = 'Please confirm the sender'
            payload = {"Status": "Failed", "Message": message}
            answ = make_response(jsonify(payload), 400)
            return answ

    
        if data['destination'] == "" or data['recipient'] == ""\
        or data['recipient'].isalpha()== False or data['destination'].isalpha()==False:
            message = 'Check your details. Destination, Recipient...'
            payload = {"Status": "Failed", "Message": message}
            answ = make_response(jsonify(payload), 400)
            return answ

    
        if data['price'] == "" or data['weight'] == "":
            message = 'Kindly confirm the wight and pricing of your package'
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
    def patch(self, parcelid):
        """This method uses the PUT method to cancel a request."""
        data = request.get_json() or {}
        if data['sender'] == "":
            message = 'Please confirm the sender'
            payload = {"Status": "Failed", "Message": message}
            answ = make_response(jsonify(payload), 400)
            return answ

    
        if data['destination'] == "" or data['recipient'] == "":
            message = 'Check your details. Destination, Recipient...'
            payload = {"Status": "Failed", "Message": message}
            answ = make_response(jsonify(payload), 400)
            return answ

    
        if data['price'] == "" or data['weight'] == "":
            message = 'Kindly confirm the wight and pricing of your package'
            payload = {"Status": "Package status update failed", "Message": message, "Parcel": data}
            answ = make_response(jsonify(payload), 400)
            return answ
    
        if data['status'] == "":
            message = 'Kindly update the status of this package'
            payload = {"Status": "Package status update failed", "Message": message, "Parcel": data}
            answ = make_response(jsonify(payload), 400)
            return answ

        parcelid = str(parcelid)
        for item in Parcel.parcels:
            if item['id'] == parcelid:
                item["status"] = data["status"]
                item["price"] = data["price"]
                item["weight"] = data["weight"]
                item["sender"] = data["sender"]
                item["recipient"] = data["recipient"]
                item["destination"] = data["destination"]

        payload = {"Status": "Order Updated"}
        answ = make_response(jsonify(payload), 200)
        return answ


class CancelParcelOrder(Resource):
    """This class handles cancel order requests."""
    def put(self, parcelid):
        """This method uses the PUT method to cancel a request."""
        parcelid = str(parcelid)
        for item in Parcel.parcels:
            if item['id'] == parcelid:
                item["status"] = "Canceled"
        payload = {"Status": "Parcel Canceled!"}
        answ = make_response(jsonify(payload), 200)
        return answ
