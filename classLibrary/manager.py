from classLibrary.user import user
class manager(user):
    _login:str
    _password:str
    def __init__(self, login, password, name, phone, bonus):
        super().__init__(name,phone,bonus)
        self._login = login
        self._password = password
    def getLogin(self):
        return self._login
    def getPassword(self):
        return self._password
