from classLibrary import manager,smena ,user
def OpenSmena (exmanager:manager.manager):
      return smena.smena(exmanager)
def LoginManager(login,password):
    vallLogin="123"
    valPassword="123"
    name="Алексей"
    phone="89638874619"
    bonus=100
    if vallLogin == login and valPassword == password:
        exmanager = manager.manager(login,password,name,phone,bonus)
        return exmanager
    else:
        return None
_mainMenu:str
_buyMenu:str
_smenaMenu:str
while True:
    password = input ("введите пароль от кассы")
    if password == "qwerty":
        login = input("введите логин")
        passwordManager = input("введите пароль")
        manager = LoginManager(login,passwordManager)
        break
    else:
        continue