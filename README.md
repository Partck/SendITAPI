## By Partck 2018

[![Build Status](https://travis-ci.org/Partck/SendITAPI.svg?branch=develop)](https://travis-ci.org/Partck/SendITAPI) [![Coverage Status](https://coveralls.io/repos/github/Partck/SendITAPI/badge.svg?branch=develop)](https://coveralls.io/github/Partck/SendITAPI?branch=develop)[![Maintainability](https://api.codeclimate.com/v1/badges/981768bd757f1386b352/maintainability)](https://codeclimate.com/github/Partck/SendITAPI/maintainability)[![Test Coverage](https://api.codeclimate.com/v1/badges/981768bd757f1386b352/test_coverage)](https://codeclimate.com/github/Partck/SendITAPI/test_coverage)


 **SendIT** is a service that helps users track the parcel delivery orders

## How it Works:
    An user register into the system.
    A user can add a parcel delivery order
    A user can view a single delivery order
    A user can cancel a delivery order
    An Admin can fetch all delivery orders in the system
    A user can see their details
    A user can see all orders attached to a specific user

## Prerequisite
    Python3.6
    A Virtual Environment

## Installation and Setup
 Clone this repository: (https://github.com/Partck/SendITAPI.git)

    Create and activate a virtual environment
            virtualenv env --python=python3.6
            source env/bin/activate

    Install required Dependencies
        pip install -r requirements.txt

    Export flask file and run
        export FLASK_APP=run.py
        flask run

 URL FORMAT: `HOST/api/v1/endpoint`
     For example: (http://127.0.0.1:5000/api/v1/parcels)

 The `/SendITapp` has the following endpoints:

## Endpoints:
    - Create an account : api/v1/users
    - Create a parcel delivery order : api/v1/parcels
    - Fetch all parcel delivery orders  : api/v1/parcels
    - Fetch a specific parcel delivery order  : api/v1/parcels/<parcel_id>
    - Fetch all parcel delivery orders by a specific user  : api/v1/users/<user_id>/parcels
    - Cancel a specific parcel delivery order : api/v1/parcels/<parcel_id>/cancel



## Tests
 Steps to follow:
 Install the following packages in you virtual environment:
         pip install pytest
         pip install pytest-cov

 Running the tests:
         Run pytest in the terminal

 This application runs on Heroku at:(https://partck-sendit.herokuapp.com/api/v1/parcels)

 Add the endpoints to the app.
