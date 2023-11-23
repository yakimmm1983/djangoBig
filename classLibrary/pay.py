import datetime
from classLibrary.user import user
from classLibrary.coffe import coffe
from classLibrary.additional import additional

class pay:
    _date: datetime.date
    _eMoney: bool
    _client: user
    _sum = 0.0
    _sum:float
    _coffes:list[coffe]
    _additionals: list[additional]
    def __init__ (self,eMoney,client,coffes=None,additionals=None):
        if additionals is None:
            additionals = []
        if coffes is None:
            coffes = []
        self._eMoney = eMoney
        self._client = client
        self._coffes = coffes
        self._date = datetime.datetime.now().date()
        self._additionals = additionals
        if len(coffes) !=0:
            for coffe in self._coffes:
                self._sum += coffe.getPrise()
        if len(additionals) !=0:
            for additional in self._additionals:
                self._sum += additional.getPrise()
    def getSun(self):
        return self._sum