from classLibrary.user import user
from classLibrary.additional import additional
from classLibrary.pay import pay

if __name__ == "__main__":
    user.create_table()
    additional.create_table()
    pay.create_table()
    print("Migration Done")