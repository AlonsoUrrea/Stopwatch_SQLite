#libaries
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import pathlib
import os
from sqlitemodel import SQL

#local
from QtUi import Ui_MainWindow
import storetime
from models import *

class InflatedStopwatchInterface(Ui_MainWindow):
    INTERVAL = 1000
    LOG_PATH = os.path.join(pathlib.Path().resolve(), "working_hours.log")
    DATE_FORMAT = "%Y-%m-%d"
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        today = datetime.datetime.today()
        self.today = datetime.datetime(
            year=today.year,
            month=today.month,
            day=today.day,
            hour=0, minute=0, second=0
        )
        self.seconder = QtCore.QTimer()
        self.counter = storetime.Time()
        self.record = Record()

        self.display()
    #end def
        
    def setupDb(self):
        Record().createTable()
    #end def

    # -- Behaviors
    def display(self):
        self.lcdTime.display(str(self.counter))
    #end def

    def log(self):
        self.record.unix_date = SqLiteConvertions.dateToUnix(self.today)
        self.record.seconds_worked = self.counter.totalSeconds()
        self.record.save()
    #end def
        
    def loadCounterFromLog(self, date: datetime.date=None):
        if date is None:
            date = self.today
        #end if
        record = Record().selectOne(SQL().WHERE('unix_date', '=', SqLiteConvertions.dateToUnix(date)))

        if record is None:
            return 
        #end if
        self.record = record
        self.counter = Time.from_seconds(record.seconds_worked)
    #end def


    # -- Events
    def addSecond(self):
        self.seconder.start(self.INTERVAL)
        self.counter.addSecond()
        self.display()
    #end def

    def clickStart(self):
        self.seconder.start(self.INTERVAL)
    #end def

    def clickPause(self):
        self.seconder.stop()
    #end def

    def clickStop(self):
        self.seconder.stop()
        if not self.counter.isReset():
            self.log()
        #end if
        self.counter.reset()
        self.display()
    #end def

    def clickPlusOne(self):
        self.counter.addMinute()
        self.display()
    def clickPlusTen(self):
        self.counter.addMinutes(10)
        self.display()
    #end def
    
    def clickClose(self):
        self.clickStop()
    #end def
#end class
