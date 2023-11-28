from uuid import uuid4

class AuthToken():
    def get_api_key(self):
        return uuid4()