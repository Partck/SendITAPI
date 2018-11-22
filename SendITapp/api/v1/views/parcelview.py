"""Install relevant packages."""
from flask import request, make_response, jsonify
from flask_restful import Resource
from SendITapp.api.v1.models.parcel import Parcel
import re

class AllParcels(Resource):
    """Class to handle parcel views."""

    def get(self):
        """Method to get all the parcels available in the system."""
        parcel = Parcel()
        all_parcels = parcel.get_all()

        payload = {
            "Status": "OK.",
            "Parcels": all_parcels
        }
        
        return make_response(jsonify(payload), 200)

    def post(self):
        """Method to create a parcel order. It uses the POST method"""
        data = request.get_json() or {}
        """Check email validation."""            
        sender = data["sender"].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", sender)):
            message = 'Incorrect input in sender'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)

        if data["sender"] == "":
            message = 'Enter the sender'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            
        recipient = data["recipient"].strip()
        
        if not (re.match("^[a-zA-Z0-9_]*$", recipient)):
            message = 'Check the recipient.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
        
        destination = data["destination"].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", destination)):
            message = 'Check the destination.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)

        if data["destination"] == "":
            message = 'Enter the destination'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            
        if data["recipient"] == "":
            message = 'Enter the recipient'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
    
        weight = data["weight"].strip()
        price_status = ["Paid", "Not Paid"]
        if data['price'] not in price_status:
            message = 'Price status is: Paid or Not Paid.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            
        if not (re.match("^[a-zA-Z0-9_]*$", weight)):
            message = 'Incorrect weight format.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            
        if data["weight"] == "":
            message = 'Enter the weight'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
            
    
        accepted=["Pending","Canceled","Delivered"]
        if data["status"] not in accepted:
                message = 'Status can only be Pending, Delivered or Canceled'
                payload = {"Status": "Failed", "Message": message, "Data": data['status']}
                return make_response(jsonify(payload), 400)
        parcel = Parcel()
        parcel.create_parcel(data)

        payload = {"Status": "Created.....Your order is on its way", "Parcel": data}
        return make_response(jsonify(payload), 200)
        

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
            return make_response(jsonify(reply), 200)
        else:
            pack = {"Status": "Not Found!!", "id": parcelid}
            return make_response(jsonify(pack), 404)
            

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
            return make_response(jsonify(reply), 200)
            
            
        else:
            reply = {"Status": "No parcel!"}
            return make_response(jsonify(reply), 404)
            


class UpdateOrder(Resource):
    """This class handles cancel order requests."""
    def patch(self, parcelid):
        """This method uses the PUT method to cancel a request."""
        data = request.get_json() or {}
        if data['sender'] == "":
            message = 'Please confirm the sender'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
    
        if data['destination'] == "":
            message = 'Enter the destination'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)

        price_status = ["Paid", "Not Paid"]
        if data['price'] not in price_status:
            message = 'Price status is: Paid or Not Paid.'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)

        if data['recipient'] == "":
            message = 'Enter the recipient'
            payload = {"Status": "Failed", "Message": message}
            return make_response(jsonify(payload), 400)
       
        if data['weight'] == "":
            message = 'Kindly confirm the wight and pricing of your package'
            payload = {"Status": "Failed", "Message": message, "Parcel": data}
            return make_response(jsonify(payload), 400)
             
    
        if data['status'] == "":
            message = 'Kindly update the status of this package'
            payload = {"Status": "Failed", "Message": message, "Parcel": data}
            return make_response(jsonify(payload), 400)
            

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
        return make_response(jsonify(payload), 200)
        


class CancelParcelOrder(Resource):
    """This class handles cancel order requests."""
    def put(self, parcelid):
        """This method uses the PUT method to cancel a request."""
        parcelid = str(parcelid)
        for item in Parcel.parcels:
            if item['id'] == parcelid:
                item["status"] = "Canceled"
        payload = {"Status": "Parcel Canceled!"}
        return make_response(jsonify(payload), 200)
        
