"""Import unique identifier library. Used to generate my Ids."""
import uuid


class Parcel(object):
    """Parcel model."""

    parcels = []

    def create_order(self, destination, recipient, sender, weight):
        """Create parcel order. It stores data in a data list"""
        self.destination = destination
        self.recipient = recipient
        self.sender = sender
        self.weight = weight

        # id1 = str(uuid.uuid4().int)
        id1 = "1"

        userid = "4"
        status = "pending"

        payload = {"id": str(id1), "destination": self.destination,
        "recipient": self.recipient, "sender": self.sender,
        "weight": self.weight, "userid": userid, "status": status}

        Parcel.parcels.append(payload)

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
