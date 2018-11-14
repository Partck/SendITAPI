
"""This test class tests the parcel_views. It tests most of the fucntionality in thr Parcel Order Views. """
from ... import create_app
import unittest
import json

class TestParcelViews(unittest.TestCase):
    """
    Test the views for all http methods availed on test views."""

    def setUp(self):
        create_app().testing = True
        self.app = create_app().test_client()
        self.data = {
            "destination": "Nairobi",
            "recipient": "John",
            "sender": "Maina",
            "weight": "24",
            "price": "100",
            "status": "Pending"
}

    def test_create_parcel_order(self):
        """ Test create a new parcel order. """
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')        
        self.assertEqual(response.status_code, 200, msg="OK")

    def test_get_all_orders(self):
        """ This function tests getting of all parcel orders"""
        response = self.app.get("/api/v1/parcels")
        assert response.status_code == 200

    def test_get_one_order(self):
        """This function tests for getting one order"""
        response1 = self.app.get("/api/v1/parcels/10")
        assert response1.status_code == 404

    def test_get_orders_by_user(self):
        """This function tests function for getting orders by a user"""
        
        response = self.app.get("/api/v1/users/10/parcels")
        assert response.status_code == 404

    def test_cancel_order(self):
        """This function tests the cancel order end point"""
        response = self.app.put("/api/v1/parcels/1/cancel")
        assert response.status_code == 200


if __name__ == "__main__":
    unittest.main()
