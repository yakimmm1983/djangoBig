from classLibrary.manager import manager
import datetime

class smena:
    _date:datetime.date
    _timeOpen:datetime.time
    _timeClose:datetime.time
    _sum:float
    _manager:manager
    def __init__(self,manager):
        self._date = datetime.datetime.now().date()
        self._timeOpen = datetime.datetime.now().time()
        self._manager = manager
    def getDate(self):
        return self._date
    def getTimeOpen(self):
        return self._timeOpen
    def getTimeClose(self):
        return self._timeClose
    def setTimeClose(self):
        self._timeClose = datetime.datetime.now().time()
    def getManager(self):
        return self._manager
    def getSum(self):
        return self._sum
    def setSum(self,sum):
        self._sum = sum

