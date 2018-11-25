"""Import unique identifier library. Used to generate my Ids."""
import uuid
from SendITapp.db_config import DbConfig
import psycopg2
from flask_jwt_extended import get_jwt_identity
from psycopg2.extras import RealDictCursor

class Parcel(object):
    """Parcel model."""
    def __init__(self):
        self.conn = DbConfig()
        self.db = self.conn.init_db()
        self.cursor = self.db.cursor(cursor_factory=RealDictCursor)
        self.user = get_jwt_identity()
        
    def create_parcel(self,data):
        """Create parcel order. It stores data in a data list."""
        self.destination = data["destination"]
        self.recipient = data["recipient"]
        self.sender = data["sender"]
        self.weight = data["weight"]
        self.price = data["price"]
        self.status = data["status"]
        
        id1 = str(uuid.uuid4())
        try:
            self.cursor.execute("""SELECT (userid) FROM Users_table WHERE
                     email = %s""", (self.user, ))
            userid = self.cursor.fetchone()
            self.cursor.execute("""INSERT INTO Parcels_table (parcelid, weight, destination,\
                     sender, recipient, status, price, userid) VALUES
                     (%s, %s, %s, %s, %s, %s, %s, %s )""", (id1, self.weight,
                        self.destination, self.sender,
                    self.recipient, self.status, self.price, userid["userid"]))
            self.db.commit()
            self.cursor.execute("""SELECT parcelid, userid, sender, destination,\
         weight, price, status FROM Parcels_table\
                    WHERE parcelid = %s""", (id1, ))
            parcel_orders = self.cursor.fetchone()
            self.db.commit()                  
            return parcel_orders
        except (Exception, psycopg2.DatabaseError):
            return "Failed"
        finally:
            if self.db is not None:
                self.db.close()






       

    def get_all(self):
        """This method returns all parcels in the system."""
        self.cursor.execute("""SELECT parcelid, userid, sender, destination, 
        weight, price, status FROM Parcels_table""")
        parcel_orders = self.cursor.fetchall()               
        return parcel_orders

    def get_one_parcel(self, id):
        """Get one parcel."""
        self.cursor.execute("""SELECT parcelid, weight, destination,\
                     sender, recipient, status, price, userid\
                      FROM Parcels_table WHERE parcelid = %s""", (id, ))
        row = self.cursor.fetchone()
        self.db.close()
        return row

    def get_parcels_by_user(self, userid):
        """Get parcels by user."""
        self.cursor.execute("""SELECT parcelid, weight, destination,\
                     sender, recipient, status, price, userid\
                      FROM Parcels_table WHERE userid = %s""", (userid, ))
        row = self.cursor.fetchall()
        
        self.db.close()
        return row
    
    def cancel_pending_order(self, parcelid):
        """Cancel pending order."""
        sql = """UPDATE Parcels_table SET status = %s WHERE parcelid = %s"""
        val = ("Canceled", parcelid)
        try:
            self.cursor.execute(sql, val)
            self.db.commit()
            self.cursor.execute("""SELECT parcelid, weight, destination,
                    sender, recipient, status, price, userid FROM Parcels_table
                    WHERE parcelid = %s""", (parcelid, ))
            rows = self.cursor.fetchone()
            self.db.close()
            return rows
            
        except (Exception, psycopg2.DatabaseError):
            return "Error updating the record"
        finally:
            if self.db is not None:
                self.db.close()
    
    def update_pending_order(self, parcelid, destination):
        """Cancel pending order."""
        sql = """UPDATE Parcels_table SET destination = %s WHERE parcelid = %s"""
        val = (destination, parcelid)
        try:
            self.cursor.execute(sql, val)
            self.db.commit()
            self.cursor.execute("""SELECT parcelid, userid, destination, weight,
             price, status FROM Parcels_table WHERE parcelid = %s""", (parcelid, ))
            rows = self.cursor.fetchone()
            
            self.db.close()
            return rows
            
        except (Exception, psycopg2.DatabaseError):
            return "Error updating the record"
        finally:
            if self.db is not None:
                self.db.close()