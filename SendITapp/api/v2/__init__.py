"""From flask import Blueprint. Name it : api_v1."""
from flask import Blueprint
from SendITapp.api.v2.views.parcelview import AllParcels, SingleParcel,\
    ParcelsByUser, CancelParcelOrder, UpdateOrder
from flask_restful import Api
from SendITapp.api.v2.views.userView import User, SingleUser

superv2_blueprint = Blueprint("api_v2", __name__, url_prefix='/api/v2')

blueprint_api = Api(superv2_blueprint)

blueprint_api.add_resource(AllParcels, "/parcels")
blueprint_api.add_resource(SingleParcel, "/parcels/<parcelid>")
blueprint_api.add_resource(User, "/users")
blueprint_api.add_resource(SingleUser, "/users/<userid>")
blueprint_api.add_resource(ParcelsByUser, "/users/<userid>/parcels")
blueprint_api.add_resource(CancelParcelOrder, "/parcels/<parcelid>/cancel")
blueprint_api.add_resource(UpdateOrder, "/parcels/<parcelid>/update")
