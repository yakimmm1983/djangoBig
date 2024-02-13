from classLibrary.BaseModel import BaseModel
from peewee import *
class additional(BaseModel):
    id = PrimaryKeyField(column_name="id",unique=True)
    type = CharField(column_name="type",max_length=100)
    size = CharField(column_name="size",max_length=2)
    price = FloatField(column_name="price",null=False)
    class Meta:
        table_name = "additional"



    def getType(self):
        return self._type

    def getSize(self):
        return self._size

    def getPrise(self):
        return self._price