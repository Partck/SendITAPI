"""Import unique identifier library. Used to generate my Ids."""
import uuid

class Parcel(object):
    """Parcel model."""

    parcels = []
    def create_parcel(self, data):
        """Create parcel order. It stores data in a data list."""
        self.destination = data["destination"]
        self.recipient = data["recipient"]
        self.sender = data["sender"]
        self.weight = data["weight"]
        self.price = data["price"]
        self.status = data["status"]

        id1 = str(uuid.uuid4().int)
        userid = str(uuid.uuid4().int)
        
        payload = {"id": str(id1), "destination": self.destination,
        "recipient": self.recipient, "sender": self.sender,
        "weight": self.weight, "status": self.status, "price": self.price, "userid":userid}

        Parcel.parcels.append(payload)
        return True

    def get_all(self):
        """This method returns all parcels in the system."""
        return Parcel.parcels

    def get_one_parcel(self, id):
        """Create users."""
        for item in Parcel.parcels:
            if item['id'] == id:
                return item
            return False

    def get_parcels_by_user(self, userid):
        """Get parcels by user."""
        for item in Parcel.parcels:
            if item['userid'] == userid:
                return item
            return False
