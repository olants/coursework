# Updated Login Model
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_authenticated = False

    def authenticate(self):
        pass

    def logout(self):
        pass

    def reset_password(self, email):
        pass