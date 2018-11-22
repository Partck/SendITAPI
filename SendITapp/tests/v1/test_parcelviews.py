
"""This test class tests the parcel_views."""
from ... import create_app
import unittest
from flask import Flask
import json
from SendITapp.tests.v1.test_data import incorrect_sender, missing_sender, data,\
 missing_destination, incorrect_recipient, missing_recipient, missing_weight,\
  incorrect_weight, incorrect_status


class TestParcelViews(unittest.TestCase):
    """Test the views for all http methods availed on test views."""

    def setUp(self):
        """Function tests creating a parcel with incomplete data."""
        create_app().testing = True
        self.app = create_app().test_client()


    def test_create_parcel_order(self):
        """Function tests creating a parcel."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data)
        self.assertIn('Created.....Your order is on its way', str(result))
        self.assertEqual(response.status_code, 200, msg="OK")
        self.assertIn('2', str(result))
        
    
    def test_create_parcel_missing_sender(self):
        """Function tests creating a parcel."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(missing_sender), content_type='application/json')
        result = json.loads(response.data)
        self.assertIn('Enter the sender', str(result))
        self.assertEqual(response.status_code, 400, msg="OK")
        
    
    def test_create_parcel_incorrect_sender(self):
        """Function tests creating a parcel."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(incorrect_sender), content_type='application/json')
        result = json.loads(response.data)
        self.assertIn('Incorrect input in sender', str(result))
        self.assertEqual(response.status_code, 400, msg="OK")
        

    def test_create_order_with_missing_destination(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(missing_destination), content_type='application/json')
        result = json.loads(response.data)
        self.assertIn('Enter the destination',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")

    def test_update_parcel(self):
        """Function tests updating a parcel."""
        response = self.app.patch('/api/v1/parcels/1/update', 
        data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data)
        self.assertIn('Order Updated', str(result))
        self.assertEqual(response.status_code, 200, msg="OK")

    def test_update_parcel_missing_destination(self):
        """Function tests updating a parcel with incomplete data."""
        response1 = self.app.patch('/api/v1/parcels/1/update', 
        data=json.dumps(missing_destination), content_type='application/json')
        result = json.loads(response1.data)
        self.assertEqual(response1.status_code, 400, msg="OK")
        self.assertIn('Enter the destination',
         str(result))

    def test_get_all_orders(self):
        """Function tests getting of all parcel orders."""
        response = self.app.get("/api/v1/parcels")
        result = json.loads(response.data)
        self.assertIn('OK', str(result))
        assert response.status_code == 200

    def test_get_one_order(self):
        """Function tests for getting one order."""
        response1 = self.app.get("/api/v1/parcels/1")
        result = json.loads(response1.data)
        self.assertIn('Not Found!!', str(result))
        assert response1.status_code == 404

    def test_get_orders_by_user(self):
        """Function tests getting orders by a user."""
        response = self.app.get("/api/v1/users/10/parcels")
        result = json.loads(response.data)
        self.assertIn('No parcel!', str(result))
        assert response.status_code == 404

    def test_cancel_order(self):
        """Function tests the cancel order end point."""
        response = self.app.put("/api/v1/parcels/1/cancel")
        result = json.loads(response.data)
        self.assertIn('Parcel Canceled!', str(result))
        assert response.status_code == 200


    def test_create_app_serves_flask_app(self):
        """Function tests create app."""
        self.assertTrue(isinstance(create_app(), Flask),
        msg="create app does not serve a flask instance")
    
    def test_create_order_with_incorrect_recipient(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(incorrect_recipient), content_type='application/json')
        result = json.loads(response.data)
        self.assertIn('Check the recipient.',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")

    def test_create_order_with_missing_recipient(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(missing_recipient), content_type='application/json')
        result = json.loads(response.data)
        self.assertIn('Enter the recipient',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")
    
    def test_create_order_with_missing_weight(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(missing_weight), content_type='application/json')
        result = json.loads(response.data)
        self.assertIn('Enter the weight',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")

    def test_create_order_with_incorrect_weight(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(incorrect_weight), content_type='application/json')
        result = json.loads(response.data)
        self.assertIn('Incorrect weight format.',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")
    
    def test_create_order_with_incorrect_status(self):
        """Function tests creating a parcel with incomplete data."""
        response = self.app.post('/api/v1/parcels', 
        data=json.dumps(incorrect_status), content_type='application/json')
        result = json.loads(response.data)
        self.assertIn('Price status is: Paid or Not Paid.',str(result))
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")


if __name__ == "__main__":
    unittest.main()

