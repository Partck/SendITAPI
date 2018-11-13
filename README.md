#By Partck
# SendITAPI
[![Coverage Status](https://coveralls.io/repos/github/Partck/SendITAPI/badge.svg?branch=test_setup)](https://coveralls.io/github/Partck/SendITAPI?branch=test_setup)


SendIT API

Fast food fast is a fast food delivery web application.
How it Works

    An user register into the system.
    A user can add a parcel delivery order
    A user can view a single delivery order
    A user can cancel a delivery order
    Admin can fetch all delivery orders in the system
    A user can see their details
    A user can see all orders attached to a specific user

Prerequisite

    Python3.6
    A Virtual Environment

Installation and Setup

Clone the repository below

https://github.com/Partck/SendITAPI.git

Create and activate a virtual environment

virtualenv env --python=python3.6

source env/bin/activate

Install required Dependencies

pip install -r requirements.txt

Export flask file and run

export FLASK_APP=run.py

flask run

url: host/api/v1/endpoint

For example: http://127.0.0.1:5000/api/v1/parcels

Endpoints
/parcels
/parcels/<parcelId>
/users/<userId>/parcels
/parcels/<parcelId>/cancel
/users
/users/<userid>
/users/<userid>/parcels
