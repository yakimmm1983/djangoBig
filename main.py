from classLibrary import manager,smena ,user,pay,coffe,additional
def OpenSmena (exmanager:manager.manager):
      return smena.smena(exmanager)


def LoginManager(login,password):
    vallLogin="123"
    valPassword="123"
    name="Алексей"
    phone="89638874619"
    bonus=100
    if vallLogin == login and valPassword == password:
        exmanager = manager.manager(login=login,
                                    password=password,
                                    name=name,
                                    phone=phone,
                                    bonus=bonus)
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
        if manager is None:
            break
        _mainMenu = f"{manager.getName()}\n 1 - Открыть смену"
        choice = input(_mainMenu)
        if choice == "1":
            smena = OpenSmena(manager)
            payList = []
            while True:
                _mainMenu = f"{manager.getName()}\n1 - Закрыть смену\n2 - Покупка"
                choice = input(_mainMenu)

                if choice == "2":
                    additionals = []
                    coffees = []
                    summ = 0
                    smena.setSum(summ)
                    smena.setTimeClose()
                    while True:
                        _buyMenu = f"1 - Латте{' ' * 12}5 - Oreo\n2 - Капучино{' ' * 12}5 - Пончик\n3 - Американо{' ' * 12}6-Выход"
                        choice = input(_buyMenu)
                        if choice in ["1", "2", "3"]:
                            size = input("Выберите размер M,L,XL")
                            if size in ["M", "L", "XL"]:
                                if choice == "1":
                                    name = "Латте"
                                    coffePrice = 160
                                elif choice == "2":
                                    name = "Капучино"
                                    coffePrice = 140
                                elif choice == "3":
                                    name = "Американо"
                                    coffePrice = 100
                                _buyMenu = f"1-Сироп,2-Сливки,3-без добавок"
                                choice = input(_buyMenu)
                                if choice == "1":
                                    type = "Сироп"
                                    price = 40
                                    additionals.append(additional.additional(type, size, price))
                                elif choice == "2":
                                    type = "Сливки"#####
                                    price = 60
                                    additionals.append(additional.additional(type, size, price))
                                coffees.append(coffe.coffe(name,size,coffePrice))#####
                            else:
                                continue


                        elif choice in ["4", "5"]:
                            if choice == "4":
                                count = int(input("колличество"))
                                for i in range(count):
                                    additionals.append(additional.additional("Oreo", "N/A", "150"))
                            elif choice == "5":
                                count = int(input("колличество"))
                                for i in range(count):
                                    additionals.append(additional.additional(
                                    "Oreo", "N/A", "100"))
                        elif choice == "6":
                            break
                        else:
                            continue
                        expay = pay.pay(
                            eMoney=True,
                            client=user.user(bonus=100, name="Андрей", phone=""),
                            additionals=additionals,
                            coffes=coffees
                        )
                        payList.append(expay)
                elif choice == "1":
                    summ = 0
                    for payItem in payList:
                        summ+=payItem.getSun()
                    smena.setSum(summ)
                    smena.setTimeClose()
                    break

        print(payList)
        break
    else:
        continue