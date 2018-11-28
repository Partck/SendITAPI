
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


    def test_create_user_with_correct_mail(self):
        """ Test create a new parcel order. """
        response = self.app.post('/api/v1/users', data=json.dumps(self.data),
        content_type='application/json;charset=utf-8')
        result = json.loads(response.data)
        self.assertIn('User Registered', str(result))
        self.assertEqual(response.status_code, 200, msg="OK")

    def test_create_user_with_empty_username(self):
        """ Test create a new parcel order. """
        response1 = self.app.post('/api/v1/users',
        data=json.dumps(self.data1), content_type='application/json;charset=utf-8')
        result = json.loads(response1.data)
        self.assertIn('Check your usename', str(result))
        self.assertEqual(response1.status_code, 400, msg="BAD REQUEST")

    def test_create_user_with_empty_name(self):
        """ Test create a new parcel order. """
        response2 = self.app.post('/api/v1/users',
        data=json.dumps(self.data2), content_type='application/json;charset=utf-8')
        result = json.loads(response2.data)
        self.assertIn('Enter your name', str(result))
        self.assertEqual(response2.status_code, 400, msg="BAD REQUEST")

    def test_create_user_with_incorrect_email(self):
        """ Test create a new parcel order. """
        response3 = self.app.post('/api/v1/users',
        data=json.dumps(self.data3), content_type='application/json;charset=utf-8')
        result = json.loads(response3.data)
        self.assertIn('Incorrect email format', str(result))
        self.assertEqual(response3.status_code, 400, msg="BAD REQUEST")

    def test_create_user_with_incorrect_role(self):
        """ Test create a new parcel order. """
        response4 = self.app.post('/api/v1/users',
         data=json.dumps(self.data4),content_type='application/json;charset=utf-8')
        result = json.loads(response4.data)
        self.assertIn('Role input can either be Admin or User', str(result))
        self.assertEqual(response4.status_code, 400, msg="BAD REQUEST")

    def test_get_all_users(self):
        """ This function tests getting of all users."""
        response = self.app.get("/api/v1/users")
        result = json.loads(response.data)
        assert response.status_code == 200
        self.assertIn('Ok', str(result))

    def test_get_single_user(self):
        """This function tests for getting one user."""
        response = self.app.post('/api/v1/users', data=json.dumps(self.data),
        content_type='application/json;charset=utf-8')
        result = json.loads(response.data)
        # print(result["User"]["username"])
        
        
        response1 = self.app.get("/api/v1/users/10")
        
        result = json.loads(response1.data)
        assert response1.status_code == 404
        self.assertIn('User does not exist!', str(result))



    