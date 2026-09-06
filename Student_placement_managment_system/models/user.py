class User:
    def __init__(self, user_id, name, email):
        self._user_id = user_id
        self._name = name
        self._email = email

    def get_details(self):
        return {
            "id": self._user_id,
            "name": self._name,
            "email": self._email
        }
