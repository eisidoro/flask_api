from model.User import User

class UserController():
    def __init__(self):
        self.user_model = User()

    def login(self, email, password):
        self.user_model.email = email
        
        _user = self.user_model.get_user_by_email()

        if user_exists is not None:
            user_verified_pwd = self.user_model.verify_password(password, _user.password)

            if user_verified_pwd:
                return _user
            else:
                return {}
        return {}

    def recovery(email):
        return ''