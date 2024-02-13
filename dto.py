from classLibrary.user import user
from classLibrary.additional import additional
from classLibrary.pay import pay
def FillUser():
    userC = user(name = "олег",phone = "+79638874619",bonus = 0)
    userC.save()
def SelectUser():
    users = user.select()
    for user1 in users:
        print(user1.id,user1.name,user1.phone,user1.bonus)
def SelectUserByPhone(phone:str):
    user2 = user.select().where(user.phone == phone).get()
    user2.name = "вадим"
    user2.save()
def CreateAdditional():
    additional1 = additional(size = "XL",type = "Сироп",price = 30.0)
    additional1.save()
    additional2 = additional(size="L", type="Сироп", price=20.0)
    additional2.save()
    additional3 = additional(size="M", type="Сироп", price=10.0)
    additional3.save()
def CreatePay(user:user,additional:additional):
    import datetime
    date = datetime.date
    pay1 = pay(date='2022-09-11',additionals=additional,client=user,eMoney=False,sum=additional.price)
    pay1.save()
def SelectPay(id:int):
    pay1 = pay.select().where(pay.id == id).get()
    print(pay1.additionals.type, pay1.sum)

if __name__ == "__main__":
    # user2 = user.select().where(user.phone == "+79638874619").get()
    # additional = additional.select().where((additional.type == "Сироп") &(additional.size == "L")).get()
    # CreatePay(user2,additional)
    SelectPay(1)