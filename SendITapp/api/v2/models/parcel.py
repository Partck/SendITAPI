"""Import unique identifier library. Used to generate my Ids."""
import uuid
from SendITapp.db_config import init_db


class Parcel(object):
    """Parcel model."""

    def create_parcel(self, destination, recipient, sender, weight, price, status):
        """Create parcel order. It stores data in a data list."""
        self.db = init_db()
        self.destination = destination
        self.recipient = recipient
        self.sender = sender
        self.weight = weight
        self.price = price
        self.status = status

        id1 = str(uuid.uuid4())
        userid = str(uuid.uuid4())

        cursor = self.db.cursor()
        cursor.execute("""INSERT INTO Parcels_table (parcelid, weight, destination,
                     sender, recipient, status, price, userid) VALUES
                     (%s, %s, %s, %s, %s, %s, %s, %s )""", (id1, self.weight,
                        self.destination, self.sender,
                    self.recipient, self.status, self.price, userid))
        self.db.commit()
        self.db.close()
        return True

    def get_all(self):
        """This method returns all parcels in the system."""
        self.db = init_db()
        conn = self.db
        cur = conn.cursor()
        cur.execute("""SELECT (parcelid, weight, destination,\
                     sender, recipient, status, price, userid) FROM Parcels_table""")
        rows = cur.fetchall()
        conn.close()
        return rows

    def get_one_parcel(self, id):
        """Get one parcel."""
        self.db = init_db()
        conn = self.db
        cur = conn.cursor()
        cur.execute("""SELECT (parcelid, weight, destination,\
                     sender, recipient, status, price, userid)\
                      FROM Parcels_table WHERE parcelid = %s""", (id, ))
        row = cur.fetchone()
        conn.close()
        return row

    def get_parcels_by_user(self, userid):
        """Get parcels by user."""
        self.db = init_db()
        conn = self.db
        cur = conn.cursor()
        cur.execute("""SELECT (parcelid, weight, destination,\
                     sender, recipient, status, price, userid)\
                      FROM Parcels_table WHERE userid = %s""", (id, ))
        row = cur.fetchone()
        conn.close()
        return row
