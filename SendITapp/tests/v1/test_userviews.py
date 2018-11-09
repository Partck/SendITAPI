
"""This test class tests the parcel_views."""
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
                        "name": "Pit Pat",
                         "email": "pat@mail.com",
                          "role": "admin",
                          "phone": "0712304050",
                           "password": "qwerty"
                           }

    def test_create_user_order(self):
        """ Test create a new parcel order. """
        response = self.app.post('/api/v1/users', data=json.dumps(self.data), content_type='application/json')        
        self.assertEqual(response.status_code, 200, msg="OK")

    def test_get_all_users(self):
        """ This function tests getting of all users."""
        response = self.app.get("/api/v1/users")
        assert response.status_code == 200
    
    def test_get_single_user(self):
        """This function tests for getting one user."""
        response = self.app.get("/api/v1/users/4")
        assert response.status_code == 200
        response1 = self.app.get("/api/v1/users/10")
        assert response1.status_code == 404