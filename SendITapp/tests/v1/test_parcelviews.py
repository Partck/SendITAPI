
"""This test class tests the parcel_views. It tests most of the fucntionality in thr Parcel Order Views. """
from ... import create_app
import unittest
from flask import Flask
import json


class TestParcelViews(unittest.TestCase):
    """
    Test the views for all http methods availed on test views."""

    def setUp(self):
        create_app().testing = True
        self.app = create_app().test_client()
        self.data = {
            "parcelid": "1",
            "destination": "Nairobi",
            "recipient": "John",
            "sender": "Maina",
            "weight": "24",
            "price": "Paid",
            "status": "Pending",
            "userid": "2"}

        self.incomplete_data = {
            "parcelid": "1",
            "destination": "",
            "recipient": "John",
            "sender": "Maina",
            "weight": "24",
            "price": "Paid",
            "status": "Pending",
            "userid": "2"}

    def test_create_parcel_order(self):
        """ Test create a new parcel order. """
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 200, msg="OK")

    def test_create_order_with_incomplete_data(self):
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.incomplete_data), content_type='application/json')
        self.assertEqual(response.status_code, 400, msg="BAD REQUEST")

    def test_update_parcel(self):
        response = self.app.patch('/api/v1/parcels/1/update', data=json.dumps(self.data), content_type='application/json')
        
        self.assertEqual(response.status_code, 200, msg="OK")
        
    def test_update_parcel_incomplete_data(self):
        response1 = self.app.patch('/api/v1/parcels/2/update', data=json.dumps(self.incomplete_data), content_type='application/json')

        self.assertEqual(response1.status_code, 400, msg="OK")


    def test_get_all_orders(self):
        """ This function tests getting of all parcel orders"""
        response = self.app.get("/api/v1/parcels")
        assert response.status_code == 200

    def test_get_one_order(self):
        """This function tests for getting one order"""
        response1 = self.app.get("/api/v1/parcels/1")
        assert response1.status_code == 404

    def test_get_orders_by_user(self):
        """This function tests function for getting orders by a user"""
        response = self.app.get("/api/v1/users/10/parcels")
        assert response.status_code == 404

    def test_cancel_order(self):
        """This function tests the cancel order end point"""
        response = self.app.put("/api/v1/parcels/1/cancel")
        assert response.status_code == 200

    def test_create_app_serves_flask_app(self):
        self.assertTrue(isinstance(create_app(), Flask), msg="create app does not serve a flask instance")

if __name__ == "__main__":
    unittest.main()