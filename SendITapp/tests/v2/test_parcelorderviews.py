"""This test class tests the parcel_views."""
from werkzeug.security import generate_password_hash, check_password_hash
from SendITapp import create_app
import unittest
from flask import Flask
from flask_jwt_extended import create_access_token, get_jwt_identity
import json
import pytest
from instance.config import config
from SendITapp.tests.v2.tests_data import incorrect_sender, missing_sender, data,\
 missing_destination, incorrect_recipient, missing_recipient, missing_weight,\
  incorrect_weight, incorrect_status, data_login, data_register



class TestParcelViews(unittest.TestCase):
    """Test the views for all http methods availed on test views."""

    def setUp(self):
        """Function tests creating a parcel with incomplete data."""
        
        self.app = create_app(config_class=config["test"]).test_client()
        self.data = {
                    "username": "pato",
                    "name": "Pit Pat", "email": "deo32@mail.com", "role": "Admin",
                    "phone": "0713984050", "password": "qwerty", "retype_password": "qwerty"
                    }
        self.token = self.get_token()
                    
        
    
    def test_register(self):
        """ Tests create a new parcel order """

        response = self.app.post(
            "/api/v2/register",
            data=json.dumps(self.data),
            
            content_type='application/json', headers=self.token)

        resp_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Failed' in str(resp_data['Status'])
    

    def get_token(self):
        self.app.post('/api/v1/register', 
        data=json.dumps(data_register), content_type='application/json')
        response = self.app.post('/api/v2/login', data=json.dumps(data_login),
                                content_type='application/json')
        access_token = json.loads(response.get_data())['token']
        auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
        return auth_header
    
    def test_create_order(self):
        """Tests if an order has been created"""        
        res = self.app.post('/api/v2/parcels',
                               data=json.dumps(data),
                               content_type='application/json', headers=self.token)
        output = json.loads(res.data)
        self.assertEqual(output['Status'], "Created.....Your order is on its way")
        assert res.status_code == 200


    def test_create_parcel_missing_sender(self):
        """Function tests creating a parcel."""
        response = self.app.post('/api/v2/parcels', 
        data=json.dumps(missing_sender), content_type='application/json', headers=self.token)
        result = json.loads(response.data)
        self.assertIn('Enter the sender', str(result))
        self.assertEqual(response.status_code, 400, msg="OK")
    
    def test_create_parcel_incorrect_sender(self):
        """Function tests creating a parcel."""
        response = self.app.post('/api/v2/parcels', 
        data=json.dumps(incorrect_sender), content_type='application/json', headers=self.token)
        result = json.loads(response.data)
        self.assertIn('Incorrect input in sender', str(result))
        self.assertEqual(response.status_code, 400, msg="OK")

    def test_create_order_with_missing_destination(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(missing_destination), content_type='application/json', headers=self.token)
        result = json.loads(response.data)
        self.assertIn('Enter the destination',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")
    
    def test_update_parcel(self):
        """Function tests updating a parcel."""
        response = self.app.patch('/api/v1/parcels/1/update', 
        data=json.dumps(data), content_type='application/json', headers=self.token)
        result = json.loads(response.data)
        self.assertIn('Order Updated', str(result))
        self.assertEqual(response.status_code, 200, msg="OK")
    
    def test_update_parcel_missing_destination(self):
        """Function tests updating a parcel with incomplete data."""
        response1 = self.app.patch('/api/v1/parcels/1/update', 
        data=json.dumps(missing_destination), content_type='application/json', headers=self.token)
        result = json.loads(response1.data)
        self.assertEqual(response1.status_code, 400, msg="OK")
        self.assertIn('Enter the destination',
         str(result))
    
    def test_create_order_with_incorrect_recipient(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(incorrect_recipient), content_type='application/json', headers=self.token)
        result = json.loads(response.data)
        self.assertIn('Check the recipient.',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")
    

    def test_create_order_with_missing_recipient(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(missing_recipient), content_type='application/json', headers=self.token)
        result = json.loads(response.data)
        self.assertIn('Enter the recipient',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")
    
    def test_create_order_with_missing_weight(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(missing_weight), content_type='application/json', headers=self.token)
        result = json.loads(response.data)
        self.assertIn('Enter the weight',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")
    
    def test_create_order_with_incorrect_weight(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(incorrect_weight), content_type='application/json', headers=self.token)
        result = json.loads(response.data)
        self.assertIn('Incorrect weight format.',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")

    def test_create_order_with_incorrect_status(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(incorrect_status), content_type='application/json', headers=self.token)
        result = json.loads(response.data)
        self.assertIn('Price status is: Paid or Not Paid.',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")