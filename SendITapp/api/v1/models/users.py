"""Unique identifier library."""
import uuid


class UserModel(object):
    '''This class does User CRUD operations.
    '''
    user_data = []

    def create_user(self, username, name, email, role, phone, password):
        '''This method allows the admin to create a user'''

        self.username = username
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone
        self.password = password

        # Validate common user data.
        for user in UserModel.user_data:
            if user['username'] == self.username:
                message = 'The username is already in the system'
                return message
            if user['email'] == self.email:
                message = 'The email already in use in the system.'
                return message

            if user['phone'] == self.phone:
                message = 'This phone number is in use'
                return message

        id1 = str(uuid.uuid4().int)

        payload = {"userid": str(id1), "username": self.username,
                   "name": self.name, "email": self.email, "role": self.role,
                   "phone": self.phone, "password": self.password}

        UserModel.user_data.append(payload)
        return True

    def get_all(self):
        """Create users."""
        return UserModel.user_data

    def get_user(self, userid):
        for user in UserModel.user_data:
            if user['userid'] == userid:
                return user
            return False
