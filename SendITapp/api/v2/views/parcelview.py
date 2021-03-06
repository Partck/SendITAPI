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
        parcel = Parcel()
        all_parcels = parcel.get_all()

        payload = {
            "Status": "OK.",
            "Parcels": all_parcels
        }
        answer = make_response(jsonify(payload),200)
        answer.content_type='application/json;charset=utf-8'
        return answer
        

    @jwt_required
    def post(self):
        """Method to create a parcel order. It uses the POST method"""
        data = request.get_json() or {}
        if not data:
            return "please fill the fields"
   
        sender = data["sender"].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", sender)):
            message = 'Incorrect input in sender'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer

        if data["sender"] == "":
            message = 'Enter the sender'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
        recipient = data["recipient"].strip()
        
        if not (re.match("^[a-zA-Z0-9_]*$", recipient)):
            message = 'Check the recipient.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        
        destination = data["destination"].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", destination)):
            message = 'Check the destination.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer

        if data["destination"] == "":
            message = 'Enter the destination'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
        if data["recipient"] == "":
            message = 'Enter the recipient'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
    
        weight = data["weight"].strip()
        price_status = ["Paid", "Not Paid"]
        if data['price'] not in price_status:
            message = 'Price status is: Paid or Not Paid.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
        if not (re.match("^[a-zA-Z0-9_]*$", weight)):
            message = 'Incorrect weight format.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
        if data["weight"] == "":
            message = 'Enter the weight'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
    
        accepted=["Pending","Canceled","Delivered"]
        if data["status"] not in accepted:
                message = 'Status can only be Pending, Delivered or Canceled'
                payload = {"Status": "Failed", "Message": message, "Data": data['status']}
                answer = make_response(jsonify(payload),400)
                answer.content_type='application/json;charset=utf-8'
                return answer
                
        parcel = Parcel()
        response = parcel.create_parcel(data)
        if not response:
            payload = {"Status": "Not saved"}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer    
        payload = {"Status": "Created", "Parcel": response}
        answer = make_response(jsonify(payload),200)
        answer.content_type='application/json;charset=utf-8'
        return answer

        
        
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
            return make_response(reply, 200)
            
        else:
            pack = {"Status": "Not Found!!", "id": parcelid}
            return make_response(jsonify(pack), 404)
            
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
            return make_response(reply, 200)
            
        else:
            reply = {"Status": "No parcel!"}
            return make_response(jsonify(reply), 404)
            
class UpdateOrder(Resource):
    """This class handles cancel order requests."""

    @jwt_required
    def patch(self, parcelid):
        """This method uses the PUT method to cancel a request."""
        data = request.get_json() or {}
            
        recipient = data["recipient"].strip()
        
        if not (re.match("^[a-zA-Z0-9_]*$", recipient)):
            message = 'Check the recipient.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
        destination = data["destination"].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", destination)):
            message = 'Enter the destination.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
        if data["destination"] == "":
            message = 'Enter the destination'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        
        if data["recipient"] == "":
            message = 'Enter the recipient'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
        
        price_status = ["Paid", "Not Paid"]
        if data['price'] not in price_status:
            message = 'Price status is: Paid or Not Paid.'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
        weight = data["weight"].strip()    
        if not (re.match("^[a-zA-Z0-9_]*$", weight)):
            message = 'Incorrect weight format'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
        if data["weight"] == "":
            message = 'Enter the weight'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer
            
    
        accepted=["Pending","Canceled","Delivered"]
        if data["status"] not in accepted:
                message = 'Status can only be Pending, Delivered or Canceled'
                payload = {"Status": "Failed", "Message": message, "Data": data['status']}
                answer = make_response(jsonify(payload),400)
                answer.content_type='application/json;charset=utf-8'
                return answer
                
        parcelid = str(parcelid)
        pass


class CancelParcelOrder(Resource):
    """This class handles cancel order requests."""
    @jwt_required
    def put(self, parcelid):
        """This method uses the PUT method to cancel a request."""
        parcelid = str(parcelid)
        parcel = Parcel()
        query_result = parcel.cancel_pending_order(parcelid)
        if query_result:
            return query_result
        return "No record found!"


class UpdateDestinationOrder(Resource):
    """This class handles cancel order requests."""
    @jwt_required
    def put(self, parcelid):
        """This method uses the PUT method to cancel a request."""
        data = request.get_json() or {}
            
        destination = data["destination"].strip()
        if not (re.match("^[a-zA-Z0-9_]*$", destination)):
            message = 'Please confirm the sender'
            payload = {"Status": "Failed", "Message": message}
            answer = make_response(jsonify(payload),400)
            answer.content_type='application/json;charset=utf-8'
            return answer

        parcelid = str(parcelid)
        parcel = Parcel()
        query_result = parcel.update_pending_order(parcelid,destination)
        if query_result:
            return query_result
        return "No parcel found!"