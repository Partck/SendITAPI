
"""This test class tests the user views. It tests most of the fucntionality in the User Views. """
from ... import create_app
import unittest
import json
from instance.config import config
# from SendITapp.tests.v2.test_parcelorderviews import TestParcelViews


class TestUserViews(unittest.TestCase):
    """
    Test the views for all http methods availed on test views."""

    def setUp(self):
        create_app().testing = True
        self.app = create_app(config_class=config["test"]).test_client()
        self.data = {
                    "username": "pato",
                    "name": "Pit Pat", "email": "patf@mail.com", "role": "Admin",
                    "phone": "0733304050", "password": "qwerty", "retype_password": "qwerty"
                    }
        #Data containing empty name         
        self.data1 = {
                    "username": "",
                    "name": "Pit Pat", "email": "pat@mail.com", "role": "Admin",
                    "phone": "0712304050", "password": "qwerty", "retype_password": "qwerty"
                    }
        #Dataset containing an empty name            
        self.data2 = {
                    "username": "pato",
                    "name": "", "email": "pat@mail.com", "role": "Admin",
                    "phone": "0712304050", "password": "qwerty", "retype_password": "qwerty"
                    }
        #Dataset containing an incorrect email            
        self.data3 = {
                    "username": "pato",
                    "name": "Pit Pat", "email": "pamail.com", "role": "Admin",
                    "phone": "0712304050", "password": "qwerty", "retype_password": "qwerty"
                    }
        #Dataset containing an incorrect role            
        self.data4 = {
                    "username": "pato",
                    "name": "Pit Pat", "email": "pat@mail.com", "role": "admin",
                    "phone": "0712304050", "password": "qwerty", "retype_password": "qwerty"
                    }
            #login data sample
        self.login =    {
                "email": "pat@mail.com",
                "password": "qwerty"
                }


    def test_create_user_with_empty_username(self):
        """ Test create a new parcel order. """
        response1 = self.app.post('/api/v2/register',
        data=json.dumps(self.data1), content_type='application/json;charset=utf-8')
        result = json.loads(response1.data)
        self.assertIn('Check your username', str(result))
        self.assertEqual(response1.status_code, 400, msg="BAD REQUEST")

    def test_create_user_with_empty_name(self):
        """ Test create a new parcel order. """
        response2 = self.app.post('/api/v2/register',
        data=json.dumps(self.data2), content_type='application/json;charset=utf-8')
        result = json.loads(response2.data)
        self.assertIn('Enter your name', str(result))
        self.assertEqual(response2.status_code, 400, msg="BAD REQUEST")

    def test_create_user_with_incorrect_name(self):
        """ Test create a new parcel order. """
        response3 = self.app.post('/api/v2/register',
        data=json.dumps(self.data3), content_type='application/json;charset=utf-8')
        result = json.loads(response3.data)
        self.assertIn('Check your name.', str(result))
        self.assertEqual(response3.status_code, 400, msg="BAD REQUEST")

    def test_create_user_with_incorrect_role(self):
        """ Test create a new parcel order. """
        response4 = self.app.post('/api/v2/register',
         data=json.dumps(self.data4),content_type='application/json;charset=utf-8')
        result = json.loads(response4.data)
        self.assertIn('Check your name.', str(result))
        self.assertEqual(response4.status_code, 400, msg="BAD REQUEST")