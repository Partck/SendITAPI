
"""This test class tests the user views. It tests most of the fucntionality in the User Views. """
from ... import create_app
import unittest
import json


class TestUserViews(unittest.TestCase):
    """
    Test the views for all http methods availed on test views."""

    def setUp(self):
        create_app().testing = True
        self.app = create_app().test_client()
        self.data = {
                    "username": "pato",
                    "name": "Pit Pat", "email": "pat@mail.com", "role": "Admin",
                    "phone": "0712304050", "password": "qwerty", "retype_password": "qwerty"
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
                    "name": "Pit Pat", "email": "pat@mail.com", "role": "Admin",
                    "phone": "0712304050", "password": "qwerty", "retype_password": "qwerty"
                    }
      

    def test_create_user_order(self):
        """ Test create a new parcel order. """
        response = self.app.post('/api/v1/users', data=json.dumps(self.data), content_type='application/json')
        response1 = self.app.post('/api/v1/users', data=json.dumps(self.data1), content_type='application/json')
        response2 = self.app.post('/api/v1/users', data=json.dumps(self.data2), content_type='application/json')
        response3 = self.app.post('/api/v1/users', data=json.dumps(self.data3), content_type='application/json')

        self.assertEqual(response.status_code, 200, msg="OK")
        self.assertEqual(response1.status_code, 400, msg="BAD REQUEST")
        self.assertEqual(response2.status_code, 400, msg="BAD REQUEST")
        self.assertEqual(response3.status_code, 400, msg="BAD REQUEST")


    def test_get_all_users(self):
        """ This function tests getting of all users."""
        response = self.app.get("/api/v1/users")
        assert response.status_code == 200
    
    def test_get_single_user(self):
        """This function tests for getting one user."""
        response1 = self.app.get("/api/v1/users/10")
        assert response1.status_code == 404